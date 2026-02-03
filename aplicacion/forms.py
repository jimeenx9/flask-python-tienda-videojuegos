from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    DecimalField,
    IntegerField,
    SelectField,
    TextAreaField,
    SubmitField,
    PasswordField,
    EmailField,
    HiddenField
)
from wtforms.validators import DataRequired,  NumberRange
from flask_wtf.file import FileField


# ---------- ARTÍCULOS ----------
class formArticulo(FlaskForm):
    nombre = StringField(
        "Nombre:",
        validators=[DataRequired("Tienes que introducir el dato")]
    )

    precio = DecimalField(
        "Precio:",
        default=0,
        validators=[DataRequired("Tienes que introducir el dato")]
    )

    iva = IntegerField(
        "IVA:",
        default=21,
        validators=[DataRequired("Tienes que introducir el dato")]
    )

    descripcion = TextAreaField("Descripción:")

    photo = FileField("Selecciona imagen:")

    stock = IntegerField(
        "Stock:",
        default=1,
        validators=[DataRequired("Tienes que introducir el dato")]
    )

    categoriaId = SelectField(
        "Categoría:",
        coerce=int
    )

    submit = SubmitField("Enviar")


# ---------- CATEGORÍAS ----------
class formCategoria(FlaskForm):
    nombre = StringField(
        "Nombre:",
        validators=[DataRequired("Tienes que introducir el dato")]
    )

    submit = SubmitField("Enviar")


# ---------- CONFIRMACIÓN SÍ / NO ----------
class formSINO(FlaskForm):
    si = SubmitField("Sí")
    no = SubmitField("No")


# ---------- LOGIN ----------
class LoginForm(FlaskForm):
    username = StringField(
        "Login:",
        validators=[DataRequired("Introduce el usuario")]
    )

    password = PasswordField(
        "Password:",
        validators=[DataRequired("Introduce la contraseña")]
    )

    submit = SubmitField("Entrar")


# ---------- REGISTRO / PERFIL USUARIO ----------
class formUsuario(FlaskForm):
    username = StringField(
        "Login:",
        validators=[DataRequired("Introduce el usuario")]
    )

    password = PasswordField(
        "Password:",
        validators=[DataRequired("Introduce la contraseña")]
    )

    nombre = StringField(
        "Nombre completo:",
        validators=[DataRequired("Introduce el nombre")]
    )

    email = EmailField(
        "Email:",
        validators=[DataRequired("Introduce el email")]
    )

    submit = SubmitField("Aceptar")


# ---------- CAMBIO DE CONTRASEÑA ----------
class formChangePassword(FlaskForm):
    password = PasswordField(
        "Nueva contraseña:",
        validators=[DataRequired("Introduce la nueva contraseña")]
    )

    submit = SubmitField("Cambiar contraseña")

class formCarrito(FlaskForm):
    id = HiddenField()
    cantidad = IntegerField(
        "Cantidad",
        default=1,
        validators=[
            NumberRange(min=1, message="Debe ser un número positivo"),
            DataRequired("Tienes que introducir el dato")
        ]
    )
    submit = SubmitField("Aceptar")
