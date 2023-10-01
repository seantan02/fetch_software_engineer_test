import requests

def spend_api_call(points:int):
    url = 'http://localhost:8000/spend'
    data = {"points":points}

    response = requests.post(url, data=data)

    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    return True

assert spend_api_call(5000) == True, "Spend API call was not successful"