

class Mixin_description_class:
    def __init__(self, *args, **kwargs) -> None:
        print(repr(self))

    def __repr__(self):
        """метод возвращающий человечное представление экземпляра класса (конкретного продукта)"""
        return f"Название продукта: {self.name}, Описание:{self.description}, Остаток: {self.quantity}"