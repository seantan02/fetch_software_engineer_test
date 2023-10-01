from flask import Blueprint, jsonify, request, make_response
from app.helper import api as apiHelper

api = Blueprint("api", __name__, static_folder=None, template_folder=None)

#To me, I like having a router endpoint where it routes each call to the appropriate handler
#But according to the write-up, I will provide different end point directly
#In production, there will be a lot of security consideration to verify the user who is calling\
#this function is a authorized user
#Ways for security can be a token required for each api call, rate limitation, and more
#We will skip this step here
#ALSO, I am not implementing a relational database here because this is a small application
#For my previos project, I have always utilize MySQL as my database in Flask

@api.route("/add", methods=["POST"])
def add():
    try:
        #Make sure the request is a POST call eventhough Flask already checks it
        assert request.method == "POST", "This endpoint only accepts POST request"
        #We retrive the request data: payer, points, timestamp and we make sure it's not empty
        payer = request.form.get("payer", None)
        points = request.form.get("points", None)
        timestamp = request.form.get("timestamp", None)
        assert payer != None and points != None and timestamp != None, "Payer or Points or Timestamp is empty. They are required to have a value."
        #Define the file path. In this case, it is relative to our folder that contains our app folder because we specified it in our main.py
        data_file_path = "data/user_points.json"
        #Read the user points json file (Supposingly we should read and write in SQL / relational database)
        current_data = apiHelper.read_user_points(data_file_path)
        assert isinstance(current_data, dict), "ERROR: User data was not in dictionary"
        #Make sure everything is right
        #We will convert the timestamp here into datetime object to make things easier
        datetime = apiHelper.convert_timestamp_to_datetime(timestamp, timestamp_format= "%Y-%m-%dT%H:%M:%SZ")
        assert apiHelper.add_user_points(current_data, payer, points, timestamp, datetime) == True, f"System failed to add points to user. Payer: {payer}, Points: {points}, timestamp: {timestamp}"
        assert apiHelper.write_user_points(current_data, data_file_path) == True, "Failed to saved the new updated user points"
        #return a message and status code 200
        return make_response(jsonify({"message":"success"}), 200)
    except Exception as e:
        #return messages and status code 400
        return jsonify({"success":False, "handler_status":str(e)}), 400
    
@api.route("/spend", methods=["POST"])
def spend():
    try:
        #Make sure that it is a POST call
        assert request.method == "POST", "This endpoint only accepts POST request"
        #We retrive the request data: points 
        points = request.form.get("points", None)
        assert points != None, "Points is empty. It is required to have a value."
        #Now we convert points to integer
        points = int(points)
        #Define the file path to our user_points data. In this case, it is relative to our folder that contains our app folder because we specified it in our main.py
        data_file_path = "data/user_points.json"
        #Read the user points json file (Supposingly we should read and write in SQL / relational database)
        #This is not an ideal approach at all for a real-world product
        current_data = apiHelper.read_user_points(data_file_path)
        assert isinstance(current_data, dict), "ERROR: User data was not in dictionary"
        #Ensure our apiHelper have mutated the dictionary in way we wanted
        # assert apiHelper.spend_user_points(current_data, points) == True, "Failed to spend users points."
        current_data, summary = apiHelper.spend_user_points(current_data, points)
        #Ensure our apiHelper have written the latest user points record into the json file
        assert apiHelper.write_user_points(current_data, data_file_path) == True, "Failed to saved the new updated user points"
        #return a message and status code 200
        return make_response(jsonify(summary), 200)
    except Exception as e:
        #return messages and status code 400
        return jsonify({"success":False, "handler_status":str(e)}), 400
    
@api.route("/balance", methods=["GET"])
def balance():
    try:
        #In production, there will be a lot of security consideration to verify the user who is calling\
        #this function is a authorized user
        #Ways for security can be a token required for each api call, rate limitation, and more
        #We will skip this step here
        #ALSO, I am not implementing a relational database here because this is a small application
        #For my previos project, I have always utilize MySQL as my database in Flask
        assert request.method == "GET", "This endpoint only accepts GET request"
        #Define the file path. In this case, it is relative to our folder that contains our app folder because we specified it in our main.py
        data_file_path = "data/user_points.json"
        #Read the user points json file (Supposingly we should read and write in SQL / relational database)
        current_data = apiHelper.read_user_points(data_file_path)
        assert isinstance(current_data, dict), "ERROR: User data was not in dictionary"
        #Make sure everything is right
        balance_summary = apiHelper.summarize_user_points(current_data)
        #return a message and status code 200
        return make_response(jsonify(balance_summary), 200)
    except Exception as e:
        #return messages and status code 400
        return jsonify({"success":False, "handler_status":str(e)}), 400