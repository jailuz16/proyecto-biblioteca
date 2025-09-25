class AuthStub:
    """Stub que simula autenticación."""

    def __init__(self, usuarios_validos=None):
        # si usuarios_validos es None, usamos la regla por defecto: id>0 es válido
        # si es un set/list, solo esos IDs están autorizados
        self.usuarios_validos = set(usuarios_validos) if usuarios_validos is not None else None

    def verificar_usuario(self, usuario_id):
        if self.usuarios_validos is None:
            return usuario_id > 0
        return usuario_id in self.usuarios_validos
