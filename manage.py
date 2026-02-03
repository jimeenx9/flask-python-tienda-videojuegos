from click import echo
from aplicacion.app import app
from aplicacion.models import db, Categoria, Articulo, Usuario
from getpass import getpass

@app.cli.command("create_tables")
def create_tables():
    """Create relational database tables."""
    db.create_all()
    echo("Create relational database tables.")

@app.cli.command("drop_tables")
def drop_tables():
    """Drop all project relational database tables. THIS DELETES DATA."""
    db.drop_all()
    echo("Drop all project relational database tables. THIS DELETES DATA.")

@app.cli.command("add_data_tables")
def add_data_tables():
    """Create tables and insert demo data."""
    db.create_all()

    categorias = ["Deportes", "Arcade", "Carreras", "Acción"]
    for cat in categorias:
        db.session.add(Categoria(nombre=cat))
    db.session.commit()

    juegos = [
        {"nombre": "Fernando Martín Basket", "precio": 12, "descripcion": "Baloncesto 1 contra 1", "stock": 10, "categoria_id": 1, "imagen": "basket.jpeg", "iva": 21},
        {"nombre": "Hyper Soccer", "precio": 10, "descripcion": "Fútbol Konami", "stock": 7, "categoria_id": 1, "imagen": "soccer.jpeg", "iva": 21},
        {"nombre": "Arkanoid", "precio": 15, "descripcion": "Arcade clásico", "stock": 10, "categoria_id": 2, "imagen": "arkanoid.jpeg", "iva": 21},
        {"nombre": "Tetris", "precio": 6, "descripcion": "Puzzle clásico", "stock": 5, "categoria_id": 2, "imagen": "tetris.jpeg", "iva": 21},
        {"nombre": "Road Fighter", "precio": 15, "descripcion": "Carreras arcade", "stock": 10, "categoria_id": 3, "imagen": "road.jpeg", "iva": 21},
        {"nombre": "Out Run", "precio": 10, "descripcion": "Carreras Sega", "stock": 3, "categoria_id": 3, "imagen": "outrun.jpeg", "iva": 21},
        {"nombre": "Army Moves", "precio": 8, "descripcion": "Acción clásica", "stock": 8, "categoria_id": 4, "imagen": "army.jpeg", "iva": 21},
        {"nombre": "La Abadía del Crimen", "precio": 4, "descripcion": "Aventura española", "stock": 10, "categoria_id": 4, "imagen": "abadia.jpeg", "iva": 21},
    ]

    for jue in juegos:
        db.session.add(Articulo(**jue))

    db.session.commit()
    echo("Datos de ejemplo insertados.")

@app.cli.command("create_admin")
def create_admin():
    """Create admin user"""
    username = input("Usuario: ")
    password = getpass("Password: ")
    nombre = input("Nombre completo: ")
    email = input("Email: ")

    user = Usuario(
        username=username,
        nombre=nombre,
        email=email,
        admin=True
    )
    user.password = password  # ← aquí se hashea automáticamente

    db.session.add(user)
    db.session.commit()

    echo("Usuario administrador creado.")

