import unittest #pythons own testing

from app import app  #import our web app

 

class TestAppSmoke(unittest.TestCase): #create a class thats inherited from unittest

 

    def setUp(self):  #for the set up, puts app in testing most and makes a fake browse

        app.testing = True 

        self.client = app.test_client() 

 

    def test_home_route(self): #get request for the homepage (/), asserts that response should be 200 (http status) meaning it loaded successfully (not 404)

        response = self.client.get("/") 

        self.assertEqual(response.status_code, 200) 

    def test_message(self): #get request to / , compare bytes and checks the string is inside the returned page

        response = self.client.get("/") 

        self.assertIn(b"Hellooooooo, Welcome to Lab 4", response.data) 

 

if __name__ == "__main__": 

    unittest.main() 
