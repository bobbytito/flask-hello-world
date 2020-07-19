# -----Flask Hello World -----#

# import Flask class from the flask package
from flask import Flask

app = Flask(__name__)

# use the decorator pattern to
# link the view function to a url
@app.route("/")
@app.route("/Hello")

def hello_world():
	return "Hello, World!"

# start the development server using the run() method
if __name__ == "__main__":
	app.run()