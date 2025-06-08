from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.headless = True

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get("https://www.google.com")


print(driver.title)
driver.quit()