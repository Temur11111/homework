
class Product:
    """Создание класса продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

class Category:
    """Создание класса категории"""
    name: str
    description: str
    products: list

    number_of_categories = 0###Количество категории
    number_of_products = 0 ###Количество товаров

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products

        Category.number_of_categories += 1
        Category.number_of_products += len(self.products)

