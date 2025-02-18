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

    number_of_categories = 0  ###Количество категории
    number_of_products = 0  ###Количество товаров

    def __init__(self, name, description, products):
        self.name = name  ###наименование категории
        self.description = description  ###описание категории
        self.products = products  ###список товаров
        Category.number_of_categories += 1
        Category.number_of_products += len(self.products)

    def add_products_in_category(self, product):
        """метод добавление товара в определенную категорию"""
        self.products = self.products.append(product)


category_1 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан"])
category_2 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан", "[eq"])
category_3 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан", "[eq"])

print(Category.number_of_products)
print(Category.number_of_categories)
