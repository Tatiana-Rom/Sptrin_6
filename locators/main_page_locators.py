from selenium.webdriver.common.by import By

class MainPageLocators:
    order_button_up = (By.XPATH, '//button[contains(@class, "Button_Button") and text()="Заказать"]')
    order_button_down = (By.XPATH, '//button[contains(@class, "Button_Middle") and text()="Заказать"]')
    button_cookie = (By.ID, 'rcc-confirm-button')
    question_locator = (By.ID, 'accordion__heading-{}')
    answer_locator = (By.ID, 'accordion__panel-{}')
    question_locator_for_scroll = By.XPATH, '//div[@id="accordion__heading-7"]'
