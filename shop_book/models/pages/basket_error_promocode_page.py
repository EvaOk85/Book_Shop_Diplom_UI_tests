from selene import have, be, by
from selene.support.shared import browser


class BasketErrorPromocodePage:

    def open_page(self):
        browser.open("https://www.dom-knigi.ru/")
        return self

    def open_catalog_book (self):
        browser.element('a[href="/catalog/"]').click()
        browser.element('#bx_1847241719_8226').click()
        return self

    def add_book_basket(self):
        browser.all('.product-item-button-container').element(4).click()
        browser.all('.btn-buy.btn-sm').element(0).click()
        return self

    def enter_error_promocode(self, text):
        browser.element('.form-group').first_child.send_keys('ftruyui').press_enter()
        return self

    def check_promocode(self):
        browser.element('//span[contains(@class, "basket-coupon-text")]').should(have.text("FTRUYUI - не найден"))
        return self