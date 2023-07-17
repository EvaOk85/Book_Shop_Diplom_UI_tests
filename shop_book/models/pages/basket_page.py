from selene import have, be, by
from selene.support.shared import browser


class BasketPage:

    def open_page(self):
        browser.open("https://www.dom-knigi.ru/")
        return self

    def open_catalog_book (self):
        browser.element('a[href="/catalog/"]').click()
        browser.element('#bx_1847241719_8226').click()
        return self

    def add_book_basket(self):
        browser.element('.product-item-image-alternative').first_child.click()
        browser.element('.main-button-container').click()
        browser.element('a[href="/catalog/"]').click()
        browser.element('#bx_1847241719_8226').click()
        browser.all('.product-item-button-container').element(2).click()
        browser.all('.btn-buy.btn-sm').element(0).click()
        return self

    def check_books_in_basket(self):
        browser.element(by.partial_text('В корзине 2 товара')).should(be.visible)