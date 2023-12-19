# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/02/2023
# Description: Recording the menu items and daily sales of a lemonade stand

class MenuItem:
	""" Creat a class about the lemonade stand menu, represent the menu item with name, whole cost and selling price """
	
	def __init__(self, name, whole_cost, selling_price):
		"""" Create three private variables. Initialize name, whole_cost and selling_price """
		self._name = name                       # name of menu item (private)
		self._whole_cost = whole_cost           # the whole cost of menu item (private)
		self._selling_price = selling_price     # the selling price of menu item (private)
		
	def get_name(self):
		return self._name
	def get_whole_cost(self):
		
		return self._whole_cost
	
	def get_selling_price(self):
		return self._selling_price
	
class SalesForDay:
	

	def __init__(self, day, sales_dict):
		self._day = day
		self._sales_dict = sales_dict
		
	def get_day(self):
		return self._day
	
	def get_sales_dict(self):
		return self._sales_dict
	

class LemonadeStand:
	

	def __init__(self, name):
		self._name = name
		self._day = 0
		self._menu = {}
		self._sales_record = []
		
	def get_name(self):
		return self._name
	
	def add_menu_item(self, menu_item):
		self._menu[menu_item.get_name()] = menu_item
		
	def enter_sales_for_day(self, sales_dict):
		try:
			for sale in sales_dict:
				if sale not in self._menu:
					raise InvalidSalesItemError("Item not in menu")
			sales_for_day = SalesForDay(self._day, sales_dict)
			self._sales_record.append(sales_for_day)
			self._day += 1
		except InvalidSalesItemError as ise:
			print(ise)
			
	def get_sales_dict_for_day(self, day):
		for sale in self._sales_record:
			if sale.get_day() == day:
				return sale.get_sales_dict()
		return None
	
	def sales_of_menu_item_for_day(self, item_name):
		total_sales = 0
		for sale in self._sales_record:
			sales_dict = sale.get_sales_dict()
			if item_name in sales_dict:
				total_sales += sales_dict[item_name]
		return total_sales
	def total_sales_for_menu_item(self, item_name):
		total_sales = self.sales_of_menu_item_for_day(item_name)
		item = self._menu[item_name]
		total_profit = total_sales * (item.get_selling_price() - item.get_whole_cost())
		return total_profit
	def total_profit_for_menu_item(self):
		total_profit = 0
		for item in self._menu:
			total_profit += self.total_sales_for_menu_item(item)
		return total_profit
	
    
class InvalidSalesItemError(Exception):
	pass

if __name__ == "__main__":
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
		stand.enter_sales_for_day({'cupcake':1})
	except InvalidSalesItemError as ise:
		print(ise)
	stand.enter_sales_for_day(day_0_sales)
	print(f"lemonade profit = {stand.total_sales_for_menu_item('lemonade')}") 