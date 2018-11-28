import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page_object import BasePage

class PaymentReservationPage(BasePage):
    def __init__(self, driver, base_url='https://www.phptravels.net/'):
        self.base_url = base_url

        self.driver = driver
        self.timeout = 30

    locator_dictionary={
        "btn_pay_arrival": (By.CLASS_NAME, "arrivalpay"),
        "btn_pay_now":(By.XPATH, "//button[@data-target='#pay']")
    }