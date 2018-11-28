import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page_object import BasePage

class BookingSummary(BasePage):
    def __init__(self, driver, base_url='https://www.phptravels.net/'):
        self.base_url = base_url

        self.driver = driver
        self.timeout = 30

    locator_dictionary={
        "in_first_name": (By.NAME, "firstname"),
        "in_last_name": (By.NAME, "lastname"),
        "in_email": (By.NAME, "email"),
        "in_email_repeat": (By.NAME, "confirmemail"),
        "in_phone": (By.NAME, "phone"),
        "in_address": (By.NAME, "address"),
        "btn_select_country": (By.CLASS_NAME, "select2-chosen"),
        "in_select_country": (By.CLASS_NAME, "select2-input"),
        "in_traveler1_name": (By.NAME, "passport[1][name]"),
        "in_traveler1_passport": (By.NAME, ("passport[1][passportnumber]")),
        "in_traveler1_age": (By.NAME, ("passport[1][age]")),
        "in_traveler2_name": (By.NAME, "passport[2][name]"),
        "in_traveler2_passport": (By.NAME,("passport[2][passportnumber]")),
        "in_traveler2_age": (By.NAME, ("passport[2][age]")),
        "in_traveler3_name": (By.NAME, "passport[3][name]"),
        "in_traveler3_passport": (By.NAME,("passport[3][passportnumber]")),
        "in_traveler3_age": (By.NAME, ("passport[3][age]")),
        "val_subtotal": (By.XPATH, ("//tr[./td//strong[contains(text(),'Subtotal')]]/td[@class='text-right']")),
        "btn_confirm_booking":(By.NAME, ("guest"))
    }
    def met_fill_form(self):
        self.find_element(*self.locator_dictionary["in_first_name"]).send_keys("Tester")
        self.find_element(*self.locator_dictionary["in_last_name"]).send_keys("Zbigniew")
        self.find_element(*self.locator_dictionary["in_email"]).send_keys("test@example.com")
        self.find_element(*self.locator_dictionary["in_email_repeat"]).send_keys("test@example.com")
        self.find_element(*self.locator_dictionary["in_phone"]).send_keys("838383838")
        self.find_element(*self.locator_dictionary["in_address"]).send_keys("TestStr 99, TestTown")
        self.find_element(*self.locator_dictionary["btn_select_country"]).click()
        self.find_element(*self.locator_dictionary["in_select_country"]).send_keys("Poland"+Keys.RETURN)
        self.find_element(*self.locator_dictionary["in_traveler1_name"]).send_keys("Tester Zbigniew")
        self.find_element(*self.locator_dictionary["in_traveler1_passport"]).send_keys("P455NUM1")
        self.find_element(*self.locator_dictionary["in_traveler1_age"]).send_keys(55)
        self.find_element(*self.locator_dictionary["in_traveler2_name"]).send_keys("Testerka Zbigniew")
        self.find_element(*self.locator_dictionary["in_traveler2_passport"]).send_keys("P455NUM2")
        self.find_element(*self.locator_dictionary["in_traveler2_age"]).send_keys(50)
        self.find_element(*self.locator_dictionary["in_traveler3_name"]).send_keys("Testerek Zbigniew")
        self.find_element(*self.locator_dictionary["in_traveler3_passport"]).send_keys("P455NUM3")
        self.find_element(*self.locator_dictionary["in_traveler3_age"]).send_keys(10)
