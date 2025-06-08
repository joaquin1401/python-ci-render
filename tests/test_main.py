import unittest
import main

class TestBasico(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(2 + 2, 4)

class TestPrueba(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(main.home(), "Hola, esta es una app desplegada con Render y CI")  