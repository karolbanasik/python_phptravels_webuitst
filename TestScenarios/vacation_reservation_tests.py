import pytest
from datetime import date

from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.usefixtures("driver_get")
class TestReservation:


    @pytest.mark.parametrize("family_size", [3])
    def test_family_tour_Dubai(self, family_size):
        city = "Dubai"
        trip_date = date.today()
        trip_date = date(trip_date.year+1, trip_date.month, trip_date.day)
        adult_no = 2

        from PageObjects.home_page import HomePage
        page = HomePage(self.driver)
        page.visit(url="https://www.phptravels.net/")
        page.search_tours(city, adult_no)

        from PageObjects.tour_search_results import TourSearchResultsPage
        page = TourSearchResultsPage(self.driver)
        page.met_lookfor(city)

        from PageObjects.tour_details_page import TourDetailsPage
        page=TourDetailsPage(self.driver)
        page.met_change_date(trip_date)
        price = page.met_select_travelers(adult_no, children_no=family_size-adult_no, infant_no=0)
        page.btn_book_now.click()

        from PageObjects.booking_sumary_page import BookingSummary
        page=BookingSummary(self.driver)
        page.met_fill_form()
        page.btn_confirm_booking.click()

        from PageObjects.payment_reservation_page import PaymentReservationPage
        page = PaymentReservationPage(self.driver)
        WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located((By.CLASS_NAME, "arrivalpay")))
        page.btn_pay_arrival.click()
        Alert(self.driver).accept()

        from PageObjects.reservation_confirmation_page import ReservationConfirmationPage
        page = ReservationConfirmationPage(self.driver)
        reserved = page.val_reserved.text
        assert reserved == "RESERVED"

