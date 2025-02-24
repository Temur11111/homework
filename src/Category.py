from src.Product import Product


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
        return f"Наименование: {self.name}, Описание: {self.description}, Количество товаров в категории: {Category.number_of_products}"


    def add_products_in_category(self, product: Product):
        """метод добавления нескольких товаров в определенную категорию"""
        self.__products.append(product)  # добавляем новые продукты в список
        Category.number_of_products += 1  # увеличиваем количество продуктов(товаров) в категориии


    @property
    def return_products(self):
        """геттер для вывода товаров в категории (так как список товаров приватный)"""
        return self.__products

