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

@usuarios_bp.route("/usuarios", methods=["POST"])
def crear_usuario():
    session = SessionLocal()
    
    try:
        data = request.get_json()

        # 🛑 Validaciones básicas
        if not data:
            return jsonify({"error": "Body vacío"}), 400

        nombre = data.get("nombre")
        idpersona = data.get("idpersona")

        if not nombre:
            return jsonify({"error": "El campo 'nombre' es obligatorio"}), 400

        if not isinstance(nombre, str):
            return jsonify({"error": "'nombre' debe ser texto"}), 400

        if idpersona is not None and not isinstance(idpersona, int):
            return jsonify({"error": "'idpersona' debe ser número"}), 400

        # 🧱 Crear objeto
        nuevo_usuario = Usuario(
            nombre=nombre,
            idpersona=idpersona
        )

        session.add(nuevo_usuario)
        session.commit()
        session.refresh(nuevo_usuario)

        return jsonify({
            "id": nuevo_usuario.idusuario,
            "nombre": nuevo_usuario.nombre,
            "idpersona": nuevo_usuario.idpersona
        }), 201

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()
        
@usuarios_bp.route("/usuarios/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    session = SessionLocal()
    
    try:
        usuario = session.query(Usuario).filter(Usuario.idusuario == id).first()

        # 🛑 Validar si existe
        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        session.delete(usuario)
        session.commit()

        return jsonify({"mensaje": f"Usuario {id} eliminado correctamente"}), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()
        
@usuarios_bp.route("/usuarios/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    session = SessionLocal()
    
    try:
        data = request.get_json()

        # 🛑 Validar body
        if not data:
            return jsonify({"error": "Body vacío"}), 400

        # 🔎 Buscar usuario
        usuario = session.query(Usuario).filter(Usuario.idusuario == id).first()

        if not usuario:
            return jsonify({"error": "Usuario no encontrado"}), 404

        # 🧪 Obtener campos
        nombre = data.get("nombre")
        idpersona = data.get("idpersona")

        # 🛑 Validaciones
        if nombre is not None and not isinstance(nombre, str):
            return jsonify({"error": "'nombre' debe ser texto"}), 400

        if idpersona is not None and not isinstance(idpersona, int):
            return jsonify({"error": "'idpersona' debe ser número"}), 400

        # ✏️ Actualizar solo lo que venga
        if nombre is not None:
            usuario.nombre = nombre

        if idpersona is not None:
            usuario.idpersona = idpersona

        session.commit()

        return jsonify({
            "id": usuario.idusuario,
            "nombre": usuario.nombre,
            "idpersona": usuario.idpersona
        }), 200

    except Exception as e:
        session.rollback()
        return jsonify({"error": str(e)}), 500

    finally:
        session.close()