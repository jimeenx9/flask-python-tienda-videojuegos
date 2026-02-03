from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class Categoria(db.Model):
    __tablename__ = "categorias"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    articulos = db.relationship(
        "Articulo",
        backref="categoria",
        cascade="all, delete-orphan",
        lazy=True
    )

    def __repr__(self):
        return f"<Categoria {self.nombre}>"


class Articulo(db.Model):
    __tablename__ = "articulos"

    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    iva = db.Column(db.Integer, nullable=False, default=21)
    descripcion = db.Column(db.Text)
    imagen = db.Column(db.String(200))
    stock = db.Column(db.Integer, default=0)

    categoria_id = db.Column(
        db.Integer,
        db.ForeignKey("categorias.id"),
        nullable=False
    )

    def precio_final(self):
        return self.precio + (self.precio * self.iva / 100)

    def __repr__(self):
        return f"<Articulo {self.nombre}>"


class Usuario(db.Model, UserMixin):
    __tablename__ = "usuarios"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(255), nullable=False)
    nombre = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(200), nullable=False, unique=True)
    admin = db.Column(db.Boolean, default=False)

    # --- Password helpers ---
    @property
    def password(self):
        raise AttributeError("password is not a readable attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_admin(self):
        return self.admin

    def __repr__(self):
        return f"<Usuario {self.username}>"
