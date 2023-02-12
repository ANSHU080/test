# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
import json

from flask import Flask
import requests
# import json

# Flask constructor takes the name of
# current module (__name__) as argument.
app = Flask(__name__)

# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# @app.route('/')
# # ‘/’ URL is bound with hello_world() function.
# def hello_world():
# 	link = "https://f3e3b133-50ee-40c1-ab73-e84d69ac7c58.mock.pstmn.io/cust-add"
# 	f = requests.get(link)
# 	a = (f.json())
@app.route('/cust-add/<id>')
def cust_add(id):
	link = "https://f3e3b133-50ee-40c1-ab73-e84d69ac7c58.mock.pstmn.io/cust-add"
	f = requests.get(link)
	a = (f.json())
	for i in range(len(a)):
		for key in a[i]:
			if key == "addressID" and str(a[i][key])==id:
				return a[i]

# main driver function
if __name__ == '__main__':

	# run() method of Flask class runs the application
	# on the local development server.
	app.run()
