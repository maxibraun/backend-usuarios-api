from flask import Flask, jsonify, request
from sqlalchemy import create_engine, Column, Integer, String, func
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

# 🔌 conexión 
import os
DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

Session = sessionmaker(bind=engine)
Base = declarative_base()

# 🧱 modelo
class Usuario(Base):
    __tablename__ = "usuario"
    
    idusuario = Column(Integer, primary_key=True)
    nombre = Column(String)
    idpersona = Column(Integer)

# 📌 endpoint: lista + filtro
@app.route("/usuarios")
def get_usuarios():
    session = Session()
    
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

# 📌 endpoint: por id
@app.route("/usuarios/<int:id>")
def get_usuario(id):
    session = Session()
    
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

if __name__ == "__main__":
    app.run(debug=True)