import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_check_add_button_on_the_page_with_different_language(browser):
    browser.get(link)
    time.sleep(30)
    assert browser.find_element_by_css_selector("#add_to_basket_form > button"), "Error, the button doesn't find"
