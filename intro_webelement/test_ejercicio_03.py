import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/index.php?route=account/login"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)


    def test_login_invalido(self):
        time.sleep(2)

        # buscar un iphone desde la barra de búsqueda
        elemento_busqueda = self.driver.find_element(By.NAME, "search")
        assert elemento_busqueda.is_displayed() and elemento_busqueda.is_enabled(), 'El campo de busqueda tiene que estar visible y habilitado'
        elemento_busqueda.send_keys('Iphone')

        # escribir correo electronico
        elemento_busqueda = self.driver.find_element(By.ID, "input-email")
        assert elemento_busqueda.is_displayed() and elemento_busqueda.is_enabled(), 'El campo de busqueda tiene que estar visible y habilitado'
        elemento_busqueda.send_keys('georgette@gmail.com')
        elemento_busqueda.click()
        time.sleep(2)

        # escribir password
        elemento_busqueda = self.driver.find_element(By.ID, "input-password")
        assert elemento_busqueda.is_displayed() and elemento_busqueda.is_enabled(), 'El campo de busqueda tiene que estar visible y habilitado'
        elemento_busqueda.send_keys('asdfg')
        elemento_busqueda.click()

        # dar click al boton
        

    def teardown_method(self):
        self.driver.quit()