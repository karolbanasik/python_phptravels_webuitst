import time

from selenium.webdriver.common.by import By
from base_page_object import BasePage

class HomePage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            base_url='https://www.phptravels.net/')

    locator_dictionary = {
        "btn_tours": (By.XPATH, "//a[@title='Tours']/span"),
        "btn_searchbox": (By.ID, "s2id_autogen10"),
        "in_searchbox": (By.XPATH,"//div[@id='select2-drop']/div/input[@type='text']"),
        "btn_location_dubai": (By.XPATH, "//li[contains(@class, 'select2-result')]/div[contains(text(), 'Arab')]"
                                     "/span[contains(text(),'Dubai')]"),
        "btn_how_many_guests": (By.ID, "adults"),
        "opt_2guests": (By.XPATH, "//*[@id='adults']/option[@value=2]"),
        "btn_submit_search": (By.XPATH, "//div[@id='tours']//button[@type='submit']")

    }

    def search_tours(self, city= "Dubai", adult_no = 2):
        self.find_element(*self.locator_dictionary["btn_tours"]).click()
        time.sleep(1)
        self.find_element(*self.locator_dictionary["btn_searchbox"]).click()
        self.find_element(*self.locator_dictionary["in_searchbox"]).send_keys(city)
        time.sleep(1)
        self.find_element(*self.locator_dictionary["btn_location_dubai"]).click()
        #TODO: check if two adults are selected
        self.find_element(*self.locator_dictionary["btn_submit_search"]).click()