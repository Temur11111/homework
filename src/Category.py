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


category_1 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан"])
category_2 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан", "eq"])
category_3 = Category("Фрукты", "Свежие фрукты", ["яблоко", "банан", "eq"])

print(Category.number_of_products)
#print(Category.number_of_categories)


category_1.add_products_in_category("ghbjhb","ивыиы","мттывмо","sdjnv")
print(Category.number_of_products)