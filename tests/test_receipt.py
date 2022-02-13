from sales_taxes.item import Item
from sales_taxes.basket import ShoppingBasket


def test_input1(capture_stdout):
    item1 = Item(1, "book", 12.49, "book")
    item2 = Item(1, "music CD", 14.99, "other")
    item3 = Item(1, "chocolate bar", 0.85, "food")
    cart = ShoppingBasket()
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.get_receipt()
    assert capture_stdout["stdout"] == "1 book: 12.49\n" + \
                                       "1 music CD: 16.49\n" + \
                                       "1 chocolate bar: 0.85\n" + \
                                       "Sales Taxes: 1.50\n" + \
                                       "Total: 29.83\n"


def test_input2(capture_stdout):
    item1 = Item(1, "imported box of chocolates", 10.00, "food")
    item2 = Item(1, "imported bottle of perfume", 47.50, "other")
    cart = ShoppingBasket()
    cart.add_item(item1)
    cart.add_item(item2)
    cart.get_receipt()
    assert capture_stdout["stdout"] == "1 imported box of chocolates: 10.50\n" + \
                                       "1 imported bottle of perfume: 54.65\n" + \
                                       "Sales Taxes: 7.65\n" + \
                                       "Total: 65.15\n"


def test_input3(capture_stdout):
    item1 = Item(1, "imported bottle of perfume", 27.99, "other")
    item2 = Item(1, "bottle of perfume", 18.99, "other")
    item3 = Item(1, "packet of headache pills", 9.75, "medical product")
    item4 = Item(1, "box of imported chocolates", 11.25, "food")
    cart = ShoppingBasket()
    cart.add_item(item1)
    cart.add_item(item2)
    cart.add_item(item3)
    cart.add_item(item4)
    cart.get_receipt()
    assert capture_stdout["stdout"] == "1 imported bottle of perfume: 32.19\n" + \
                                       "1 bottle of perfume: 20.89\n" + \
                                       "1 packet of headache pills: 9.75\n" + \
                                       "1 imported box of chocolates: 11.85\n" + \
                                       "Sales Taxes: 6.70\n" + \
                                       "Total: 74.68\n"
