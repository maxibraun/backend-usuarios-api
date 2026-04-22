from flask import Flask
from routes.usuarios import usuarios_bp
from routes.auth import auth_bp
from flasgger import Swagger
from database import engine, Base
from models.usuario import Usuario
from flask_jwt_extended import JWTManager

app = Flask(__name__)

jwt = JWTManager(app)

from datetime import timedelta
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=30)

app.register_blueprint(auth_bp)

swagger = Swagger(app)

Base.metadata.create_all(bind=engine)

# registrar rutas
app.register_blueprint(usuarios_bp)

@app.route("/")
def home():
    return "API funcionando 🚀"

if __name__ == "__main__":
    app.run()