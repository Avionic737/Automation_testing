import time
from selenium.webdriver.common.by import By


def test_add_to_cart_button_presence(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)  # Добавьте задержку

    # Проверяем наличие кнопки "Добавить в корзину" с помощью CSS-селектора
    add_to_cart_button = browser.find_element(By.CSS_SELECTOR, ".btn-add-to-basket")
    assert add_to_cart_button.is_displayed(), "Button 'Add to cart' is not displayed"
