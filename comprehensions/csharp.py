from typing import Union


class OnlineStore:
    def __init__(self, store_name: str, inventory: dict, prices: dict):
        self.store_name = store_name
        self.inventory = inventory
        self.prices = prices

    def add_item(self, item_name: str, stock: int, price: float):
        if item_name not in self.inventory:
            self.inventory[item_name] = stock
        else:
            self.inventory[item_name] += stock

        if self.prices[item_name] != price:
            self.prices[item_name] = price

    def check_stock(self, item_name: str):
        return self.inventory.get(item_name, 0)

    def update_price(self, item_name: str, new_price: float):
        if self.prices[item_name] != new_price:
            self.prices[item_name] = new_price

    def purchase(self, item_name: str, quantity: int) -> Union[str, float]:
        if self.inventory.get(item_name, 0) >= quantity:
            total = quantity * self.prices[item_name]
            self.inventory[item_name] -= quantity
            return f'{item_name} has been ordered. your total cost is {total}'
        return f'{item_name} cannot be ordered! not enough items in stock!'
