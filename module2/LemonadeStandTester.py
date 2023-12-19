# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/05/2023
# Description: Recording the menu items and daily sales of a lemonade stand and teat

import unittest
import LemonadeStand


class TestLemonadeStand(unittest.TestCase):
	""" Creat TestLemonadeStand class """
	
	def setUp(self):
		""" Set up the stand """
		self.stand = LemonadeStand('Lemons R Us')
		self.item1 = LemonadeStand.MenuItem('lemonade', 0.5, 1.5)
		self.stand.add_menu_item(self.item1)
		self.item2 = LemonadeStand.MenuItem('nori', 0.6, 0.8)
		self.stand.add_menu_item(self.item2)
		self.item3 = LemonadeStand.MenuItem('cookie', 0.2, 1)
		self.stand.add_menu_item(self.item3)
		self.day0 = {
			'lemonade' : 5,
			'cookie'   : 2
		}
		
	def test_init(self):
		""" Text the init method"""
		self.assertEqual(self.stand.get_name(), 'Lemons R Us')
		self.assertEqual(self.stand._day, 0)
		self.assertEqual(self.stand._menu, {'lemonade': self.item1, 'nori': self.item2, 'cookie': self.item3})
		self.assertEqual(self.stand._sales_record, [])
		
	def test_add_menu_item(self):
		"""" Text the add_menu_item method """
		self.assertEqual(self.stand._menu, {'lemonade': self.item1, 'nori': self.item2, 'cookie': self.item3})
		item4 = LemonadeStand.MenuItem('ice cream', .3, 1.5)
		self.stand.add_menu_item(item4)
		self.assertEqual(self.stand._menu, {'lemonade': self.item1, 'nori': self.item2, 'cookie': self.item3, 'ice cream': item4})
		
	def test_enter_sales_for_day(self):
		""" Text the enter_sales_for_day method """
		self.assertRaises(LemonadeStand.InvalidSalesItemError, self.stand.enter_sales_for_day, {'egg':1})
		self.stand.enter_sales_for_day(self.day0)
		self.assertIs(self.stand._day, 1)
		self.assertEqual(len(self.stand._sales_record), 1)
		
	def test_get_sales_dict_for_day(self):
		""" Text the get_sales_dict_for_day method """
		self.stand.enter_sales_for_day(self.day0)
		self.assertEqual(self.stand.get_sales_dict_for_day(0), self.day0)
		
	def test_sales_of_menu_item_for_day(self):
		""" Text the sales_of_menu_item_for_day method """
		self.stand.enter_sales_for_day(self.day0)
		self.assertEqual(self.stand.sales_of_menu_item_for_day('lemonade'), 8.0)
		
	def test_total_sales_for_menu_item(self):
		""" Text the total_sales_for_menu_item method """
		self.stand.enter_sales_for_day(self.day0)
		self.assertIs(self.stand.total_sales_for_menu_item('lemonade'), 4.5)
		
	def test_total_profit_for_menu_item(self):
		""" Text the total_profit_for_menu_item method """
		self.stand.enter_sales_for_day(self.day0)
		self.assertIs(self.stand.total_profit_for_menu_item(), 1.0)
		
if __name__ == '__main__':
	unittest.main()