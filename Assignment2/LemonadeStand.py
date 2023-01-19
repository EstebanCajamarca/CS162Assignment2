# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/18/2023
# Assignment 2.
#
#


import objects as objects


class Invalid_sales_statement_error(Exception):
    pass


class MenuItem:
    """Represents menu item to be offered."""

    def __init__(self, name, wholesale_cost, selling_price):  # data members are private.
        self._name = name
        self._wholesale_cost = wholesale_cost
        self._selling_price = selling_price

    def get_name(self):
        """To access name from outside MenuItem class."""
        return self._name

    def get_wholesale_cost(self):
        """To access wholesale_cost from outside MenuItem class."""
        return self._wholesale_cost

    def get_selling_price(self):
        """To access selling_price from outside MenuItem class."""
        return self._selling_price


class SalesForDay:
    """Represents sells for a particular day."""

    def __init__(self, day, sales_dictionary):  # data members are private.
        self._day = day
        self._sales_dict = sales_dictionary

    def get_day(self):
        """To access day from outside SalesForDay class."""
        return self._day

    def get_sales_dict(self):
        """To access sales_dict from outside SalesForDay class."""
        return self._sales_dict


class LemonadeStand:
    """Represents a lemonade stand."""

    def __init__(self, stand_name):
        self._stand_name = stand_name
        self._current_day = 0
        self._menu = {}
        self._sales_record = []

    def get_name(self):
        """Gets Name"""
        return self.get_name()

    def add_menu_item(self, menu_item_objects):  # Here!
        self._menu[menu_item_objects.get_name()] = menu_item_objects
        print(self._menu)

    def enter_sales_for_today(self, sales_dictionary):
        items_sold = sales_dictionary.keys()

        for item in sales_dictionary:
            if item not in items_sold:
                items_sold = 0
            elif item != MenuItem:
                raise Invalid_sales_statement_error
                items_sold = 0
            else:
                self._sales_record.append(sales_dictionary)

    def sales_of_menu_item_for_day(self, day, name_menu_item):
        for sell in self._sales_for_day_list:
            if day == sell.get_day:
                return objects.get_sales_dictionary()[name_menu_item]

    def total_sales_for_menu_item(self, menu_name):
        total_sales = 0
        for today_sales in self.sales_record:
            total_sales += today_sales.get_sales_dict()[menu_name]
            return total_sales

    def total_profit_for_menu_item(self, menu_items_name):
        item_sales_history = self.total_sales_for_menu_item(menu_items_name)
        menu_item = self._menu.get(menu_items_name)
        items_total_sales_profit = item_sales_history * menu_item.get_selling_price() - item_sales_history * menu_item.get_wholesale_cost()
        return items_total_sales_profit

    def total_profit_for_stand(self):
        total_profit = 0
        for items in self.enter_sales_for_today.keys():
            total_profit += self.total_profit_for_menu_item()
            return total_profit


stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand called 'Lemons R Us'
item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'

# This dictionary records that on day zero, 5 lemonades were sold, 2 cookies were sold, and no nori was sold
day_0_sales = {
    'lemonade': 5,
    'cookie': 2
}

stand.enter_sales_for_today(day_0_sales)  # Record the sales for day zero
print(f"lemonade profit = {stand.total_profit_for_menu_item('lemonade')}")  # print the total profit for lemonade so far

