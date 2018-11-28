import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page_object import BasePage

class ReservationConfirmationPage(BasePage):
    def __init__(self, driver, base_url='https://www.phptravels.net/'):
        self.base_url = base_url

        self.driver = driver
        self.timeout = 30

    locator_dictionary={
        "val_reserved": (By.XPATH, "//b[@class='wow flash animted animated animated']")
    }