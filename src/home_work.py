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
   """Создание класса категории"""
    name = str
    description = str
    products = list

   number_of_categories = 0###Колиество категории
   number_of_products = 0 ###Количество товаров

    def __init__(self, name, description, products):
        name = self.name
        description = self.description
        products = self.products
        number_of_categories+=1
        number_of_products = len(self.products)
