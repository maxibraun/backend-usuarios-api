# 🚀 Backend Usuarios API

API REST desarrollada en Flask para gestión de usuarios, conectada a PostgreSQL usando SQLAlchemy.

---

## 🧰 Tecnologías

- Python
- Flask
- PostgreSQL
- SQLAlchemy

---

## 📌 Funcionalidades

- Obtener lista de usuarios
- Obtener usuario por ID
- Filtrar usuarios por nombre
- Manejo de errores

---

## ✨ Características destacadas

- API REST estructurada con Flask
- Arquitectura modular (routes, models, database)
- Conexión a PostgreSQL mediante SQLAlchemy
- Uso de variables de entorno para configuración segura
- Implementación de CRUD (Create, Read, Delete)

---

## ⚙️ Configuración

Definir la variable de entorno `DATABASE_URL`

Ejemplo:

postgresql+psycopg2://usuario:password@localhost:5432/tu_db

---

## ▶️ Cómo ejecutar el proyecto

1. Clonar el repositorio:

git clone https://github.com/maxibraun/backend-usuarios-api.git

2. Entrar a la carpeta:

cd backend-usuarios-api

3. Instalar dependencias:

pip install -r requirements.txt

4. Configurar variable de entorno:

En Windows (PowerShell):

$env:DATABASE_URL="postgresql+psycopg2://usuario:password@localhost:5432/tu_db"

5. Ejecutar la aplicación:

python app.py

---

## 🔗 Endpoints

### Obtener todos los usuarios

GET /usuarios

---

### Obtener usuario por ID

GET /usuarios/1

---

### Filtrar usuarios por nombre

GET /usuarios?nombre=Maxi

---

### Crear usuario

POST /usuarios

Body:
{
  "nombre": "Maxi",
  "idpersona": 123
}

---

### Eliminar usuario

DELETE /usuarios/<id>

Respuesta:
{
  "mensaje": "Usuario eliminado correctamente"
}

---

### Actualizar usuario

PUT /usuarios/<id>

Body:
{
  "nombre": "Nuevo Nombre",
  "idpersona": 123
}

---

## 🏗️ Estructura del proyecto

backend-usuarios-api/
│
├── app.py
├── database.py
├── models.py
├── requirements.txt
├── README.md
│
└── routes/
    └── usuarios.py

## ❗ Manejo de errores

## ❗ Manejo de errores

La API devuelve códigos HTTP apropiados:

- 200 OK → solicitud exitosa  
- 201 Created → recurso creado  
- 400 Bad Request → datos inválidos  
- 404 Not Found → recurso no encontrado  
- 500 Internal Server Error → error del servidor  

## 📷 Ejemplo de respuesta

```json
[
  {
    "id": 1,
    "nombre": "Maxi",
    "idpersona": 10
  }
]