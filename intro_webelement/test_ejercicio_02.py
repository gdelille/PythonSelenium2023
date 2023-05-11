import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

CHROME_DRIVER_PATH = "./drivers/chromedriver.exe"
CHROME_SERVICE = Service(CHROME_DRIVER_PATH)
URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = webdriver.Chrome(service=CHROME_SERVICE)
        self.driver.maximize_window()
        self.driver.get(URL)


    def test_tablets(self):
        time.sleep(2)

        # Click Tablets
        tablets_btn = self.driver.find_element(By.XPATH, "//a[@href='https://laboratorio.qaminds.com/index.php?route=product/category&path=57']")
        assert tablets_btn.is_displayed(), "Boton de Tablets tiene que ser visible"
        assert tablets_btn.is_enabled(), "Boton de Tablets tiene que estar habilitado"
        tablets_btn.click()

       # Verificar resultados
        time.sleep(2)
        tablet_img = self.driver.find_element(By.XPATH, "//img[@alt='Samsung Galaxy Tab 10.1' and contains(@src, 'https://laboratorio.qaminds.com/image/cache/catalog/demo/samsung_tab_1-228x228.jpg')]")
        assert tablet_img.is_displayed(), "La imagen del Samsung Galaxy tiene que estar en el DOM"
        tablet_img.click()  #dar click al elemento

        # Validar en la nueva pagina los datos solicitados
        time.sleep(2)
        assert self.driver.current_url == "https://laboratorio.qaminds.com/index.php?route=product/product&path=57&product_id=49", "URL tiene que ser la de Samsung"
        precio = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/ul[2]/li[1]/h2')
        assert precio.text == "$241.99", "El precio mostrado en la pagina debe de tener el valor de $241.99"

        # agregarlo a la WishList

        wishList_boton = self.driver.find_element(By.XPATH, '//div[@class="btn-group"]//button[@class="btn btn-default"][1]')
        wishList_boton.click()
        #alerta = self.driver.find_element(By.XPATH, '//div[@class="alert alert-success alert-dismissible"]')
        #assert alerta.text == "You must login or create an account to save Samsung Galaxy Tab 10.1 to your wish list!", "El texto mostrado en la pagina debe corresponder con You must login or create an account to save Samsung Galaxy Tab 10.1 to your wish list! "

        # agregarlo al carrito
        time.sleep(2)
        carrito_boton = self.driver.find_element(By.XPATH, '//div[@id="cart"]//button')
        carrito_boton.click()
        alerta_carrito = self.driver.find_element(By.XPATH, '//div[@id="cart"]//li/p')
        assert alerta_carrito.text == "Your shopping cart is empty!", "El texto mostrado en la pagina debe corresponder con Your shopping cart is empty! "

    def teardown_method(self):
        self.driver.quit()