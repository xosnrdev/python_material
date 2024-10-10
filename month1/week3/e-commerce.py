from datetime import datetime


class Product:
    def __init__(
            self,
            name: str,
            price: float,
            stock: int,
            weight: float
    ):
        self.name = name
        self.price = price
        self.stock = stock
        self.weight = weight

    def get_info(self) -> str:
        return f"Product Name: {self.name}, Price: ${self.price:.2f}, Stock: {self.stock}, Weight: {self.weight:.1f} kg"

    def apply_discount(self, discount_percentage: float) -> str:
        discount_amount = self.price * (discount_percentage / 100)
        self.price -= discount_amount
        return f"\nAfter {discount_percentage}% discount:\n" + self.get_info()

    def check_stock(self, quantity: int) -> str:
        if quantity > self.stock:
            return "Out of stock"
        else:
            self.stock -= quantity
            return f"Order {quantity} units of {self.name}: Successful, Stock Left: {self.stock}"

    def calculate_shipping_cost(self) -> str:
        rate_per_kg = 10
        cost = self.weight * rate_per_kg
        return f"Shipping cost for {self.name}: ${cost:.2f}"


class ElectronicProduct(Product):
    def __init__(self, warranty_years: int, brand: str, name: str, price: float, stock: int, weight: float):
        super().__init__(name, price, stock, weight)
        self.warranty_years = warranty_years
        self.brand = brand

    def get_info(self) -> str:
        return f"Electronic Product: {self.name} (Brand: {self.brand}), Price: ${self.price:.2f}, Warranty: {self.warranty_years} years, Stock: {self.stock}, Weight: {self.weight:.1f} kg"

    def calculate_warranty_extension(self, extra_years: int) -> str:
        extended_warranty = self.warranty_years + extra_years
        return f"Extended warranty for {self.name}: {extended_warranty} years"


class GroceryProduct(Product):
    def __init__(self, expiration_date: str, is_perishable: bool, name: str, price: float, stock: int, weight: float):
        super().__init__(name, price, stock, weight)
        self.expiration_date = expiration_date
        self.is_perishable = is_perishable

    def get_info(self) -> str:
        return f"Grocery Product: {self.name}, Price: ${self.price:.2f}, Expiration Date: {self.expiration_date}, Stock: {self.stock}, Weight: {self.weight:.1f} kg, Perishable: {self.is_perishable}"

    def check_if_expired(self, current_date: str) -> str:
        current_dt = datetime.strptime(current_date, '%Y-%m-%d')
        expiration_dt = datetime.strptime(self.expiration_date, '%Y-%m-%d')
        is_expired = current_dt > expiration_dt
        return f"Is {self.name} expired? {is_expired}"


laptop = ElectronicProduct(name="Laptop", brand="Dell", price=1500, warranty_years=3, weight=2.5, stock=10)
milk = GroceryProduct(name="Milk", price=4, expiration_date="2024-11-15", weight=1, stock=50, is_perishable=True)

print(laptop.get_info())
print(milk.get_info())

print(laptop.apply_discount(15))

print(laptop.check_stock(5))
print(milk.check_stock(5))

print(laptop.calculate_shipping_cost())
print(milk.calculate_shipping_cost())

print(laptop.calculate_warranty_extension(2))

print(milk.check_if_expired('2024-10-01'))
