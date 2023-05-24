# proyecto_practico_intermedio/test_ejercicio_02
# Ejercicio 2
# En la barra de búsqueda. buscar la palabra "Display".
# se deberá mostrar un mensaje: no existen productos con la búsqueda.
# Luego, seleccionar la opción "Search in product descriptions"
# y volver a realizar la búsqueda.
# La nueva búsqueda deberá mostrar 4 resultados de los productos
# Apple Cinema 30", iPod Nano, iPod Touch, MacBook Pro

from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_search_display(self):
        # Escribir Display
        search_input = self.driver.find_element(By.NAME, "search")
        assert search_input.is_displayed() and search_input.is_enabled(), "El campo de búsqueda tiene que estar visible y habilitado"
        search_input.send_keys("Display")

        # Dar click en buscar
        search_btn = self.driver.find_element(By.XPATH, "//div[@id='search']//button")
        assert search_btn.is_displayed() and search_btn.is_enabled(), "El boton de búsqueda tiene que estar visible y habilitado"
        search_btn.click()

        # Verificar resultados
        display_msg = self.driver.find_element(By.XPATH, "//*[@id='content']//p[2]")
        assert display_msg.is_displayed(), "Debe de aparecer el msg: There is no product that matches the search criteria."

        # seleccionar la opción "Search in product descriptions" y darle click
        search_casilla = self.driver.find_element(By.XPATH, "//*[@id='description']")
        assert search_casilla.is_displayed() and search_casilla.is_enabled(), "La casilla de Search in product descriptions tiene que estar visible y habilitado"
        search_casilla.click()

        # Dar click en el botón azul Search
        search_blue_btn = self.driver.find_element(By.XPATH, "//*[@id='button-search']")
        assert search_blue_btn.is_displayed() and search_blue_btn.is_enabled(), "El boton de búsqueda tiene que estar visible y habilitado"
        search_blue_btn.click()

        # Verificar resultados, que se muestren los productos Apple Cinema 30", iPod Nano, iPod Touch, MacBook Pro
        celulares_img = self.driver.find_element(By.XPATH, "//img[@alt='Apple Cinema 30\"' and contains(@src, 'apple_cinema_30')]")
        #celulares_img = self.driver.find_element(By.XPATH, "//img[@alt='iPod Nano'] and //img[@alt='iPod Touch']")
        #celulares_img = self.driver.find_element(By.XPATH, "//*[@id={content{]/div[3]")
        assert celulares_img.is_displayed(), "La imagen de los celulares tiene que estar en el DOM"


    def teardown_method(self):
        self.driver.quit()
