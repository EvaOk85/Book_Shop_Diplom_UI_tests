from selene import have, be, by
from selene.support.shared import browser


class SearchPageNotFound:

    def open_page (self):
        browser.open("https://www.dom-knigi.ru/")
        return self

    def search_book (self, text):
        browser.element('[name="q"]').send_keys('Вилка серебрянная')
        browser.element('[name="q"]').submit()
        return self

    def check_error_search_book (self):
        browser.element(by.partial_text('К сожалению, на ваш поисковый запрос ничего не найдено.')).should(be.visible)