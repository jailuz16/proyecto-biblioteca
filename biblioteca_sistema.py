class BibliotecaSistema:
    def __init__(self, database, auth):
        self.database = database
        self.auth = auth

    def prestar_libro(self, usuario_id, libro_id):
        if not self.auth.verificar_usuario(usuario_id):
            return "Usuario no autorizado"
        if not self.database.libro_disponible(libro_id):
            return "Libro no disponible"
        self.database.registrar_prestamo(usuario_id, libro_id)
        return "Préstamo exitoso"
