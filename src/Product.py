class Product:
    """Создание класса продуктов"""
    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        """Метод инициализации класса"""
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """метод возвращающий человечное представление экземпляра класса (конкретного продукта)"""
        return f"Название продукта: {self.name}, Цена: {self.__price}, Остаток: {self.quantity}"

    def __add__(self, other):
        """метод сложения: реализует вывод общей стоимости двух товаров по логике остаток(1 товара)*цену(1 товара)+остаток(2 товара)*цена(2 товара)"""
        return  self.__price*self.quantity + other.__price*other.quantity

    @classmethod
    def new_product(cls, product: dict):
        """Метод создания экземпляра класса из словаря"""
        name = str(product['name'])
        description = str(product['description'])
        price = float(product['price'])
        quantity = int(product['quantity'])
        return cls(name, description, price, quantity)

    @property
    def return_price(self):
        """геттер для вывода цены (так как она приватная)"""
        return self.__price


    @return_price.setter
    def return_price(self, new_price):
        """сеттер для изменения цены конкретного продукта, без переопределения всего экземпляра(с проверкой корректности новой цены)"""
        if new_price <= 0:
            print ("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price



product_1 = Product("яблоко", "зеленое", 10, 7)
product_2 = Product("банан", "желтый", 5, 40)

print(product_1)