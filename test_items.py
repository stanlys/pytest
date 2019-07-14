from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_button_basket(browser):
    browser.get(link)
    time.sleep(30)
    try:
        button = browser.find_element_by_css_selector('.btn-add-to-basket')
    except NoSuchElementException:
        assert button == "Добавить в    корзину","My Error 1"
    buttontext = button.text
    print("--------{}----------".format(buttontext))