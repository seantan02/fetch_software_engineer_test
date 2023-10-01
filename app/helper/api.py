import json
import random
from datetime import datetime

def read_user_points(filepath = "/data/user_points.json") -> dict:
    with open(filepath, "r", encoding="utf-8") as file:
        data = json.load(file)

    return data

def write_user_points(data:dict, filepath) -> bool:
    with open(filepath, "w") as file:
        json.dump(data, file)

    return True

def generate_unique_id(user_points) -> int:
    unique_id = random.randint(10**8, (10**9)-1)
    
    while unique_id in user_points:
        unique_id = random.randint(10**8, (10**9)-1)

    return unique_id

def add_user_points(user_points:dict, payer, points_to_add:int, timestamp, datetime) -> bool:
    assert isinstance(user_points, dict), "User points data provided is not a dictionary"
    id = generate_unique_id(user_points)
    #Now we have generate a unique ID for each adding
    #Let's add it to the dictionary
    user_points[id] = dict()
    user_points[id]["payer"] = payer
    user_points[id]["points"] = points_to_add
    user_points[id]["timestamp"] = timestamp
    user_points[id]["datetime"] = datetime

    return True

def spend_user_points(user_points:dict, points_to_spend:int) -> bool:
    """
    This method spends user's points given there's sufficient points. Oldest points will be spent and no payer will have negative value.
    :param user_points: The user's points dictionary data
    :param points_to_spend: The amount we are spending
    :return: Updated user's points dictionary, list of summary; Raise exception if there's insufficient points.
    """

    assert isinstance(user_points, dict), "User points data provided is not a dictionary"
    #We have 2 conditions for spending given there's sufficient total points
    #1. Spend the oldest first
    #2. No payer should have negative amount
    #Given our implementation is that it is a dictionary that contains all information
    #We will first loop through the dictionary and create some arrays
    total_points = 0
    id_in_datetime_order = list()
    summary = list()
    for id in user_points:
        record = user_points[id]
        #Now we want to add payer's record sorted in oldest to latest to a list
        #We also wants a total point in the end to check if spending > total
        payer = record["payer"]
        points = int(record["points"])
        date = record["datetime"]
        #Only if the points added are positive, else we ignore it
        if points > 0:
            #Convert date to datetime object
            date = convert_string_to_datetime(date, datetime_format="%Y-%m-%d %H:%M:%S")
            id_in_datetime_order.append([id, date])
        #Add to total
        total_points += points
    #Sort the datetime in order
    id_in_datetime_order = sorted(id_in_datetime_order, key=lambda val : val[1])
    #Now we do have a list of ids in descending order of datetime
    #Now we also have a total points
    #So let's implement it
    #Case 1) Not enough points
    if points_to_spend > total_points:
        raise Exception("User does not have enought points.")
    #Case 2) We have enough points and we spend it
    else:
        for value in id_in_datetime_order:
            id = value[0]
            this_user_points = int(user_points[id]["points"])
            payer = user_points[id]["payer"]
            #If this_user_points == 0 we ignore it
            if this_user_points <= 0:
                continue
            #If points to spend is more than or equal
            if points_to_spend >= this_user_points:
                points_to_spend -= this_user_points
                user_points[id]["points"] = 0
                summary.append({"payer":payer, "points": -this_user_points})
            else:
                user_points[id]["points"] = (this_user_points - points_to_spend)
                summary.append({"payer":payer, "points": -points_to_spend})
                points_to_spend = 0
                break

    return user_points, summary

def summarize_user_points(user_points:dict)->dict:
    #We define a variable of dict we returning
    summary = dict()
    #We loop through the dictionary and retrieve all points
    for id in user_points:
        user_point = user_points[id]
        this_user_point = int(user_point["points"])
        this_payer = user_point["payer"]
        if this_payer in summary:
            summary[this_payer] += this_user_point
        else:
            summary[this_payer] = this_user_point

    return summary

#Datetime functions
def convert_timestamp_to_datetime(timestamp_str, timestamp_format):
    # Parse the string and convert it to a datetime object
    datetime_obj = datetime.strptime(timestamp_str, timestamp_format)
    formatted_datetime_str = datetime_obj.strftime("%Y-%m-%d %H:%M:%S")
    return formatted_datetime_str

def convert_string_to_datetime(string, datetime_format):
    # Parse the string and convert it to a datetime object
    datetime_obj = datetime.strptime(string, datetime_format)

    return datetime_obj