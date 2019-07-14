link = "http://selenium1py.pythonanywhere.com/ru/catalogue/coders-at-work_207/"

def test_button_basket(browser):
    browser.get(link)
    button = browser.find_element_by_css_selector(("[class='..btn-add-to-basket']"))
