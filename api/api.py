# Import necessary modules from Flask
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Define a route for getting user information by user ID
@app.route("/get-user/<user_id>")
def get_user(user_id):
    user_data = {
        "user_id": user_id,
        "name": "Jhon Doe",
        "email": "jhon.doe@example.com"
    }

    # Check for any extra query parameters in the request
    extra = request.args.get("extra")
    if extra:
        user_data["extra"] = extra  # Add the extra information to the user data if present

    # Return the user data as JSON with a 200 OK status
    return jsonify(user_data), 200


# Define a route for creating a new user with POST method
@app.route("/create-user", methods=["POST"])
def create_user():
    data = request.get_json()  # Get data sent in the request body

    # Return the received data as JSON with a 201 Created status
    return jsonify(data), 201

# Run the Flask application if this script is executed as the main program
if __name__ == '__main__':
    app.run(debug=True)