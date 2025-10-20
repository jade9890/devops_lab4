import unittest
from calculate import Calculations

class TestEachCalculation(unittest.TestCase):
	
	def setUp(self):  #constructor? not quite. it tests a new copy of the data every time u test
		self.nums = Calculations(10, 2)
	
	def test_sum(self):
		self.assertEqual(self.nums.get_sum(), 12, 'The sum is wrong.')

	def test_difference(self):
		self.assertEqual(self.nums.get_difference(), 8, 'The difference is wrong')

	def test_product(self): 
		self.assertEqual(self.nums.get_product(), 20, 'The product is wrong.') 

 
	def test_quotient(self): 
		self.assertEqual(self.nums.get_quotient(), 5, 'The quotient is wrong.')

if __name__ == '__main__':
	unittest.main()
