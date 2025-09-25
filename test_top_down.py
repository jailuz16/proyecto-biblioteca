import pytest
from biblioteca_sistema import BibliotecaSistema
from stubs.database_stub import DatabaseStub
from stubs.auth_stub import AuthStub


def setup_sistema():
    """Configura el sistema con stubs para reutilizar en varias pruebas"""
    db_stub = DatabaseStub()
    auth_stub = AuthStub()
    return BibliotecaSistema(db_stub, auth_stub)


def test_prestamo_exitoso():
    """Caso: usuario válido y libro disponible"""
    sistema = setup_sistema()
    resultado = sistema.prestar_libro(usuario_id=1, libro_id=2)
    assert resultado == "Préstamo exitoso"


def test_usuario_no_autorizado():
    """Caso: usuario no válido"""
    sistema = setup_sistema()
    resultado = sistema.prestar_libro(usuario_id=0, libro_id=2)
    assert resultado == "Usuario no autorizado"


def test_libro_no_disponible():
    """Caso: usuario válido pero libro no disponible"""
    sistema = setup_sistema()
    resultado = sistema.prestar_libro(usuario_id=1, libro_id=3)
    assert resultado == "Libro no disponible"


def test_multiples_prestamos_exitosos():
    """Caso: un mismo usuario pide varios libros disponibles"""
    sistema = setup_sistema()
    resultados = [
        sistema.prestar_libro(usuario_id=2, libro_id=4),
        sistema.prestar_libro(usuario_id=2, libro_id=6),
    ]
    assert resultados == ["Préstamo exitoso", "Préstamo exitoso"]


def test_usuario_id_negativo():
    """Caso: usuario con ID negativo"""
    sistema = setup_sistema()
    resultado = sistema.prestar_libro(usuario_id=-5, libro_id=2)
    assert resultado == "Usuario no autorizado"


def test_libro_id_cero():
    """Caso: usuario válido pero libro con ID=0 (par, disponible según stub)"""
    sistema = setup_sistema()
    resultado = sistema.prestar_libro(usuario_id=1, libro_id=0)
    # Según la lógica del stub, 0 % 2 == 0 → disponible
    assert resultado == "Préstamo exitoso"
