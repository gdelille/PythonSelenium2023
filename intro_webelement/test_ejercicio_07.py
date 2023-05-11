# ejercicio para practicar

# Ir a la pagina https://demoqa.com/select-menu
# Escribir un script que:
# a. Seleccione de la primera lista Standard Multi Select las opciones "Volvo" y "Audi".
# b. verifique que la opcion ha sido seleccionada.

import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = " https://demoqa.com/select-menu"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_standard_multi_select(self):
        time.sleep(1)
        element = self.driver.find_element(By.ID, "cars")
        select = Select(element)
        select.select_by_value("volvo")
        assert select.first_selected_option.text == "Volvo"
        time.sleep(5)

        select.select_by_value("audi")
        assert select.second_selected_option.text == "Audi"
        time.sleep(5)


    def teardown_method(self):
        self.driver.quit()
