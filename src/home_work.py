from symtable import Class

class Product
  """Создание класса продуктов"""
    name = str
    description = str
    price = float
    quantity = int

    def __init__(self, name, description, price, quantity):
        name = self.name
        description = self.description
        price = self.price
        quantity = self.quantity

class Category
    name = str
    description = str
    products = list

    def __init__(self, name, description, products):
        name = self.name
        description = self.description
        products = self.products
