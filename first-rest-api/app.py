import os
import psycopg2
from datetime import datetime, timezone
from dotenv import load_dotenv
from flask import Flask, request, jsonify

# SQL query to create a table for rooms if it doesn't exist
CREATE_ROOMS_TABLE = "CREATE TABLE IF NOT EXISTS rooms (id SERIAL PRIMARY KEY, name TEXT);"

# SQL query to create a table for temperatures if it doesn't exist, with a foreign key to rooms
CREATE_TEMPS_TABLE = """CREATE TABLE IF NOT EXISTS temperatures (
    id SERIAL PRIMARY KEY,
    room_id INTEGER,
    temperature REAL,
    date TIMESTAMP,
    FOREIGN KEY(room_id) REFERENCES rooms(id) ON DELETE CASCADE
);"""

# SQL query to insert a new room and return its ID
INSERT_ROOM_RETURN_ID = "INSERT INTO rooms (name) VALUES (%s) RETURNING id;"

# SQL query to insert a new temperature record
INSERT_TEMP = "INSERT INTO temperatures (room_id, temperature, date) VALUES (%s, %s, %s);"

# SQL query to count the number of distinct days with temperature records
GLOBAL_NUMBER_OF_DAYS = "SELECT COUNT(DISTINCT DATE(date)) AS days FROM temperatures;"

# SQL query to calculate the global average temperature
GLOBAL_AVG = "SELECT AVG(temperature) AS average FROM temperatures;"

# Load environment variables from a .env file
load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)

@app.route("/api/room", methods=["POST"])
def create_room():
    # Extract the room name from the request body
    data = request.get_json()
    name = data.get("name")
    if not name:
        # Return an error if the name is not provided
        return jsonify({"error": "Name is required."}), 400

    with connection:
        with connection.cursor() as cursor:
            # Create the rooms table if it doesn't exist and insert the new room
            cursor.execute(CREATE_ROOMS_TABLE)
            cursor.execute(INSERT_ROOM_RETURN_ID, (name, ))
            room_id = cursor.fetchone()[0]

    # Return the ID of the newly created room
    return jsonify({"id": room_id, "message": f"Room {name} created."}), 201

@app.route("/api/temperature", methods=["POST"])
def add_temp():
    # Extract temperature, room ID, and date from the request body
    data = request.get_json()
    temperature = data.get("temperature")
    room_id = data.get("room")
    date_str = data.get("date")

    if not all([temperature, room_id]):
        # Return an error if temperature or room ID is not provided
        return jsonify({"error": "Temperature and room ID are required."}), 400

    try:
        # Parse the date string or use the current time if not provided
        date = datetime.strptime(date_str, "%m-%d-%Y %H:%M:%S") if date_str else datetime.now(timezone.utc)
    except ValueError:
        # Return an error if the date format is invalid
        return jsonify({"error": "Invalid date format. Use 'MM-DD-YYYY HH:MM:SS'."}), 400

    with connection:
        with connection.cursor() as cursor:
            # Create the temperatures table if it doesn't exist and insert the new temperature record
            cursor.execute(CREATE_TEMPS_TABLE)
            cursor.execute(INSERT_TEMP, (room_id, temperature, date))

    # Confirm the addition of the new temperature record
    return jsonify({"message": "Temperature added."}), 201

@app.route("/api/average", methods=["GET"])
def get_global_avg():
    with connection:
        with connection.cursor() as cursor:
            # Calculate the global average temperature and the number of days with records
            cursor.execute(GLOBAL_AVG)
            average = cursor.fetchone()[0]
            cursor.execute(GLOBAL_NUMBER_OF_DAYS)
            days = cursor.fetchone()[0]

    # Return the global average temperature and the number of days
    return jsonify({"average": round(average, 2), "days": days})

