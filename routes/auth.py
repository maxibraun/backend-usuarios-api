from flask import Blueprint, request, jsonify
from database import SessionLocal
from models.usuario import Usuario
import bcrypt

auth_bp = Blueprint("auth", __name__)

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    username = data.get("username")
    password = data.get("password")

    if username != "admin" or password != "1234":
        return {"error": "Credenciales inválidas"}, 401

    access_token = create_access_token(identity=username)

    return {"access_token": access_token}, 200


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

        # 🔴 Validaciones
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

        # 🧱 Crear usuario
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