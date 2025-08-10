import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_current_url(self):
        return self.driver.current_url

    @allure.title('Ожидаем появления URL в текущем URL')
    def wait_for_url_contains(self, text, timeout=15):
        return WebDriverWait(self.driver, timeout).until(
            lambda d: text in d.current_url
        )

    @allure.title('Ищем элемент на странице')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 15).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.title('Кликаем по элементу')
    def click_to_element(self, locator):
        WebDriverWait(self.driver, 30).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator).click()

    @allure.title('Добавляем текст в элемент')
    def add_text_to_element(self, locator, text):
        self.find_element_with_wait(locator).send_keys(text)


    @allure.title('Получаем текст элемента')
    def get_text_from_element(self, locator):
        return self.find_element_with_wait(locator).text

    @allure.title('Пролистываем страницу до элемента')
    def scroll_for_element(self, name_element):
        self.driver.execute_script("arguments[0].scrollIntoView();", name_element)

    @allure.title('Переходим на последнюю открывшуюся вкладку')
    def switch_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def format_locators(self, locator_1, question_id):
        method, locator = locator_1
        locator = locator.format(question_id)

        return (method, locator)