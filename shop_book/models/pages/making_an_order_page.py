from selene import have, be, by
from selene.support.shared import browser


class MakingAnOrderPage:

    def open_page(self):
        browser.open("https://www.dom-knigi.ru/")
        return self

    def open_catalog_book (self):
        browser.element('a[href="/catalog/"]').click()
        browser.element('#bx_1847241719_8226').click()
        return self

    def add_book_basket(self):
        browser.all('.product-item-button-container').element(2).click()
        browser.all('.btn-buy.btn-sm').element(0).click()
        return self

    def order_forms(self):
        browser.element('[data-entity="basket-checkout-button"]').click()
        browser.element('button.pull-right.btn-primary').click()
        browser.element('button.pull-right.btn-primary').click()
        browser.element('input#soa-property-2').type('PevRot@mail.ru')
        browser.all('.form-control').element(2).type(79124560507)
        browser.element('button.pull-right.btn-primary').click()
        browser.element('#bx-soa-orderSave  a').click()
        return self

    def check_form(self):
        browser.element(by.partial_text('Согласие на обработку персональных данных')).should(be.visible)
        return self

    def rejection(self):
        browser.element('span.main-user-consent-request-popup-button-rej').click()