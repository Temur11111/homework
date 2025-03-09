from src.Product import Product, product_1, product_2


class Smartphone(Product):
    efficiency = float ### производительность
    model = str ### модель
    memory = float ### объем памяти
    color = str ### цвет
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price,quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    country = str ### страна-производитель
    germination_period = float ### срок прорастания
    color = str  ### цвет
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price,quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color




smartphone_1 = Smartphone("Nokia", "Кнопочный", 5, 2, 1, "3350", 32, "черный")
smartphone_2 = Smartphone("Nokia", "Кнопочный", 6, 1, 1, "3350", 32, "черный")

grass_1 = LawnGrass("полынь", "сорняк", 1, 1, "Россия", 2, "зеленый")

