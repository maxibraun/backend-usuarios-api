from flask import Flask
from routes.usuarios import usuarios_bp

app = Flask(__name__)

# registrar rutas
app.register_blueprint(usuarios_bp)

@app.route("/")
def home():
    return "API funcionando 🚀"

if __name__ == "__main__":
    app.run()