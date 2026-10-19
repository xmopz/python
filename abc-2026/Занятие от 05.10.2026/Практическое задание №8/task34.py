# Композиция и вычисляемые свойства
# todo: Класс "Заказ"
# Создайте класс Order (Заказ). Внутри он хранит список экземпляров Product (из предыдущей задачи 37).
# Реализуйте свойство total_price, которое вычисляет общую стоимость заказа на основе цен всех товаров
# в списке. Реализуйте методы add_product(product) и remove_product(product) для управления списком.
"""
# Пример использования
book = Product("Book", 10)
pen = Product("Pen", 2)
order = Order()
order.add_product(book)
order.add_product(pen)
print(f"Общая стоимость: {order.total_price}")  # 12
"""

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = max(0, value)

class Order:
    def __init__(self):
        self._products = []

    def add_product(self, product):
        self._products.append(product)

    def remove_product(self, product):
        self._products.remove(product)

    @property
    def total_price(self):
        return sum(product.price for product in self._products)

book = Product("Book", 10)
pen = Product("Pen", 2)

order = Order()
order.add_product(book)
order.add_product(pen)

print(f"Общая стоимость: {order.total_price}")  # 12

order.remove_product(pen)
print(f"После удаления ручки: {order.total_price}")  # 10
