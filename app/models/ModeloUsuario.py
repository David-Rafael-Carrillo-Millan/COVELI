from app.models.entities.Usuario import Usuario
from app.models.entities.TipoUsuario import TipoUsuario
class ModeloUsuario():
    
    @classmethod
    def login(self, db, usuario):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT id, usuario, password 
                FROM usuario WHERE usuario = '{0}'""".format(usuario.usuario)
            cursor.execute(sql)
            data = cursor.fetchone()
            if data != None:
                print(data)
                coincide = Usuario.verificar_password(data[2], usuario.password)
                print(data[2], usuario.password)
                if coincide:
                    usuario_logueado = Usuario(data[0], data[1], None, None)
                    return usuario_logueado
                else:
                    return None
            else:
                return None
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def obtener_por_id(self, db, id):
        try:
            cursor = db.connection.cursor()
            sql = """SELECT USU.id, USU.usuario, TIP.id, TIP.nombre 
                FROM usuario USU JOIN tipousuario TIP ON USU.tipousuario_id = TIP.id
                WHERE USU.id = {0}""".format(id)
            cursor.execute(sql)
            data = cursor.fetchone()
            tipousuario = TipoUsuario(data[2], data[3])
            usuario_logueado = Usuario(data[0], data[1], None, tipousuario)
            return usuario_logueado
        except Exception as ex:
            raise Exception(ex)

    @classmethod
    def registar_usuario(self, db, usuario):
        """"Crear usuario"""
        try:
            # id (NO SE ESPECIFICA)
            # usuario
            # password
            # tipousuario_id (DEBE SER = 2)
            user = usuario.usuario
            password = usuario.password
            tipousuario_id = usuario.tipousuario

            cursor = db.connection.cursor()
            sql = """INSERT INTO usuario (usuario, password, tipousuario_id)
                     VALUES ('{0}', '{1}' ,{2})""".format(user, password, tipousuario_id)
            cursor.execute(sql)
            db.connection.commit()

            print(user)
            print(password)
            print(tipousuario_id)

            return True
        except Exception as ex:
            raise Exception(ex)
            

    @classmethod
    def usuario_existe(self, db, usuario):
        """"Verificar si el usuario existe en la base de datos"""
        try:
            cursor = db.connection.cursor()
            sql = """SELECT usuario FROM usuario"""
            cursor.execute(sql)
            data = cursor.fetchall()
            lista_sin_comas = [elemento[0] for elemento in data]

            if usuario in lista_sin_comas:
                print(f'El usuario existe')
                return True
            else:
                return False
        except Exception as ex:
            raise Exception(ex)