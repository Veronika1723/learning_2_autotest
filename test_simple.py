from selene import be, have
from selene.support.shared import browser


def test_first(configuration_browser, open_browser):
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('Selene - User'))
    browser.all('[id=search] [class~=g]').should(have.size_greater_than(6))


def test_second(configuration_browser, open_browser):
    """Тест упадет"""
    browser.element('[name=q]').should(be.blank).type('selene').press_enter()
    browser.element('[id=search]').should(have.text('Selena - User'))
    browser.all('[id=search] [class~=g]').should(have.size_greater_than(6))

