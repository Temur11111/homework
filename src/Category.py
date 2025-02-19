class Category:
    """Создание класса категории"""
    name: str
    description: str
    products: list

    number_of_categories = 0  #Количество категории
    number_of_products = 0  #Количество товаров

    def __init__(self, name, description, products):
        self.name = name  #наименование категории
        self.description = description  #описание категории
        self.__products = products  #список товаров
        Category.number_of_categories += 1
        Category.number_of_products += len(self.__products)

    def add_products_in_category(self, *products):
        """метод добавления нескольких товаров в определенную категорию"""
        self.__products.extend(products)  # добавляем новые продукты в список
        Category.number_of_products += len(products)  # увеличиваем общее количество продуктов


