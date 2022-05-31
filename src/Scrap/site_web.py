from selenium.webdriver.common.by import By
from Scrap.web import Webdriver


class Site:
    LOGIN_LINK = (
        'http://politicanacional.simpress.com.br/RelatorioRevenda/Index'
    )
    input_revenda = (
        By.XPATH,
        '//input[@class="textBox text bloco ui-autocomplete-input"]',
    )
    input_dates = (By.XPATH, '//a[@class="chosen-single chosen-default"]')
    dates = (
        By.XPATH,
        '(//ul[@class="chosen-results"]//li[@class="active-result"])[1]',
    )
    pesquisar = (By.XPATH, '//input[@class="botao botaoSearch"]')
    baixar = (By.XPATH, '//input[@value="Baixar"]')

    def __init__(self) -> None:
        self.driver = Webdriver(download=True)

    def teste(self):
        self.driver.start()
        self.driver.open_page(
            'https://www.sarutaia.sp.gov.br/arquivos/a_pequena_sereia_(hans_christian_andersen)_01100246.pdf'
        )
        return self.driver.wait_download2()

    def open_page(self):
        self.driver.start()
        self.driver.open_page(self.LOGIN_LINK)

    def download(self):
        self.driver.click(self.baixar)

    def click_pesquisar(self):
        self.driver.click(self.pesquisar)

    def select_date(self):
        self.driver.click(self.input_dates)
        self.driver.click(self.dates)

    def fill_revenda(self, codigo):
        self.driver.fill(self.input_revenda, codigo)

    def pross(self, codigo):
        self.fill_revenda(codigo)
        self.select_date()
        self.click_pesquisar()
        if self.driver.exist(self.baixar):
            self.download()
            return self.driver.wait_download()
        return False

    def close(self):
        self.driver.close()
