from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

class BasePageElement():
    def __set__(self, obj, value):
        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element(By.XPATH, self.locator))
        driver.find_element(By.XPATH, self.locator).clear()
        driver.find_element(By.XPATH, self.locator).send_keys(value)