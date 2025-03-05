from src.Product import Product, product_1, product_2


class Category:
    """Создание класса категории"""
    name: str
    description: str

    number_of_categories = 0  #Количество категории
    number_of_products = 0  #Количество продуктов(товаров) в категории

    def __init__(self, name, description):
        """Метод инициализации класса"""
        self.name = name  #наименование категории
        self.description = description  #описание категории
        self.__products = []  #список товаров (экземпляры класса Product)
        Category.number_of_categories += 1

    def __str__(self):
        """метод возвращающий человечное представление экземпляра класса (конкретной категории товаров)"""
        quantity_summ = 0
        for product in self.__products:### осуществление перебора по всем продуктам(экземплярам класса Product) и сложение остатков товаров по всем продуктам определенной категории
            quantity_summ += product.quantity
        return f"Наименование: {self.name}, Количество товаров в категории: {quantity_summ}"


    def add_products_in_category(self, product: Product):
        """метод добавления нескольких товаров в определенную категорию"""
        self.__products.append(product)  # добавляем новые продукты в список
        Category.number_of_products += 1  # увеличиваем количество продуктов(товаров) в категориии


    @property
    def return_products(self):
        """геттер для вывода товаров в категории (так как список товаров приватный)"""
        return self.__products

category_1 = Category("Фрукты", "Свежие")

category_1.add_products_in_category(product_1)
category_1.add_products_in_category(product_2)

print(category_1)