
from selenium import webdriver
import unittest

class TestHolaMundo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_hola_mundo(self):
        self.driver.get("file:///ruta/a/tu/proyecto_hola_mundo/index.html")
        self.assertIn("Hola Mundo", self.driver.page_source)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
