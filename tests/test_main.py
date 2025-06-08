import unittest
from main import home
class TestBasico(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(2 + 2, 4)

class TestPrueba(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(home(), "Hola, esta es una app desplegada con Render y CI. aca voy camvbiennnndodoododododo")  