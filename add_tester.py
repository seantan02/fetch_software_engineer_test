import requests

def add_points_api_call(payer, points, timestamp):
    url = 'http://localhost:8000/add'
    data = {'payer':payer, "points":points, "timestamp": timestamp}
    response = requests.post(url, data=data)
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    return True

assert add_points_api_call("DANNON", 300, "2022-10-31T10:00:00Z") == True, "API call unsuccessfull"
assert add_points_api_call("UNILEVER", 200, "2022-10-31T11:00:00Z") == True, "API call unsuccessfull"
assert add_points_api_call("DANNON", -200, "2022-10-31T15:00:00Z") == True, "API call unsuccessfull"
assert add_points_api_call("MILLER COORS", 10000, "2022-11-01T14:00:00Z") == True, "API call unsuccessfull"
assert add_points_api_call("DANNON", 1000, "2022-11-02T14:00:00Z") == True, "API call unsuccessfull"