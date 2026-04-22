from flask import Blueprint, request, jsonify
from database import SessionLocal
from models.usuario import Usuario
from flask_jwt_extended import create_access_token
import bcrypt

auth_bp = Blueprint("auth", __name__)

# 🔐 LOGIN REAL
@auth_bp.route("/login", methods=["POST"])
def login():
    session = SessionLocal()

    try:
        data = request.get_json()

        if not data:
            return {"error": "Body vacío"}, 400

        nombre = data.get("nombre")
        password = data.get("password")

        if not nombre or not password:
            return {"error": "nombre y password son obligatorios"}, 400

        # 🔍 Buscar usuario en BD
        usuario = session.query(Usuario).filter_by(nombre=nombre).first()

        if not usuario:
            return {"error": "Credenciales inválidas"}, 401

        # 🔐 Validar password con bcrypt
        if not bcrypt.checkpw(
            password.encode('utf-8'),
            usuario.password.encode('utf-8')
        ):
            return {"error": "Credenciales inválidas"}, 401

        # 🎟️ Generar token
        access_token = create_access_token(identity=usuario.nombre)

        return jsonify({
            "access_token": access_token
        }), 200

    except Exception as e:
        session.rollback()
        import traceback
        traceback.print_exc()
        return {"error": str(e)}, 500

    finally:
        session.close()


# 🧱 REGISTER
@auth_bp.route("/register", methods=["POST"])
def register():
    session = SessionLocal()

    try:
        data = request.get_json()

        if not data:
            return {"error": "Body vacío"}, 400

        nombre = data.get("nombre")
        password = data.get("password")
        idpersona = data.get("idpersona")

        if not nombre:
            return {"error": "nombre es obligatorio"}, 400

        if not password:
            return {"error": "password es obligatorio"}, 400

        # 🔴 Verificar duplicado
        existing_user = session.query(Usuario).filter_by(nombre=nombre).first()
        if existing_user:
            return {"error": "El usuario ya existe"}, 400

        # 🔐 Hash password
        hashed_password = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        nuevo_usuario = Usuario(
            nombre=nombre,
            idpersona=idpersona,
            password=hashed_password
        )

        session.add(nuevo_usuario)
        session.commit()
        session.refresh(nuevo_usuario)

        return jsonify({
            "message": "Usuario creado correctamente",
            "id": nuevo_usuario.idusuario
        }), 201

    except Exception as e:
        session.rollback()
        import traceback
        traceback.print_exc()
        return {"error": str(e)}, 500

    finally:
        session.close()