import allure
from locators.switch_page_locators import SwitchPageLocators
from pages.base_page import BasePage


class SwitchPage(BasePage):
    @allure.step('Переходим на главную страницу')
    def switch_to_scooter_page(self):
        self.click_to_element(SwitchPageLocators.scooter_logo)

    @allure.step('Переходим на страницу Дзена')
    def switch_to_dzen_page(self):
        self.click_to_element(SwitchPageLocators.dzen_logo)
        self.switch_window()
        self.wait_for_url_contains("dzen.ru")

    @allure.step('Получаем текущий URL страницы')
    def get_url(self):
        return self.get_current_url()

    @allure.step('Получаем текст заголовка главной страницы')
    def get_scooter_headline_text(self):
        return self.get_text_from_element(SwitchPageLocators.title_main_page)