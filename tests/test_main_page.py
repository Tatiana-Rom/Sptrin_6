import allure
import pytest

from conftest import driver
from pages.main_page import MainPage
from pages.order_page import OrderPage
from data.faq_data import answer_for_question
from data.urls import MAIN


@allure.feature("Main Page")
class TestMainPage:

    @allure.title('Проверяем выпадающий список вопросы-ответы')
    @pytest.mark.parametrize("question_id, expected_answer", answer_for_question.items())
    def test_check_answer_for_question(self, driver, question_id, expected_answer):
        page = MainPage(driver)
        driver.get(MAIN)
        page.accept_cookie()
        assert expected_answer in page.check_answer_for_question(question_id)

    @allure.title('Проверяем работу верхней кнопки Заказать')
    def test_click_order_button_up(self, driver):
        page = MainPage(driver)
        driver.get(MAIN)
        page.accept_cookie()
        page.click_for_order_button_up()
        order_page = OrderPage(driver)
        assert order_page.is_order_page_opened()

    @allure.title('Проверяем работу нижней кнопки Заказать')
    def test_click_order_button_down(self, driver):
        page = MainPage(driver)
        driver.get(MAIN)
        page.accept_cookie()
        page.scroll_for_order_button_down()
        page.click_for_order_button_down()
        order_page = OrderPage(driver)
        assert order_page.is_order_page_opened()
