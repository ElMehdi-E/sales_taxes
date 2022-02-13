from typing import List
from sales_taxes.item import Item


class ShoppingBasket():
    """
    A class representing a shopping basket

    ...

    Attributes
    ----------
    items : List[Item]
        a list to store puchased items
    taxes : float
        the total amounts of sales taxes paid
    total_price : float
        the total cost of the items
    """

    items: List[Item]
    taxes: float
    total_price: float

    def __init__(self) -> None:
        self.items = []
        self.taxes = 0.0
        self.total_price = 0.0

    def add_item(self, item: Item) -> None:
        """Add an item to the shopping basket

        Parameters
        ----------
        item : Item
            the item to be added to the shopping basket
        """

        self.items.append(item)

    def get_receipt(self) -> None:
        for item in self.items:
            sales_tax = item.get_sales_tax()
            self.taxes += sales_tax
            price_with_tax = item.get_price() + sales_tax
            self.total_price += price_with_tax
            print("{} {}: {:.2f}".format(item.get_quantity(), item.get_name(), price_with_tax))

        print("Sales Taxes: {:.2f}".format(self.taxes))
        print("Total: {:.2f}".format(self.total_price))

    def empty_basket(self) -> None:
        self.items = []
        self.taxes = 0.0
        self.total_price = 0.0
