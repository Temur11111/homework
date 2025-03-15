from abc import ABC, abstractmethod

class BaseProduct(ABC):

    @abstractmethod
    def __add__(self, other):
        """метод сложения: реализует вывод общей стоимости двух товаров по логике остаток(1 товара)*цену(1 товара)+остаток(2 товара)*цена(2 товара)"""
        if type(self) == type(other):
            return  self.__price*self.quantity + other.__price*other.quantity
        else:
            raise ValueError("Ошибка!!!!Складывать можно только объекты одного класса!!!!")

    @property
    @abstractmethod
    def return_price(self):
        """геттер для вывода цены (так как она приватная)"""
        return self.__price

    @return_price.setter
    @abstractmethod
    def return_price(self, new_price):
        """сеттер для изменения цены конкретного продукта, без переопределения всего экземпляра(с проверкой корректности новой цены)"""
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price