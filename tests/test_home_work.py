from src.home_work import Category, Product

def test_product_initialization():
    """тест инициализации класса продуктов"""
    product = Product("Test Product", "Test Description", 100.0, 10)
    assert product.name == "Test Product"
    assert product.description == "Test Description"
    assert product.price == 100.0
    assert product.quantity == 10

def test_category_initialization():
    """ тест инициализации класса категории"""
    category = Category("Test Name", "Test Description", ["Test Product", "Test Product_1"])
    assert category.name == "Test Name"
    assert category.description == "Test Description"
    assert category.products == ["Test Product", "Test Product_1"]

def test_number_of_categories():
    """тест проверки правильности подсчета количества категории"""
    category_1 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан"])
    category_2 = Category("Овощи", "Свежие овощи", ["морковь", "огурец", "помидор"])
    assert Category.number_of_categories == 2

def test_number_of_products():
    """тест проверки правильности подсчета количества продуктов"""
    category_1 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан", "огурец"])
    category_2 = Category("Овощи", "Свежие овощи", ["морковь", "огурец", "помидор"])
    assert Category.number_of_products == 6