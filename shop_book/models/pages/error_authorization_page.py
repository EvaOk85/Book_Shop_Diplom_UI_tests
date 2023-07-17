from selene import  be, by
from selene.support.shared import browser


class ErrorAuthorizationPage:

    def open_page (self):
        browser.open("https://www.dom-knigi.ru/")
        return self

    def open_authorization (self):
        browser.all('.icon-txt').element(0).click()
        return self

    def authorization (self, text):
        browser.element('[name="USER_LOGIN"]').send_keys('Eva86')
        browser.element('[name="USER_PASSWORD"]').send_keys('123456789')
        browser.element('[name="Login"]').click()
        return self

    def check_error_authorization (self):
        browser.element(by.partial_text('Неверный логин или пароль.')).should(be.visible)
        return self