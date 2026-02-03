# 🎮 Proyecto Tienda de Videojuegos – Flask + SQLAlchemy

📚 **Asignatura:** Desarrollo Web / Backend

🧠 **Tecnologías:** Python · Flask · SQLAlchemy · Flask-Login · Jinja2 · SQLite

🛠 **Entorno:** WSL · VS Code

👤 **Autor:** Alberto Jiménez Rodríguez

📅 **Estado:** ✅ Funcional – Login, permisos, carrito con cookies

---

## 📸 CAPTURAS DEL PROYECTO

> Las capturas del proyecto se almacenan en la carpeta:
> 

```
aplicacion/static/capturas/

```

Ejemplo de uso en README / Notion:

```markdown
![Vista principal](aplicacion/static/capturas/inicio.png)
![Login](aplicacion/static/capturas/login.png)
![Carrito](aplicacion/static/capturas/carrito.png)

```


---

## 🧠 Objetivo del proyecto

Desarrollar una **aplicación web completa con Flask** que implemente:

- Gestión de usuarios (registro, login, logout)
- Control de acceso por roles (admin / usuario)
- Persistencia de datos con ORM
- Gestión de sesiones y cookies
- Carrito de la compra funcional
- Renderizado dinámico con plantillas

---

## 🖥️ Entorno de desarrollo

### 🐧 WSL (Windows Subsystem for Linux)

El proyecto se ha desarrollado íntegramente en **WSL**, lo que permite:

- Entorno Linux real
- Uso directo de Python, pip y Flask
- Mejor organización de rutas y permisos

📌 **Ruta del proyecto:**

```bash
./***/Proyectos/ProyectoFlaskSQL

```

---

## ⚙️ Preparación del entorno

### 1️⃣ Crear entorno virtual

```bash
python3 -m venv venv
source venv/bin/activate

```

---

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt

```

---

### 3️⃣ Lanzar la aplicación

Desde la raíz del proyecto:

```bash
flask --app manage.py run --debug
```

O alternativamente:

```bash
python aplicacion/app.py

```

📍 **URL local:**

```
http://127.0.0.1:5000

```

---

## 🗂️ Estructura del proyecto

```
ProyectoFlaskSQL/
│
├── aplicacion/
│   ├── app.py# Rutas y controladores
│   ├── config.py# Configuración Flask
│   ├── models.py# Modelos ORM
│   ├── forms.py# Formularios Flask-WTF
│   ├── dbase.db# Base de datos SQLite
│   │
│   ├──static/
│   │   ├── img/# Imágenes de artículos
│   │   └── capturas/# Capturas del proyecto
│   │
│   └── templates/
│       ├──base.html
│       ├── base2.html
│       ├── inicio.html
│       ├── login.html
│       ├── carrito_add.html
│       ├── categorias*.html
│       ├── articulos*.html
│       └── usuarios_new.html
│
├── venv/# Entorno virtual
├── requirements.txt
├── manage.py
└── README.md

```

---

## 🧱 Modelo de datos (ORM)

### 📦 Entidades principales

- 👤 **Usuario**
- 🏷 **Categoria**
- 🎮 **Articulo**

### 🔗 Relaciones

- Una **Categoría** tiene muchos **Artículos**
- Un **Usuario** puede tener múltiples artículos en su carrito (cookies)

---

## 🔐 Autenticación y autorización

### ✔️ Login / Logout

- Implementado con **Flask-Login**
- Contraseñas hasheadas
- Redirección segura con `next`

### ✔️ Control de acceso

- Rutas protegidas con `@login_required`
- Permisos de administrador
- Control en backend y frontend (plantillas)

---

## 🧾 Formularios (Flask-WTF)

Formularios implementados:

- `LoginForm`
- `formUsuario`
- `formArticulo`
- `formCategoria`
- `formChangePassword`
- `formCarrito`

✔️ Validaciones

✔️ Mensajes de error

✔️ CSRF activo

---

## 🛒 Carrito de la compra (Cookies + JSON)

- Cada usuario tiene una **cookie asociada a su ID**
- Los artículos se almacenan en formato **JSON**
- Estructura de la cookie:

```json
[
{
"id":1,
"cantidad":2
},
{
"id":2,
"cantidad":1
}
]

```

✔️ Añadir artículos

✔️ Actualizar cantidad

✔️ Comprobación de stock

---

## 🧠 Plantillas (Jinja2)

Uso de:

- Herencia (`extends`)
- Bloques (`block`)
- Variables
- Condicionales
- Bucles
- Control de permisos en vista

Ejemplo:

```
{% if current_user.is_authenticated %}
    <a href="{{ url_for('carrito_add', id=art.id) }}">Comprar</a>
{% endif %}

```

---

## ⚠️ Gestión de errores

- `abort(404)`
- `get_or_404`
- Página personalizada de error
- Redirecciones controladas

---

## 🏁 Funcionalidades implementadas (Checklist)

✅ Rutas estáticas

✅ Rutas dinámicas

✅ GET / POST

✅ Formularios HTML

✅ Subida de archivos

✅ ORM con SQLAlchemy

✅ Login / Logout

✅ Control de permisos

✅ Sesiones

✅ Cookies

✅ Carrito de la compra

---

## 🧾 Conclusión

Este proyecto representa una **aplicación Flask completa**, integrando:

- Backend real
- Seguridad básica
- Persistencia de datos
- Gestión de estado del usuario
- Arquitectura limpia y entendible

