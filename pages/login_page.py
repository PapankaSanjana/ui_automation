from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage


class LoginPage(BasePage):

    ADMIN_BTN = (By.XPATH, "//*[contains(text(),'Admin')]")
    USER_BTN = (By.XPATH, "//*[contains(text(),'User')]")

    def login_as_admin(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.ADMIN_BTN)
        ).click()

    def login_as_user(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.USER_BTN)
        ).click()

    def enter_credentials(self, email, password):
        pass

    def click_login(self):
        pass

    def is_login_page(self):
        return "login" in self.driver.current_url