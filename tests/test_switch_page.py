import allure

from data.urls import MAIN
from pages.main_page import MainPage
from pages.switch_page import SwitchPage
from conftest import driver


class TestSwitchPage:
    @allure.title('Проверка перехода на главную страницу по клику на лого Самоката')
    def test_transition_from_order_page_to_main_page(self, driver,):
        switch_page = SwitchPage(driver)
        main_page = MainPage(driver)
        driver.get(MAIN)
        main_page.accept_cookie()
        main_page.click_for_order_button_up()
        switch_page.switch_to_scooter_page()
        assert 'Самокат' in switch_page.get_scooter_headline_text()

    @allure.title('Проверка перехода на Дзен по клику на лого Дзена')
    def test_transition_from_order_page_to_dzen(self, driver):
        switch_page = SwitchPage(driver)
        main_page = MainPage(driver)
        driver.get(MAIN)
        main_page.accept_cookie()
        switch_page.switch_to_dzen_page()
        assert "dzen.ru" in switch_page.get_url(), \
            f"Ожидался переход на Dzen, но текущий URL: {switch_page.get_url()}"

