from flask import Flask, render_template, request, jsonify # Importing necessary Flask modules
import json  # For reading/writing JSON data
import webbrowser  # To open the URL in the browser
import threading  # To open the browser after a delay
import socket  # To get the local IP address
from datetime import datetime  # For handling date and time
import calendar  # For working with the calendar

app = Flask(__name__)  # Create a Flask application instance

DATA_FILE = "data.json"  # The file where assessment data is stored

# Function to load data from the JSON file
def load_data(): 
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)  # Return data as a dictionary
    except (FileNotFoundError, json.JSONDecodeError):  # Handle file not found or JSON errors
        return []  # Return an empty list if no data or if there's an error

# Function to save the updated data to the JSON file
def save_data(data): 
    with open(DATA_FILE, "w") as file:
        json.dump(data, file, indent=4)  # Write data to the file in a formatted way

# Main route for the home page
@app.route("/")
def home():  
    today = datetime.now().date()  # Get today's date
    y, m = today.year, today.month  # Extract the current year and month
    assessments = load_data()  # Load assessments from the file
    assessment_dates = {a["date"] for a in assessments}  # Create a set of assessment dates
    cal = calendar.monthcalendar(y, m)  # Generate the calendar for the current month
    colored_calendar = []  # List to store colored calendar days

    for week in cal:  # Loop through each week in the calendar
        row = []
        for day in week:  # Loop through each day in the week
            if day == 0:
                row.append("")  # Append empty string for non-existent days
                continue

            date_str = f"{day:02d}-{m:02d}-{y}"  # Format the date as DD-MM-YYYY
            day_date = datetime(y, m, day).date()  # Create a date object for comparison

            # Determine the color based on the date
            if date_str in assessment_dates:
                color = "cyan"  # Assessments are marked with cyan
            elif day_date < today:
                color = "red"  # Past days are marked with red
            elif day_date == today:
                color = "green"  # Today is marked with green
            else:
                color = "yellow"  # Future days are marked with yellow

            row.append({"day": day, "color": color})  # Add day and color to the row
        colored_calendar.append(row)  # Add the week to the calendar

    return render_template("index.html", calendar=colored_calendar, assessments=assessments)  # Render the HTML template with the data

# Route to add a new assessment
@app.route("/add", methods=["POST"])
def add_assessment():
    data = request.json  # Get the JSON data from the request
    try:
        datetime.strptime(data["date"], "%d-%m-%Y")  # Validate the date format (DD-MM-YYYY)
        assessments = load_data()  # Load the current assessments
        assessments.append(data)  # Add the new assessment
        save_data(assessments)  # Save the updated assessments
        return jsonify({"message": "Assessment added!"}), 200  # Respond with a success message
    except ValueError:
        return jsonify({"error": "Invalid date format! Use DD-MM-YYYY"}), 400  # Return error if date is invalid

# Route to delete a specific assessment
@app.route("/delete", methods=["POST"])
def delete_assessment(): 
    data = request.json  # Get the JSON data from the request
    assessments = load_data()  # Load the current assessments
    assessments = [a for a in assessments if a["date"] != data["date"]]  # Filter out the assessment to delete
    save_data(assessments)  # Save the updated assessments
    return jsonify({"message": "Assessment deleted!"}), 200  # Respond with a success message

# Route to delete all assessments
@app.route("/delete_all", methods=["POST"])
def delete_all(): 
    save_data([])  # Clear the data by saving an empty list
    return jsonify({"message": "All assessments deleted!"}), 200  # Respond with a success message

# Function to get the local IP address for LAN hosting
def get_local_ip(): 
    hostname = socket.gethostname()  # Get the hostname of the machine
    return socket.gethostbyname(hostname)  # Return the local IP address

# Function to open the browser with the local server URL
def open_browser(): 
    ip = get_local_ip()  # Get the local IP address
    url = f"http://{ip}:5000/"  # Construct the URL to access the app
    webbrowser.open(url)  # Open the URL in the web browser

# Main block to run the app
if __name__ == '__main__': 
    threading.Timer(1.5, open_browser).start()  # Delay opening the browser to ensure the server starts
    app.run(host="0.0.0.0", port=5000, debug=True)  # Run the app on all available IPs, port 5000
