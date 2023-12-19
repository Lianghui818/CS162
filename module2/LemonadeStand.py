# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/02/2023
# Description: Recording the menu items and daily sales of a lemonade stand

class InvalidSalesItemError(Exception):
	""" Exception class"""
	pass

class MenuItem:
	""" Creat a class about the lemonade stand menu, represent the menu item with name, whole cost and selling price """
	
	def __init__(self, name, whole_cost, selling_price):
		"""" Create three private variables. Initialize name, whole_cost and selling_price """
		self._name = name                       # name of menu item (private)
		self._whole_cost = whole_cost           # the whole cost of menu item (private)
		self._selling_price = selling_price     # the selling price of menu item (private)
		
	def get_name(self):
		""" Using get_name method to get name """
		return self._name           # return the name stored in _name
	
	def get_whole_cost(self):
		""" Using get_whole_cost method to get whole cost """
		return self._whole_cost     # return the whole cost stored in _whole_cost
	
	def get_selling_price(self):
		""" Using get_selling_price method to get selling price """
		return self._selling_price  # return the selling price stored in _selling_price
	
class SalesForDay:
	""" Creat a class about the lemonade stand sales for day, represent with day and sales_dict """
	
	def __init__(self, day, sales_dict):
		"""" Create two private variables. Initialize day and sales_dict """
		self._day = day                     # sales day (private)
		self._sales_dict = sales_dict       # sales_dict of the day (private)
		
	def get_day(self):
		""" Using get_day method to get the day """
		return self._day                   # return the day stored in _day
	
	def get_sales_dict(self):
		""" Using get_sales_dict method to get sales_dict """
		return self._sales_dict            # return the sales_dict stored in _sales_dict
	
class LemonadeStand:
	""" Creat a class about lemonade stand, represent with name """
	
	def __init__(self, name):
		"""" Create one private variable. Initialize name """
		self._name = name               # name of menu item (private)
		self._day = 0                   # _day: records the number of days the stall is in operation, initialized to 0
		self._menu = {}                 # _menu: a dictionary to store menu items
		self._sales_record = []         # _sales_record: a list to store sales records for each day.
		
	def get_name(self):
		""" Using get_name method to get name """
		return self._name               # return the name stored in _name
	
	def add_menu_item(self, menu_item):
		""" Using add_menu_item method to add item to menu """
		self._menu[menu_item.get_name()] = menu_item        # add menu item to the _menu dictionary
		
	def enter_sales_for_day(self, sales_dict):
		""" Create a method named enter_sales_for_day, sales_dict indicates the day's sales record """
		try:
			for sale in sales_dict:                 # for loop loops through each sale item in sales_dict
				if sale not in self._menu:          # if the sales item is not in _menu
					raise InvalidSalesItemError("Item not in menu")         # raises a custom exception: InvalidSalesItemError
			sales_for_day = SalesForDay(self._day, sales_dict)          # if all sales items are in the menu, create a SalesForDay object
			self._sales_record.append(sales_for_day)               # add it to the _sales_record list
			self._day += 1              # the value of _day increased by 1
		except InvalidSalesItemError:
			print("InvalidSalesItemError: Item not in menu ")        # print exception error: InvalidSalesItemError
			
	def get_sales_dict_for_day(self, day):
		"""Create a method named get_sales_dict_for_day """
		for sale in self._sales_record:             # for loop loops through each sales record object in the _sales_record list
			if sale.get_day() == day:               # finds a sales record that matches the specified date
				return sale.get_sales_dict()        # returns the sales dictionary for that sales record
		return None         # if no matching sales record is found, returne None
	
	def sales_of_menu_item_for_day(self, item_name): 
		""" Create a method named sales_of_menu_item_for_day """
		total_sales = 0             # initialized the total sales to 0
		for sale in self._sales_record:         # for loop loops through each sales record object in the _sales_record list
			sales_dict = sale.get_sales_dict()          # retrieving the sales dictionary for each sales record
			if item_name in sales_dict:         # if the specified menu item name exists in the sales dictionary
				total_sales += sales_dict[item_name]           # the corresponding sales are added to the total_sales variablethe
		return total_sales          # return total sales
	
	def total_sales_for_menu_item(self, item_name):
		""" Create a method called total_sales_for_menu_item """
		total_sales = self.sales_of_menu_item_for_day(item_name)         # call the sales_of_menu_item_for_day method to calculate the total sales for the specified menu item
		item = self._menu[item_name]            
		total_profit = total_sales * (item.get_selling_price() - item.get_whole_cost())         # profit is equal to selling price minus whole cost
		return total_profit         # return total profit 
	
	def total_profit_for_menu_item(self):
		""" Create a method called total_profit_for_menu_item """
		total_profit = 0        # initialized the total sales to 0
		for item in self._menu:         # for loop loops through each menu item name in the _menu dictionary
			total_profit += self.total_sales_for_menu_item(item)        # calculate the profit for each menu item and add the profit to the total_profit variable
		return total_profit         # return total profit
	

def main():
	""" Creat the main method"""
	stand = LemonadeStand('Lemons R Us')  # Create a new LemonadeStand callled 'Lemons R Us'
	item1 = MenuItem('lemonade', 0.5, 1.5)  # Create lemonade as a menu item (wholesale cost 50 cents, selling price $1.50)
	stand.add_menu_item(item1)  # Add lemonade to the menu for 'Lemons R Us'
	item2 = MenuItem('nori', 0.6, 0.8)  # Create nori as a menu item (wholesale cost 60 cents, selling price 80 cents)
	stand.add_menu_item(item2)  # Add nori to the menu for 'Lemons R Us'
	item3 = MenuItem('cookie', 0.2, 1)  # Create cookie as a menu item (wholesale cost 20 cents, selling price $1.00)
	stand.add_menu_item(item3)  # Add cookie to the menu for 'Lemons R Us'
	day_0_sales = {
        'lemonade' : 5,
        'cookie'   : 2
	}
	try:
		stand.enter_sales_for_day({'egg':1})
	except InvalidSalesItemError as ise:
		print(ise)
	stand.enter_sales_for_day(day_0_sales)
	print(f"lemonade profit = {stand.total_sales_for_menu_item('lemonade')}") 

if __name__ == '__main__':
	main()