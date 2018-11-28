import time

from selenium.webdriver.common.by import By
from base_page_object import BasePage

class TourSearchResultsPage(BasePage):

    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            base_url='https://www.phptravels.net/')

    locator_dictionary = {
        "btn_next_page":(By.XPATH, "//ul[contains(@class,'nav-pills')]//a[./i[contains(@class, 'fa-angle-right')]]"),
        "table_offers": (By.CLASS_NAME, "table-striped"),
        "btn_details_sheratonoffer": (By.XPATH,"//a[contains(@href,'/tours/united-arab-emirates/dubai/Sheraton-Trip')]"
                                               "//button[contains(@class,'btn-action loader')]")
    }
    def met_lookfor(self, city):
        locationstext =  self.find_element(*self.locator_dictionary["table_offers"]).text
        if city not in locationstext:
            self.find_element(*self.locator_dictionary["btn_next_page"]).click()
            time.sleep(1)
        locationstext = self.find_element(*self.locator_dictionary["table_offers"]).text
        assert city  in locationstext
        self.find_element(*self.locator_dictionary["btn_details_sheratonoffer"]).click()


