import requests

def balance_api_call():
    url = 'http://localhost:8000/balance'
    response = requests.get(url)
    print(f"Status code: {response.status_code}")
    print(f"Response text: {response.text}")
    return True

assert balance_api_call() == True, "Balance API call unsuccessfull"