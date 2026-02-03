import os
from flask import Flask, render_template, redirect, url_for, request, abort, session
from werkzeug.utils import secure_filename
from aplicacion.forms import (
    formArticulo,
    formCategoria,
    formSINO,
    LoginForm,
    formUsuario,
    formChangePassword
)
from aplicacion import config
from aplicacion.models import db, Categoria, Articulo, Usuario
from aplicacion.login import login_user, logout_user

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)

@app.route("/")
@app.route("/categoria/<int:id>")
def inicio(id=0):
    categoria = None

    if id == 0:
        articulos = Articulo.query.all()
    else:
        categoria = Categoria.query.get(id)
        articulos = Articulo.query.filter_by(categoria_id=id).all()

    categorias = Categoria.query.all()
    return render_template(
        "inicio.html",
        articulos=articulos,
        categorias=categorias,
        categoria=categoria
    )

@app.route("/categorias")
def categorias():
    categorias = Categoria.query.all()
    return render_template("categorias.html", categorias=categorias)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error="Página no encontrada"), 404

@app.route("/articulos/new", methods=["GET", "POST"])
def articulos_new():
    form = formArticulo()

    # Cargar categorías para el SelectField
    categorias = [(c.id, c.nombre) for c in Categoria.query.all()]
    form.categoriaId.choices = categorias

    if form.validate_on_submit():
        try:
            f = form.photo.data
            nombre_fichero = secure_filename(f.filename)
            f.save(app.root_path + "/static/img/" + nombre_fichero)
        except:
            nombre_fichero = ""

        art = Articulo()
        form.populate_obj(art)
        art.categoria_id = form.categoriaId.data 
        art.imagen = nombre_fichero

        db.session.add(art)
        db.session.commit()

        return redirect(url_for("inicio"))

    return render_template("articulos_new.html", form=form)

@app.route("/articulos/edit/<int:id>", methods=["GET", "POST"])
def articulos_edit(id):
    art = Articulo.query.get(id)
    if not art:
        abort(404)

    form = formArticulo(obj=art)

    categorias = [(c.id, c.nombre) for c in Categoria.query.all()]
    form.categoriaId.choices = categorias

    if form.validate_on_submit():
        if form.photo.data:
            try:
                if art.imagen:
                    os.remove(app.root_path + "/static/img/" + art.imagen)
                f = form.photo.data
                nombre_fichero = secure_filename(f.filename)
                f.save(app.root_path + "/static/img/" + nombre_fichero)
            except:
                nombre_fichero = art.imagen
        else:
            nombre_fichero = art.imagen

        form.populate_obj(art)
        art.categoria_id = form.categoriaId.data
        art.imagen = nombre_fichero

        db.session.commit()
        return redirect(url_for("inicio"))

    return render_template("articulos_new.html", form=form)


@app.route("/categorias/new", methods=["GET", "POST"])
def categorias_new():
    form = formCategoria()

    if form.validate_on_submit():
        cat = Categoria(nombre=form.nombre.data)
        db.session.add(cat)
        db.session.commit()
        return redirect(url_for("categorias"))

    return render_template("categorias_new.html", form=form)

@app.route("/categorias/edit/<int:id>", methods=["GET", "POST"])
def categorias_edit(id):
    cat = Categoria.query.get(id)
    if cat is None:
        abort(404)

    form = formCategoria(obj=cat)

    if form.validate_on_submit():
        form.populate_obj(cat)
        db.session.commit()
        return redirect(url_for("categorias"))

    return render_template("categorias_new.html", form=form)

@app.route("/categorias/delete/<int:id>", methods=["GET", "POST"])
def categorias_delete(id):
    cat = Categoria.query.get(id)
    if cat is None:
        abort(404)

    form = formSINO()

    if form.validate_on_submit():
        if form.si.data:
            db.session.delete(cat)
            db.session.commit()
        return redirect(url_for("categorias"))

    return render_template("categorias_delete.html", form=form, cat=cat)



@app.route("/articulos/delete/<int:id>", methods=["GET", "POST"])
def articulos_delete(id):
    art = Articulo.query.get(id)
    if art is None:
        abort(404)

    form = formSINO()

    if form.validate_on_submit():
        if form.si.data:
            if art.imagen:
                try:
                    os.remove(app.root_path + "/static/img/" + art.imagen)
                except:
                    pass

            db.session.delete(art)
            db.session.commit()

        return redirect(url_for("inicio"))

    return render_template("articulos_delete.html", form=form, art=art)

@app.route("/login", methods=["GET", "POST"])
def login():
    # Si ya está logueado, fuera
    if session.get("id"):
        return redirect(url_for("inicio"))

    form = LoginForm()

    if form.validate_on_submit():
        user = Usuario.query.filter_by(username=form.username.data).first()

        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for("inicio"))
        else:
            form.password.errors.append("Usuario o contraseña incorrectos")

    return render_template("login.html", form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("inicio"))




@app.route("/registro", methods=["GET", "POST"])
def registro():
    form = formUsuario()

    if form.validate_on_submit():
        existe_usuario = Usuario.query.filter_by(
            username=form.username.data
        ).first()

        if existe_usuario is None:
            user = Usuario()
            form.populate_obj(user)
            user.admin = False
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("inicio"))

        form.username.errors.append("Nombre de usuario ya existe.")

    return render_template("usuarios_new.html", form=form, perfil=False)


@app.route("/perfil/<username>", methods=["GET", "POST"])
def perfil(username):
    user = Usuario.query.filter_by(username=username).first()
    if user is None:
        abort(404)

    form = formUsuario(obj=user)
    del form.password  # 🔑 no permitimos cambiar password aquí

    if form.validate_on_submit():
        form.populate_obj(user)
        db.session.commit()
        return redirect(url_for("inicio"))

    return render_template(
        "usuarios_new.html",
        form=form,
        perfil=True
    )


@app.route("/changepassword/<username>", methods=["GET", "POST"])
def changepassword(username):
    user = Usuario.query.filter_by(username=username).first()
    if user is None:
        abort(404)

    form = formChangePassword()

    if form.validate_on_submit():
        user.password = form.password.data
        db.session.commit()
        return redirect(url_for("inicio"))

    return render_template(
        "changepassword.html",
        form=form
    )
