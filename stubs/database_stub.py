class DatabaseStub:
    """Stub que simula base de datos simple para pruebas."""

    def __init__(self, disponibles=None):
        # si `disponibles` es None usamos la regla de paridad por defecto
        # si es un set/list, solo esos IDs se consideran disponibles
        self.disponibles = set(disponibles) if disponibles is not None else None
        self.prestamos = []

    def libro_disponible(self, libro_id):
        if self.disponibles is not None:
            return libro_id in self.disponibles
        # comportamiento por defecto: libros con ID par están disponibles
        return libro_id % 2 == 0

    def registrar_prestamo(self, usuario_id, libro_id):
        # registra el préstamo en la lista para verificaciones en tests
        self.prestamos.append((usuario_id, libro_id))
        return True
