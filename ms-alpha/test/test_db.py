import unittest, sys
from sqlalchemy import text

sys.path.append('..')
from app import create_app, db

class ConnectionTestCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app()  # Crea la aplicación Flask
        self.app_context = self.app.app_context()  # Crea un contexto para la aplicación
        self.app_context.push()  # Empuja el contexto de la aplicación a la pila
        db.create_all()  # Crea todas las tablas de la base de datos

    def tearDown(self):
        db.session.remove()  # Elimina la sesión actual de la base de datos
        db.drop_all()  # Elimina todas las tablas de la base de datos
        self.app_context.pop()  # Elimina el contexto de la aplicación de la pila

    # Test connection to database
    def test_db_connection(self):
        result = db.session.query(text("'Hello world'")).one()  # Ejecuta una consulta SQL
        self.assertEqual(result[0], 'Hello world')  # Verifica que el resultado sea 'Hello world'