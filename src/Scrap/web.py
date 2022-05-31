from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.remote.remote_connection import LOGGER
from selenium.webdriver.remote.remote_connection import logging as logging_web
from webdriver_manager.chrome import ChromeDriverManager
from pathlib import Path
import time
import os
import logging


LOGGER.setLevel(logging.WARNING)


class Webdriver:
    def __init__(
        self,
        profiles=False,
        headless=False,
        download=False,
        undetected=False,
        kwargs={},
    ):

        if undetected:
            import undetected_chromedriver as UChrome

            UChrome.TARGET_VERSION = 96
            UChrome.install(ChromeDriverManager().install())
            self.options = UChrome.ChromeOptions()

        else:
            self.options = webdriver.ChromeOptions()

        if headless:
            self.options.add_argument('--headless')
        else:
            self.options.add_argument('--start-maximized')

        if download:
            self.download()

        self.options.add_experimental_option(
            'excludeSwitches', ['enable-logging']
        )
        self.kwargs = kwargs

        if profiles:
            dir_path = os.getcwd()
            profile = os.path.join(dir_path, 'profile', 'wpp')
            self.options.add_argument(f'--user-data-dir={profile}')

    def download(self):
        self.download_path = os.path.abspath(os.getcwd()) + '/download'
        config_print = """{"recentDestinations": [{"id": "Save as PDF", "origin": "local", "account": ""}], 
                    "selectedDestinationId": "Save as PDF",
                    "version": 2}"""

        self.options.add_experimental_option(
            'prefs',
            {
                'download.default_directory': self.download_path,
                'download.prompt_for_download': False,  # To auto download the file
                'download.directory_upgrade': True,
                # It will not show PDF directly in chrome
                'plugins.always_open_pdf_externally': True,
                'printing.print_preview_sticky_settings.appState': config_print,
            },
        )

    def start(self):
        self.driver = webdriver.Chrome(
            ChromeDriverManager(log_level=logging_web.ERROR).install(),
            options=self.options,
            **self.kwargs,
        )
        self.wait = WebDriverWait(self.driver, 10)

    def open_page(self, url):
        self.driver.get(url)

    def find_element(self, locator, elem=None):
        by, locator = locator
        if elem:
            return elem.find_element(by, locator)
        return self.driver.find_element(by, locator)

    def find_elements(self, locator, elem=None):
        by, locator = locator
        if elem:
            return elem.find_elements(by, locator)
        return self.driver.find_elements(by, locator)

    def move_element(self, elem, y=-100):
        if isinstance(elem, tuple):
            elem = self.find_element(elem)

        loc = elem.location_once_scrolled_into_view
        self.driver.execute_script(f"window.scrollBy({loc['x']},{y})")

    def click(self, locator, hover_to=False):
        elem = locator
        if isinstance(locator, tuple):
            elem = EC.element_to_be_clickable(locator)
            elem = self.exist(locator, wait=3, retur=True)
        if hover_to:
            self.move_element(elem)
        elem.click()

    def exist(self, element, wait=10, retur=False):
        try:
            element = WebDriverWait(self.driver, wait).until(
                EC.presence_of_element_located(element)
            )
            if retur:
                return element
            return True
        except:
            return False

    def fill(self, element, text):
        if isinstance(element, tuple):
            elem = EC.element_to_be_clickable(element)
            elem = self.wait.until(elem)

        self.move_element(elem)
        elem.click()
        elem.clear()
        elem.send_keys(text)

    def get_element_attribute(self, locator, attribute):
        elem = locator
        if isinstance(locator, tuple):
            elem = EC.presence_of_element_located(locator)
            elem = self.wait.until(elem)
        attribute = elem.get_attribute(attribute)
        return attribute

    def send_key(self, key, element=None):
        if element:
            return self.driver.find_element(element[0], element[1]).send_keys(
                key
            )
        return ActionChains(self.driver).send_keys(key).perform()

    def refresh(self):
        self.driver.refresh()

    def switch_to_frame(self, frame='root_frame'):
        if frame == 'root_frame':
            self.driver.switch_to_window(self.driver.window_handles[0])
        else:
            self.driver.switch_to.frame(frame)

    def wait_download1(self):
        file = os.listdir(self.download_path)[0]
        if '.tmp' not in file:
            if '.crdownload' not in file:
                time.sleep(1)
                return file
        return False

    def wait_download2(self):
        time.sleep(2)
        while True:
            file = sorted(
                Path(self.download_path).iterdir(), key=os.path.getmtime
            )[-1].name
            if '.tmp' not in file and '.crdownload' not in file:
                file = sorted(
                    Path(self.download_path).iterdir(), key=os.path.getmtime
                )[-1].name
                if '.tmp' not in file and '.crdownload' not in file:
                    return sorted(
                        Path(self.download_path).iterdir(),
                        key=os.path.getmtime,
                    )[-1].name
            time.sleep(1)

    def zoom(self, zoom):
        self.driver.execute_script(f"document.body.style.zoom='{zoom}'")

    def screenshot(self, file, zoom='100%'):
        self.zoom(zoom)
        self.driver.save_screenshot(file)
        self.zoom('100%')

    def close(self):
        self.driver.quit()
