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
        """Prints out the receipt details for the shopping basket"""

        for item in self.items:
            qty = item.get_quantity()
            # get the sales tax for each item
            sales_tax = item.get_sales_tax()
            self.taxes += sales_tax * qty
            # add the item's price to the total price
            price_with_tax = item.get_price() + sales_tax
            self.total_price += price_with_tax * qty
            # correct the name of item
            name = item.get_name()
            if "imported" in name:
                name_list = name.split(" ")
                idx = name_list.index("imported")
                if idx != 0:
                    name_list.pop(idx)
                    name = "imported " + " ".join(name_list)
            # list the name of all the items and their price
            print("{} {}: {:.2f}".format(item.get_quantity(), name, price_with_tax))
        # the total amounts of sales taxes paid
        print("Sales Taxes: {:.2f}".format(self.taxes))
        # the total cost of the items
        print("Total: {:.2f}".format(self.total_price))

    def empty_basket(self) -> None:
        """Resets the shopping basket"""

        self.items = []
        self.taxes = 0.0
        self.total_price = 0.0
