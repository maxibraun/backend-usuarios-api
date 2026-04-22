from flask import Flask
from routes.usuarios import usuarios_bp

app = Flask(__name__)

from database import engine
from models import Base
Base.metadata.create_all(bind=engine)

# registrar rutas
app.register_blueprint(usuarios_bp)

@app.route("/")
def home():
    return "API funcionando 🚀"

if __name__ == "__main__":
    app.run()