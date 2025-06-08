import unittest
import home from main # type: ignore

class TestBasico(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(2 + 2, 4)

class TestPrueba(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(home.home(), "Hola, esta es una app desplegada con Render y CI")  