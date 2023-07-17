from selene import have, be, by
from selene.support.shared import browser


class SearchPage:

    def open_page (self):
        browser.open("https://www.dom-knigi.ru/")
        return self

    def search_book (self, text):
        browser.element('[name="q"]').send_keys('Лем С.')
        browser.element('[name="q"]').submit()
        return self

    def check_valid_search_book (self):
        browser.element(by.partial_text('Лем С.')).should(be.visible)