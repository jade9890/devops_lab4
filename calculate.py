class Calculations:
	def __init__(self, a, b): #constructor
		self.a = a #self is basically 'this'
		self.b = b

	def get_sum(self):
		return self.a + self.b

	def get_difference(self):
		return self.a - self.b

	def get_product(self):
		return self.a * self.b

	def get_quotient(self):
		return self.a / self.b

if __name__ == '__main__': #start here
	nums = Calculations(10,2) #object
	print("Sum:",nums.get_sum())
	print("Difference:",nums.get_difference())
	print("Product:",nums.get_product())
	print("Quotient:",nums.get_quotient())
