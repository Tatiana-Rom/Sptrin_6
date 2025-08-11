import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Принимаем Куки')
    def accept_cookie(self):
        return self.click_to_element(MainPageLocators.button_cookie)

    @allure.step('Кликаем по кнопке Заказать вверху страницы')
    def click_for_order_button_up(self):
        return self.click_to_element(MainPageLocators.order_button_up)

    @allure.step('Прокручиваем страницу вниз до кнопки Заказать')
    def scroll_for_order_button_down(self):
        button_order_finish = self.find_element_with_wait(MainPageLocators.order_button_down)
        self.scroll_for_element(button_order_finish)

    @allure.step('Кликаем по кнопке Заказать внизу страницы')
    def click_for_order_button_down(self):
        return self.click_to_element(MainPageLocators.order_button_down)

    @allure.step('Создаем заказ по кнопке')
    def created_order(self, button):
        self.click_to_element(button)

    @allure.step('Прокручиваем страницу до последнего вопроса')
    def scroll_for_question_block(self):
        last_question = self.find_element_with_wait(MainPageLocators.question_locator_for_scroll)
        return self.scroll_for_element(last_question)

    @allure.step('Клик на Вопрос')
    def click_for_question (self, question_id):
        locator_question = self.format_locators(MainPageLocators.question_locator, question_id)
        self.scroll_for_question_block()
        self.click_to_element(locator_question)

    @allure.step('Получение ответа на Вопрос')
    def get_answer_text(self, question_id):
        locator_answer = self.format_locators(MainPageLocators.answer_locator, question_id)
        self.scroll_for_question_block()
        return self.get_text_from_element(locator_answer)

    @allure.step('Проверяем ответ на Вопрос')
    def check_answer_for_question(self, question_id):
        self.click_for_question(question_id)
        return self.get_answer_text(question_id)

    @allure.step('Кликаем по кнопке Заказать по позиции')
    def click_order_button(self, position):
        if position == 'down':
            self.scroll_for_order_button_down()
            self.click_for_order_button_down()
        elif position == 'up':
            self.click_for_order_button_up()
        else:
            raise ValueError(f"Unknown button position: {position}")