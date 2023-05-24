# Ejercicio 3
# Ir a la sección Desktop y seleccionar la opción Mac,
# verificar que se muestra un item con el título iMac.
# Abrir el producto y agregarlo al carrito,
# luego verificar que aparece en el botón del carrito la información:
# "1 item(s) - $122.00"


from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver
from selenium.webdriver.support.select import Select

URL = "https://laboratorio.qaminds.com/"


class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_mac(self):
        # Dar click en Desktop
        search_btn = self.driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[1]/a")
        assert search_btn.is_displayed() and search_btn.is_enabled(), "El boton de Desk tiene que estar visible y habilitado"
        search_btn.click()

        # Verificar resultados
        display_msg = self.driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[1]/div/div/ul/li[2]/a")
        assert display_msg.is_displayed(), "Debe aparecer Mac (1)"

        # seleccionar la opción "Mac (1)" y darle click
        selecciona_mac = self.driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[1]/div/div/ul/li[2]/a")
        assert selecciona_mac.is_displayed() and selecciona_mac.is_enabled(), "Mac (1) tiene que estar visible y habilitado"
        selecciona_mac.click()

        # Verificar resultados, verificar que se muestra un item con el título iMac
        iMac_img = self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div/div[2]/div[1]/h4/a")
        assert iMac_img.is_displayed(), "El título iMac tiene que estar en el DOM"

        # Abrir el producto con click
        iMac = self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div/div[1]/a/img")
        assert iMac.is_displayed() and iMac.is_enabled(), "iMac tiene que estar visible y habilitado para ser clickeable"
        iMac.click()

        # agregarlo al carrito de compras
        carrito_boton = self.driver.find_element(By.XPATH, "//*[@id='button-cart']")
        carrito_boton.click()
        alerta_carrito = self.driver.find_element(By.XPATH, "//*[@id='cart']/ul/li/p")
        assert alerta_carrito.text != "Your shopping cart is empty!", "El texto mostrado en la pagina debe corresponder con Your shopping cart is empty! "

    def teardown_method(self):
        self.driver.quit()
