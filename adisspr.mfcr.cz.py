# selenium 4
from selenium import webdriver
import time
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.select import Select
from webdriver_manager.firefox import GeckoDriverManager

URL = 'https://adisspr.mfcr.cz/dpr/DphReg?ZPRAC=FDPHI1&poc_dic=2&OK=Zobraz'
DOWNLOAD_DIR = '/tmp/download'

profile = webdriver.FirefoxProfile()
profile.set_preference("browser.download.folderList", 2)
profile.set_preference("browser.download.manager.showWhenStarting", False)
profile.set_preference("browser.download.dir", DOWNLOAD_DIR)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/comma-separated-values type")
options = webdriver.FirefoxOptions()
#### firefox without a GUI ####
options.add_argument('--headless')
browser = webdriver.Firefox(options=options, firefox_profile=profile,service=Service(GeckoDriverManager().install()))

browser.get(URL)
time.sleep(2)
select = Select(browser.find_element_by_name("form:nespolehlivost"))
select.select_by_visible_text("nespolehlivá osoba")
assert "nespolehlivá osoba" in select.first_selected_option.text
button = browser.find_element_by_name('form:hledej')
button.click()
time.sleep(2)
button = browser.find_element_by_name('actionButtons:_idJsp53')

#### download file ####
button.click()
