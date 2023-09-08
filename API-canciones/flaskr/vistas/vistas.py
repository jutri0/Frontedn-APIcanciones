from flask_restful import Resource
from ..modelos import db, Cancion, Album, Usuario, CancionSchema, AlbumSchema, UsuarioSchema
from flask import request

usuario_schema = UsuarioSchema()
cancion_schema = CancionSchema()
album_schema = AlbumSchema()

#Canciones

class VistaCanciones(Resource):
    def get(self):#me trae todas las canciones
        return [cancion_schema.dump(Cancion) for Cancion in Cancion.query.all()]

    def post(self):
        nueva_cancion = Cancion(titulo=request.json['titulo'],\
                                minutos=request.json['minutos'],\
                                segundos=request.json['segundos'],\
                                interprete=request.json['interprete'])
        db.session.add(nueva_cancion)#agregar en la DB
        db.session.commit()#guardar los cambios
        return cancion_schema.dump(nueva_cancion)#retorna la nueva cacion en formato json

class VistaCancion(Resource):
    def get(self, id_cancion):
        return cancion_schema.dump(Cancion.query.get_or_404(id_cancion))

    #Actualizar
    def put(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        cancion.titulo = request.json.get('titulo', cancion.titulo)
        cancion.minutos = request.json.get('minutos', cancion.minutos)
        cancion.segundos = request.json.get('segundos', cancion.segundos)
        cancion.interprete = request.json.get('interprete', cancion.interprete)
        db.session.commit()
        return cancion_schema(cancion)

    #Eliminacion
    def delete(self, id_cancion):
        cancion = Cancion.query.get_or_404(id_cancion)
        db.session.delete(cancion)
        db.session.commit()
        return 'operacion existosa', 204

# Albumes

class VistaAlbumes(Resource):
    def get(self):#me trae todos los albumes
        return [album_schema.dump(Album) for Album in Album.query.all()]

    def post(self):
        nuevo_album = Album(titulo=request.json['titulo'],\
                            anio=request.json['anio'],\
                            descripcion=request.json['descripcion'],\
                            medio=request.json['medio'])
        db.session.add(nuevo_album)#agregar en la DB
        db.session.commit()#guardar los cambios
        return album_schema.dump(nuevo_album)#retorna el nuevo album en formato json

class VistaAlbum(Resource):
    def get(self, id_album):
        return album_schema.dump(Album.query.get_or_404(id_album))

    #Actualizar
    def put(self, id_album):
        album = Album.query.get_or_404(id_album)
        album.titulo = request.json.get('titulo', album.titulo)
        album.anio = request.json.get('anio', album.anio)
        album.descripcion = request.json.get('descripcion', album.descripcion)
        album.medio = request.json.get('medio', album.medio)
        db.session.commit()
        return album_schema(album)

    #Eliminacion
    def delete(self, id_album):
        album = Album.query.get_or_404(id_album)
        db.session.delete(album)
        db.session.commit()
        return 'Operacion Existosa', 204

# Usuarios

class VistaUsuarios(Resource):
    def get(self):  # me trae todos los Usuarios
        return [usuario_schema.dump(Usuario) for Usuario in Usuario.query.all()]

    def post(self):
        nuevo_usuario = Usuario(nombre_usuario=request.json['nombre_usuario'], \
                                contrasena=request.json['contrasena'])
        db.session.add(nuevo_usuario)  # agregar en la DB
        db.session.commit()  # guardar los cambios
        return usuario_schema.dump(nuevo_usuario)  # retorna el nuevo usuario en formato json

class VistaUsuario(Resource):
    def get(self, id_usuario):
        return usuario_schema.dump(Usuario.query.get_or_404(id_usuario))

    # Actualizar
    def put(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        Usuario.nombre_usuario = request.json.get('nombre_usuario', usuario.nombre_usuario)
        usuario.contrasena = request.json.get('contrasena', usuario.contrasena)
        db.session.commit()
        return usuario_schema(usuario)

    # Eliminacion
    def delete(self, id_usuario):
        usuario = Usuario.query.get_or_404(id_usuario)
        db.session.delete(usuario)
        db.session.commit()
        return 'Operacion Existosa', 204