import unittest #pythons built in testing
from app import app #imports the Flask app object I made from app.py

class TestAppSmoke(unittest.TestCase): #Define test class that inherits from unittest.TestCase
	
	def setUp(self): 
		app.testing = True #puts Flask in testing mode
		self.client = app.test_client() #create a fake browser



#Test #1 Home route status
#sends a GET request to / (homepage)
#response.status_code gives the HTTP staatus (200 = OK, 404 = not found)
#Asserts that response should be 200 (meaning it loaded successfully)
#Basically it checks that the Flask route exists and works

	def test_home_route(self):
		response = self.client.get("/") 
        	self.assertEqual(response.status_code, 200) 


#test #2 check message content
#Sends another GET request to /
#response.data is the raw HTML returned by Flask
#b"..." checks that "Hello, Welcome to Lab 4!" is acc inside the returned page
#this makes sure my app returns the expected test content

    	def test_message(self): 
        	response = self.client.get("/") 
        	self.assertIn(b"Hello, Welcome to Lab 4", response.data) 

 #below is saying, run the tests if this file is executed directly
#When I run python test_app.py

if __name__ == "__main__": 
    unittest.main()
