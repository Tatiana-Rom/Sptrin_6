import allure
import pytest

from conftest import driver
from data.urls import MAIN
from data.order import comment
from helpers import generate_info_client, generate_about_scooter_rent
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderPage:
    @allure.title('Тестируем оформление заказа с валидными данными')
    @pytest.mark.parametrize('button_position', ['down', 'up'])
    def test_created_order(self, driver, button_position):
        main_page = MainPage(driver)
        driver.get(MAIN)
        main_page.accept_cookie()
        main_page.click_order_button(button_position)

        # Генерируем новые данные прямо внутри теста
        info_client = generate_info_client()
        about_scooter_rent = generate_about_scooter_rent()

        order_page = OrderPage(driver)
        order_page.fill_form_about_info_client(
            name=info_client['name'],
            last_name=info_client['last_name'],
            address=info_client['address'],
            metro=info_client['metro'],
            phone=info_client['phone']
        )
        order_page.fill_form_about_rent(
            rent_day=about_scooter_rent['rent_day'],
            colour=about_scooter_rent['colour'],
            comment=comment
        )
        order_page.click_button_order_finall()
        order_page.confirmation_order()
        assert 'Заказ оформлен' in order_page.check_accept_order()
