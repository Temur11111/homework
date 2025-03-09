from itertools import product

import pytest

from src.Product import Product, product_2, product_1
from src.Category import Category, category_1
from src.child_class import Smartphone, LawnGrass, smartphone_2, smartphone_1, grass_1

def test_product_initialization():
    """тест инициализации класса продуктов"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.return_price == 100.0
    assert product.quantity == 10

def test_category_initialization():
    """ тест инициализации класса категории"""
    category = Category("Test Name", "Test Description")
    assert category.name == "Test Name"
    assert category.description == "Test Description"


@pytest.fixture(autouse=True)
def reset_category_counts():
    # Перед каждым тестом обнуляем количество категорий и продуктов
    Category.number_of_categories = 0
    Category.number_of_products = 0


def test_number_of_categories():
    """тест проверки правильности подсчета количества категории"""
    category_1 = Category("Фрукты", "Свежие фрукты")
    category_2 = Category("Овощи", "Свежие овощи")
    assert Category.number_of_categories == 2


def test_add_products_in_category():
    """тест проверки правильности добавления продуктов в категорию"""
    product_1 = Product("яблоко", "зеленое", 10, 10)
    product_2 = Product("яблоко", "красное", 11, 10)
    category_1 = Category("Фрукты", "Свежие фрукты")
    category_1.add_products_in_category(product_1)
    category_1.add_products_in_category(product_2)
    assert len(category_1.return_products) == 2




def test_number_of_products():
    """тест проверки правильности подсчета количества продуктов в категории"""
    product_1 = Product("яблоко", "зеленое", 10, 10)
    product_2 = Product("яблоко", "красное", 11, 10)
    category_1 = Category("Фрукты", "Свежие фрукты")
    category_1.add_products_in_category(product_1)
    category_1.add_products_in_category(product_2)
    assert Category.number_of_products == 2


def test_create_product():
    """Тест правильного создания экземпляра класса Product"""
    # Данные для проверки
    product_data = {
        'name': 'Phone',
        'description': 'Smartphone with 5G',
        'price': 699.99,
        'quantity': 10
    }

    # Создаем экземпляр через метод new_product
    product = Product.new_product(product_data)

    # Проверяем значения атрибутов
    assert product.name == 'Phone'
    assert product.description == 'Smartphone with 5G'
    assert product.return_price == 699.99  # Проверяем через геттер
    assert product.quantity == 10


def test_price_getter():
    """Тест работы геттера для приватного атрибута __price"""
    product = Product('Laptop', 'High-performance laptop', 1299.99, 5)
    # Проверяем, что геттер возвращает корректное значение цены
    assert product.return_price == 1299.99


def test_price_setter_correct_value():
    """Тест работы сеттера: корректное изменение цены"""
    product = Product('Tablet', 'Portable tablet', 499.99, 15)

    # Изменяем цену через сеттер
    product.return_price = 599.99

    # Проверяем, что цена изменилась
    assert product.return_price == 599.99


def test_price_setter_incorrect_value():
    """Тест работы сеттера: некорректное значение цены"""
    product = Product('Smartwatch', 'Wearable device', 199.99, 20)

    # Попробуем установить некорректную цену (отрицательное значение)
    product.return_price = -50

    # Цена не должна измениться
    assert product.return_price == 199.99


def test_category_str_method():
    """тест правильности выполнения метода Str для класса Category (проверка выдачи правильной строки)"""
    product_1 = Product("яблоко", "зеленое", 10, 7)
    product_2 = Product("банан", "желтый", 5, 40)
    category_1 = Category("Фрукты", "Свежие")
    category_1.add_products_in_category(product_1)
    category_1.add_products_in_category(product_2)
    expected_str = "Наименование: Фрукты, Количество товаров в категории: 47"
    assert category_1.__str__() == expected_str

def test_product_str_method():
    """тест правильности выполнения метода Str для класса Product (проверка выдачи правильной строки)"""
    product_1 = Product("яблоко", "зеленое", 10, 7)
    expected_str = "Название продукта: яблоко, Цена: 10, Остаток: 7"
    assert product_1.__str__() == expected_str

def test_add_method_in_product():
    """тест правильной работы метода add в классе Product"""
    product_1 = Product("яблоко", "зеленое", 10, 7)
    product_2 = Product("банан", "желтый", 5, 40)
    expected_total_price = (10 * 7) + (5 * 40)
    assert product_1 + product_2 == expected_total_price

def test_false_add_method_in_product():
    """тест выдачи ошибки метода add в классе Product"""
    product_1 = Product("яблоко", "зеленое", 10, 7)
    grass_1 = LawnGrass("полынь", "сорняк", 1, 1, "Россия", 2, "зеленый")
    with pytest.raises(ValueError) as excinfo:
        product_1 + grass_1  # Попытка сложения объектов разных классов
    # Проверяем сообщение об ошибке
    assert str(excinfo.value) == "Ошибка!!!!Складывать можно только объекты одного класса!!!!"

def test_add_products_in_category():
    """тест выдачи ошибки метода добавления продуктов в категорию"""
    # Создаем другой класс для тестирования
    class OtherProduct:
        def __init__(self, name, price, quantity):
            self.name = name
            self.__price = price
            self.quantity = quantity
    # Создаем экземпляр другого класса
    other_product = OtherProduct("Товар 2", 20.0, 2)
    # Проверяем, что при добавление экземпляра другого класса возникает ValueError
    with pytest.raises(ValueError) as excinfo:
        category_1.add_products_in_category(other_product)  # Попытка добавления объекта другого класса
    # Проверяем сообщение об ошибке
    assert str(excinfo.value) == "Ошибка!!!!Добавлять можно только объекты класса Product, либо объекты классов его наследников"