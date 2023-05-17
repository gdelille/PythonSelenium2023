# Ejercicio # 01  04mayo2023
# 1. Ir a la página https://laboratorio.qaminds.com/
# 2. Escribir un script que:
#    a. Permita buscar un iphone desde la barra de búsqueda.
#    b. Verificar que devuelve un resultado con una imagen que pertenece a un iphone.

#import time
#from selenium import webdriver
#from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver, DriverType

#CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
#CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestBuscaElemento:

    def setup_method(self):
        #self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver = get_driver(DriverType.CHROME)
        #self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get(URL)

    def test_busqueda_iphone(self):
        #time.sleep(3)

        # buscar un iphone desde la barra de búsqueda
        elemento_busqueda = self.driver.find_element(By.NAME, "search")
        assert elemento_busqueda.is_displayed() and elemento_busqueda.is_enabled(), 'El campo de busqueda tiene que estar visible y habilitado'
        elemento_busqueda.send_keys('Iphone')

        # dar clic al boton de busqueda
        # time.sleep(3)
        boton_busqueda = self.driver.find_element(By.XPATH, '//div[@id="search"]//button')
        #assert boton_busqueda.is_displayed(), "Boton de busqueda tiene que ser visible"
        #assert boton_busqueda.is_enabled(), "Boton de busqueda tiene que estar habilitado"
        boton_busqueda.click()

        # validar la pagina de busqueda con la imagen
        #time.sleep(3)
        imagen_elemento = self.driver.find_element(By.XPATH, "//img[@alt='iPhone' and contains(@src, 'iphone')]")
        assert imagen_elemento.is_displayed(), "La imagen del elemento iphone tiene que estar en el DOM"

    def teardown_method(self):
        self.driver.quit()