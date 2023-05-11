import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://qamindslab.com/"


class TestLandingPage:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)

    def test_open_courses(self):
        time.sleep(3)

        # Click courses
        courses_btn = self.driver.find_element(By.XPATH, "//a[@href='/courses']")
        assert courses_btn.is_displayed(), "Boton de cursos tiene que ser visible"
        assert courses_btn.is_enabled(), "Boton de cursos tiene que estar habilitado"
        courses_btn.click()

        # Validate course page
        time.sleep(3)
        assert self.driver.current_url == "https://qamindslab.com/courses", "URL tiene que ser la de cursos"
        courses_header = self.driver.find_element(By.XPATH, '//section[@id="cursos"]/h1')
        assert courses_header.is_displayed(), "Header de cursos tiene que ser visible"
        assert courses_header.text == "CURSOS", "El header tiene que tener el valor de Cursos"

    def teardown_method(self):
        self.driver.quit()