import math
from typing import List


class Item():
    """
    A class used to represent a purchased item

    ...

    Attributes
    ----------
    quantity : int
        the number of purchased instances of the item
    name : str
        the name of the item
    price : float
        the price of a single item
    tag : str
        a tag to describe the item ["book", "food", "medical product", "other"]
    basic_rate : float
        basic sales tax (default is 0.1)
    exemptions : List[str]
        list of types of products that are exempt from tax
    """

    __quantity: int
    __name: str
    __price: float
    __tag: str
    basic_rate: float = 0.1
    exemptions: List[str] = ["book", "food", "medical product"]

    def __init__(self, quantity: int, name: str, price: float, tag: str = None) -> None:
        """
        Parameters
        ----------
        quantity : int
            the number of purchased instances of the item
        name : str
            the name of the item
        price : float
            the price of a single item
        tag : str
            a tag to describe the item (default is None)
        """
        self.__quantity = quantity
        self.__name = name
        self.__price = price
        self.__tag = tag

    def set_quantity(self, new_quantity: int) -> None:
        """Sets the quantity

        Parameters
        ----------
        new_quantity : int
            a new value for the number of purchased instances
        """
        self.__quantity = new_quantity

    def get_quantity(self) -> int:
        """Gets the quantity

        Returns
        -------
        int
            the number of purchased instances of the item
        """
        return self.__quantity

    def set_name(self, new_name: str) -> None:
        """Sets the name

        Parameters
        ----------
        new_name : str
            a new value for the name
        """
        self.__name = new_name

    def get_name(self) -> str:
        """Gets the name

        Returns
        -------
        str
            the name of the item
        """
        return self.__name

    def set_price(self, new_price: float) -> None:
        """Sets the price

        Parameters
        ----------
        new_price : float
            a new value for the name
        """
        self.__price = new_price

    def get_price(self) -> float:
        """Gets the price

        Returns
        -------
        float
            the price of the item
        """
        return self.__price

    def set_tag(self, new_tag: str) -> None:
        """Sets the tag

        Parameters
        ----------
        new_tag : str
            a new value for the tag
        """
        self.__tag = new_tag

    def get_tag(self) -> str:
        """Gets the tag

        Returns
        -------
        str
            the descriptive tag of the item
        """
        return self.__tag

    def get_sales_tax(self) -> float:
        """ Computes the sales tax of the item

        Returns
        -------
        float
            the sales tax of the item
        """
        rate = 0.0
        if self.__tag not in self.exemptions:
            rate += self.basic_rate
        return self.round_up(self.__price * rate, 0.05)

    def round_up(self, num: float, to: float) -> float:
        """ Rounds the sale tax to the nearest given precision

        Parameters
        ----------
        num : float
            a float number to round
        to : float
            floating point rounding precision

        Returns
        -------
        float
            the number rounded up to the nearest given precision
        """
        # ref: https://stackoverflow.com/a/70210770

        nearest = round(num / to) * to
        if math.isclose(num, nearest):
            return num
        return nearest if nearest > num else nearest + to
