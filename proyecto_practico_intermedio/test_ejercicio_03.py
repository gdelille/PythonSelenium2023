# Ejercicio 3
# Ir a la sección Desktop y seleccionar la opción Mac,
# verificar que se muestra un item con el título iMac.
# Abrir el producto y agregarlo al carrito,
# luego verificar que aparece en el botón del carrito la información: "1 item(s) - $122.00".


from selenium.webdriver.common.by import By
from factory.webdriver_factory import get_driver
URL = "https://laboratorio.qaminds.com/"

class TestLaboratorioQAMinds:

    def setup_method(self):
        self.driver = get_driver()
        self.driver.get(URL)

    def test_mac(self):

        # Dar click en Desktop
        search_desk = self.driver.find_element(By.XPATH, '//a[text()="Desktops"]')
        assert search_desk.is_displayed() and search_desk.is_enabled(), "El boton de Desk tiene que estar visible y habilitado"
        search_desk.click()

        # Verificar resultados
        display_msg = self.driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[1]/div/div/ul/li[2]/a")
        assert display_msg.is_displayed(), "Debe aparecer Mac (1)"

        # seleccionar la opción "Mac (1)" y darle click
        selecciona_mac = self.driver.find_element(By.XPATH, "//*[@id='menu']/div[2]/ul/li[1]/div/div/ul/li[2]/a")
        assert selecciona_mac.is_displayed() and selecciona_mac.is_enabled(), "Mac (1) tiene que estar visible y habilitado"
        selecciona_mac.click()

        # Verificar resultados, verificar que se muestra un item con el título iMac
        iMac_img = self.driver.find_element(By.XPATH, "//a[text()='iMac']")
        assert iMac_img.is_displayed() and iMac_img.is_enabled(), "El título iMac tiene que estar en el DOM"

        # Abrir el producto con click
        iMac = self.driver.find_element(By.XPATH, "//*[@id='content']/div[2]/div/div/div[1]/a/img")
        assert iMac.is_displayed() and iMac.is_enabled(), "iMac tiene que estar visible y habilitado para ser clickeable"
        iMac.click()

        # agregarlo al carrito de compras
        cuadro_cantidad = self.driver.find_element(By.ID, "input-quantity")
        assert cuadro_cantidad.is_displayed() and cuadro_cantidad.is_enabled(), "verificar que est[e disponible y visible el recuadro para escribir la cantidad"
        cuadro_cantidad.clear()
        cuadro_cantidad.send_keys("1")
        cuadro_cantidad.click()
        #assert cuadro_cantidad.text == "1", "debe contener el valor de 1"

        carrito_boton = self.driver.find_element(By.XPATH, "//*[@id='button-cart']")
        assert carrito_boton.is_displayed() and carrito_boton.is_enabled(), "el boton Add to cart del carrito debe estar disponible y visible"
        carrito_boton.click()
        total = self.driver.find_element(By.ID, "cart-total")
        assert total.is_displayed() and total.is_enabled(), "el boton negro del carrito debe estar disponible y visible"
        #assert "0 item(s) - $0.00" in total.text, "Se espera que el el boton negro contenga info diferente de 0"

        # verificar que aparece en el botón del carrito la información: "1 item(s) - $122.00"
        assert total.text == "1 item(s) - $122.00", "Se espera que el boton negro del carrito contenga 1 item(s) - $122.00"

    def teardown_method(self):
        self.driver.quit()
