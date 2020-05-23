import time


def test_add_to_basket_button(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    time.sleep(30)
    message = browser.find_element_by_css_selector("button.btn-add-to-basket")
    msg = message.text
    assert "Ajouter au panier" in msg, f'=== {msg}'
    time.sleep(5)
