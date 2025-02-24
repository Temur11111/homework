from itertools import product

import pytest
from src.Product import Product
from src.Category import Category



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