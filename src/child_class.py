from src.Product import Product
from src.abstract_class import BaseProduct

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




