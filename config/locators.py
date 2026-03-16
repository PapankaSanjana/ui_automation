from selenium.webdriver.common.by import By


class LoginLocators:

    USERNAME = (By.NAME, "username")
    PASSWORD = (By.NAME, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[@type='submit']")


class DashboardLocators:

    TITLE = (By.XPATH, "//h6[contains(text(),'Dashboard')]")


class ProjectLocators:

    CREATE_BTN = (By.ID, "create-project")


class TaskLocators:

    STATUS = (By.CLASS_NAME, "task-status")