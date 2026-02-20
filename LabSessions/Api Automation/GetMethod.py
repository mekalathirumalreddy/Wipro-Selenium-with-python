import requests

try:
    #make a get request to api endpoint
    response = requests.get("https://api.restful-api.dev/objects")
    print(response)
#check if type is 200 k
    if response.status_code==200:
        print("Status code is 200k")
        #prase the json file
        data = response.json()
        print(data)
    else:print(f"Error : recevied status code:{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An error occurred:{e}")