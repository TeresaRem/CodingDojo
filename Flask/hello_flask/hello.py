from flask import Flask, render_template 

app = Flask(__name__)

@app.route('/')

# @app.route('/success')
# def success():
# 	return render_template('success.html')

def hello_world():
	return render_template('index.html',name="alex")

app.run(debug=True)

# Import Flask to allow us to create our app, and import
# render_template to allow us to render index.html.                                        
# Global variable __name__ tells Flask whether or not we
# are running the file directly or importing it as a module.
# The "@" symbol designates a "decorator" which attaches the
# following function to the '/' route. This means that
# whenever we send a request to localhost:5000/ we will run
# the following "hello_world" function.
# Render the template and return it!
# Run the app in debug mode.
