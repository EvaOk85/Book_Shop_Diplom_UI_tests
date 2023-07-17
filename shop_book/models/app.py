from shop_book.models.pages.authorization_page import AuthorizationPage
from shop_book.models.pages.basket_error_promocode_page import BasketErrorPromocodePage
from shop_book.models.pages.basket_page import BasketPage
from shop_book.models.pages.error_authorization_page import ErrorAuthorizationPage
from shop_book.models.pages.making_an_order_page import MakingAnOrderPage
from shop_book.models.pages.search_page import SearchPage
from shop_book.models.pages.search_page_not_found import SearchPageNotFound


class ApplicationManager:

    def __init__ (self):
        self.search_page = SearchPage()
        self.search_page_not_found = SearchPageNotFound()
        self.basket_page = BasketPage()
        self.basket_error_promocode_page = BasketErrorPromocodePage()
        self.making_an_order_page = MakingAnOrderPage()
        self.authorization_page = AuthorizationPage()
        self.error_authorization_page = ErrorAuthorizationPage()


app = ApplicationManager()
