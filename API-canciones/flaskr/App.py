from flaskr import create_app
from flask import render_template, request, redirect
from .modelos import db, Cancion, Usuario, Album, Medios, AlbumSchema
from flask_restful import Api, Resource
from .vistas import VistaCanciones, VistaCancion, VistaAlbumes, VistaAlbum, VistaUsuarios, VistaUsuario

app = create_app('default')
app_context = app.app_context()
app_context.push()

db.init_app(app)
db.create_all()

@app.route('/')
def menu():
    return render_template('menu/menu.html')

@app.route('/canciones')
def listar_canciones():
    canciones = Cancion.query.all()
    return render_template('canciones/listar_canciones.html', canciones=canciones)

@app.route('/canciones/agregar', methods=['GET', 'POST'])
def agregar_cancion():
    if request.method == 'POST':
        titulo = request.form['titulo']
        minutos = request.form['minutos']
        segundos = request.form['segundos']
        interprete = request.form['interprete']

        nueva_cancion = Cancion(titulo=titulo, minutos=minutos, segundos=segundos, interprete=interprete)
        db.session.add(nueva_cancion)
        db.session.commit()

        return redirect('/canciones')

    return render_template('canciones/agregar_cancion.html')

@app.route('/usuarios')
def listar_usuarios():
    usuarios = Usuario.query.all()
    albumes = Album.query.all()
    return render_template('usuarios/listar_usuarios.html', albumes=albumes, usuarios=usuarios)

@app.route('/albumes')
def listar_albumes():
    albumes = Album.query.all()
    canciones = Cancion.query.all()
    return render_template('albumes/listar_albumes.html', albumes=albumes, canciones=canciones)

api = Api(app)
api.add_resource(VistaCanciones, '/canciones')
api.add_resource(VistaCancion, '/canciones/<int:id_cancion>')
api.add_resource(VistaAlbumes, '/albumes')
api.add_resource(VistaAlbum, '/albumes/<int:id_album>')
api.add_resource(VistaUsuarios, '/usuarios')
api.add_resource(VistaUsuario, '/usuarios/<int:id_usuario>')

with app.app_context():
    u = Usuario(nombre_usuario='Isaura', contrasena='A.54@z')
    al = Album(titulo='adsadsad', anio=1973, descripcion='clasico', medio=Medios.DISCO)
    c = Cancion(titulo='fdfdfdsfdsf', minutos=6, segundos=25, interprete='Spinetta')
    u.albumes.append(al)
    al.canciones.append(c)
    db.session.add(u)
    db.session.add(c)
    db.session.commit()
    print(Usuario.query.all())
    print([AlbumSchema().dumps(Album) for Album in Album.query.all()])
    print(Album.query.all())
    print(Usuario.query.all()[0].albumes)
    print(Cancion.query.all())
    db.session.delete(al)
