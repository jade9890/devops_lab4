#running a smoke test

from flask import Flask # imports Flask class from flask library

app = Flask(__name__) #creates an instance of Flask app 
#so app is my main web application object

@app.route("/") #route decorator, so / (root URL) is what triggers the function
def home():
	return "Hello, Welcome to lab 4! This is running on the local server " #home function returns a string

if __name__=="__main__":
	app.run(host="0.0.0.0", port=5000) 

#this means the code only runs if u run this file directly
#app.run(...) starts Flask dev server
#host="0.0.0.0" means it listens on all network interfaces
#port 5000 specifies the port number
