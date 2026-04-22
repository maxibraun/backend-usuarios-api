# 🚀 Backend Usuarios API

API REST desarrollada en Flask para gestión de usuarios, con autenticación JWT y base de datos PostgreSQL usando SQLAlchemy.

---

## 🧰 Tecnologías

- Python
- Flask
- SQLAlchemy
- PostgreSQL
- JWT (flask-jwt-extended)
- bcrypt
- Swagger (Flasgger)

---

## 📌 Funcionalidades

- Registro de usuarios (`/register`)
- Login con JWT (`/login`)
- CRUD de usuarios protegido
- Hash seguro de contraseñas (bcrypt)
- Validaciones básicas
- Documentación interactiva (Swagger)

---

## 🔐 Autenticación

La API utiliza JWT (JSON Web Tokens).

### Flujo:

1. Registrar usuario  
2. Login → obtener token  
3. Usar token en endpoints protegidos  

Header requerido:

Authorization: Bearer TU_TOKEN

---

## ⚙️ Configuración

Definir variables de entorno:

DATABASE_URL=postgresql+psycopg2://usuario:password@host:5432/db  
JWT_SECRET_KEY=super-secret-key

---

## ▶️ Cómo ejecutar el proyecto

git clone https://github.com/maxibraun/backend-usuarios-api.git  
cd backend-usuarios-api  
pip install -r requirements.txt  
python app.py  

---

## 🔗 Endpoints

### 🔓 Registro de usuario

POST /register

Body:

{
  "nombre": "maxi",
  "password": "1234",
  "idpersona": 123
}

---

### 🔓 Login

POST /login

Body:

{
  "nombre": "maxi",
  "password": "1234"
}

Respuesta:

{
  "access_token": "..."
}

---

### 🔒 Obtener usuarios

GET /usuarios

---

### 🔒 Obtener usuario por ID

GET /usuarios/<id>

---

### 🔒 Filtrar usuarios

GET /usuarios?nombre=Maxi

---

### 🔒 Actualizar usuario

PUT /usuarios/<id>

---

### 🔒 Eliminar usuario

DELETE /usuarios/<id>

---

## 📄 Swagger

http://127.0.0.1:5000/apidocs

---

## 🏗️ Estructura del proyecto

backend-usuarios-api/

├── app.py  
├── database.py  
├── models/  
│   └── usuario.py  
├── routes/  
│   ├── usuarios.py  
│   └── auth.py  
├── requirements.txt  
└── README.md  

---

## ❗ Manejo de errores

- Validación de datos de entrada  
- Manejo de excepciones con rollback de sesión  
- Respuestas JSON con mensajes de error claros  

---

## 🚀 Deploy

La API puede ser desplegada en Render utilizando:

- Web Service (Flask + Gunicorn)  
- PostgreSQL gestionado en Render  
- Variables de entorno configuradas en el dashboard  

---

## 📷 Ejemplo de respuesta

[
  {
    "id": 1,
    "nombre": "maxi",
    "idpersona": 16
  }
]