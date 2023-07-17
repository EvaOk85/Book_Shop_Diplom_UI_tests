import allure
from shop_book.models.app import app
from shop_book.models.date import date_page


def test_product_search_not_found():
    with allure.step('Открываем главную страницу и вводим в строку поска названия книги'):
        app.search_page_not_found.open_page(). \
            search_book(date_page.not_valid_name_book)
    with allure.step('Проверяем результат поиска'):
        app.search_page_not_found.check_error_search_book()


def test_product_search():
    with allure.step('Открываем главную страницу и вводим в строку поска Автора книги'):
        app.search_page.open_page(). \
            search_book(date_page.valid_name_author)
    with allure.step('Проверяем результат поиска'):
        app.search_page.check_valid_search_book()

def test_add_product():
    with allure.step('Открываем главную страницу и переходим в каталог Книги'):
        app.basket_page.open_page(). \
            open_catalog_book()
    with allure.step('Добавляем книги в карзину и переходим в карзину'):
        app.basket_page.add_book_basket()
    with allure.step('Проверяем наличие книг в карзине'):
        app.basket_page.check_books_in_basket()

def test_check_error_promocode():
   with allure.step('Открываем главную страницу и переходим в каталог Книги'):
       app.basket_error_promocode_page.open_page(). \
           open_catalog_book()
   with allure.step('Добавляем книгу в карзину и переходим в карзину'):
       app.basket_error_promocode_page.add_book_basket()
   with allure.step('Водим некорректный промокод'):
       app.basket_error_promocode_page.enter_error_promocode(date_page.error_promocode)
   with allure.step('Проверяем, что введенный промокод не найден'):
       app.basket_error_promocode_page.check_promocode()


def test_making_an_order():
    with allure.step('Открываем главную страницу и переходим в каталог Книги'):
        app.making_an_order_page.open_page(). \
            open_catalog_book()
    with allure.step('Добавляем книгу в карзину и переходим в карзину'):
        app.making_an_order_page.add_book_basket()
    with allure.step('Оформляем заказ'):
        app.making_an_order_page.order_forms()
    with allure.step('Проверяем, что отображается Согласие на обработку персональных данных'):
        app.making_an_order_page.check_form()
    with allure.step('Отказываемся от обработки персональных данных'):
        app.making_an_order_page.rejection()


def test_authorization():
    with allure.step('Открываем главную страницу и переходим в форму авторизации'):
        app.authorization_page.open_page(). \
            open_authorization()
    with allure.step('Вводим логин и пароль и авторизуемся'):
        app.authorization_page.authorization(date_page.login and date_page.password)
    with allure.step('Проверяем успешную авторизацию'):
        app.authorization_page.check_authorization()

def test_authorization_error_login():
    with allure.step('Открываем главную страницу и переходим в форму авторизации'):
        app.error_authorization_page.open_page(). \
            open_authorization()
    with allure.step('Вводим логин и пароль и авторизуемся'):
        app.error_authorization_page.authorization(date_page.error_login and date_page.password)
    with allure.step('Проверяем ошибку при регистрации'):
        app.error_authorization_page.check_error_authorization()

