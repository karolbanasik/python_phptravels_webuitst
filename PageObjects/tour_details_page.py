import time

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from base_page_object import *

class TourDetailsPage(BasePage):
    def __init__(self, driver):
        BasePage.__init__(
            self,
            driver,
            base_url='https://www.phptravels.net/')

    locator_dictionary={
        "in_selectdate":(By.CLASS_NAME, "tchkin"),
        "btn_change_date":(By.XPATH, "//button[contains(text(),'Change Date')]"),
        "btn_select_AdultsNo": (By.ID, "selectedAdults"),
        "btn_select_ChildrenNo": (By.ID, "selectedChild"),
        "btn_select_InfantsNo": (By.ID, "selectedInfants"),
        "val_total_cost": (By.CLASS_NAME, "totalCost"),
        "btn_book_now": (By.XPATH, "//button[contains(text(),'Book Now')]")
    }

    def met_change_date(self, date):
        str_date = date.strftime("%d/%m/%y")
        self.find_element(*self.locator_dictionary["in_selectdate"]).clear()
        self.find_element(*self.locator_dictionary["in_selectdate"]).send_keys(str_date+Keys.RETURN)

        time.sleep(1)
        date_value = self.find_element(*self.locator_dictionary["in_selectdate"]).get_property("value")
        assert date_value == str_date, "value is %(date_value)s while it should be %(str_date)s"%locals()

    def met_select_travelers(self, adult_no, children_no, infant_no):
        self.find_element(*self.locator_dictionary["btn_select_AdultsNo"]).send_keys(adult_no)
        self.find_element(*self.locator_dictionary["btn_select_ChildrenNo"]).send_keys(children_no)
        self.find_element(*self.locator_dictionary["btn_select_InfantsNo"]).send_keys(infant_no)
        total_cost = self.find_element(*self.locator_dictionary["val_total_cost"]).text
        total_cost = total_cost.split("$")[1]
        return total_cost

