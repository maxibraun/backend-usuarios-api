from flask import Blueprint, jsonify, request
from sqlalchemy import func
from database import SessionLocal
from models import Usuario

usuarios_bp = Blueprint("usuarios", __name__)

@usuarios_bp.route("/usuarios")
def get_usuarios():
    session = SessionLocal()
    
    try:
        nombre = request.args.get("nombre")
        
        query = session.query(Usuario)
        
        if nombre:
            query = query.filter(func.lower(Usuario.nombre) == nombre.lower())
        
        usuarios = query.limit(10).all()
        
        resultado = []
        for u in usuarios:
            resultado.append({
                "id": u.idusuario,
                "nombre": u.nombre,
                "idpersona": u.idpersona
            })
        
        return jsonify(resultado)
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    finally:
        session.close()


@usuarios_bp.route("/usuarios/<int:id>")
def get_usuario(id):
    session = SessionLocal()
    
    try:
        usuario = session.query(Usuario).filter(Usuario.idusuario == id).first()
        
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404
        
        return jsonify({
            "id": usuario.idusuario,
            "nombre": usuario.nombre,
            "idpersona": usuario.idpersona
        })
    
    finally:
        session.close()