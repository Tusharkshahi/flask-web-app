# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/") that returns the desired message
@app.route('/')
def hello():
    return 'Hello, Azure Web Apps!'

# Run the application if this script is executed
if __name__ == '__main__':
    app.run(debug=True)
