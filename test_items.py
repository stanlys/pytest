from selenium.common.exceptions import NoSuchElementException
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_find_button_basket(browser):
    browser.get(link)
    time.sleep(5)
    try:
        button = browser.find_element_by_css_selector('.btn-add-to-basket')
    except NoSuchElementException:
        assert "---i do dot see this button----"
    assert "--------{}----------".format(button.text)