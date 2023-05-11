# ejemplo del maestro

# Ir a la pagina https://demoqa.com/select-menu
# Escribir un script que
# a. Seleccione de la primera lista Old Style Select Menu la opcion "green"
# b. verifique que la opcion ha sido seleccionada

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

    def test_old_style_select(self):
        time.sleep(2)
        element = self.driver.find_element(By.ID, "oldSelectMenu")
        select = Select(element)
        select.select_by_visible_text("Green")
        select.select_by_value("4")
        assert select.first_selected_option.text == "Purple"
        time.sleep(2)

    def teardown_method(self):
        self.driver.quit()
