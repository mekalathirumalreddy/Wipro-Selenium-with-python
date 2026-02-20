#1. Write a Python script to send a GET request to https://jsonplaceholder.typicode.com/users and print only name and email.
import requests

try:
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    print(response)
    if response.status_code==200:
        print("Status code is 200 ok")
        data=response.json()
        for i in data:
            print(f"Name: {i['name']},Email:{i['email']}")
    else:
        print(f"An Error{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An Error{e}")

#2. Send a GET request with query parameter userId=2 and print number of posts returned.

import requests

try:
    response=requests.get("https://jsonplaceholder.typicode.com/posts?userId=2")
    print(response)
    if response.status_code==200:
        print("Status code is 200 ok")
        posts=response.json()
        print(len(posts))
    else:
        print(f"An Error{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An Error{e}")


#3. Write a POST request to create a new resource and verify status code 201.

import requests

try:
    data={
   "name": "Apple MacBook Pro 16",
   "data": {
      "year": 2019,
      "price": 1849.99,
      "CPU model": "Intel Core i9",
      "Hard disk size": "1 TB"
   }
}
    response=requests.post("https://jsonplaceholder.typicode.com/users",json=data)
    print(response)
    if response.status_code==201:
        print("Status code is 201 ok")
        data=response.json()
        print(data)
    else:
        print(f"An Error{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An Error{e}")


#4. Explain the difference between data= and json= in requests.post().
#5. Write code to check if response status code is not 200 and raise an exception.

import requests

try:
    response=requests.get("https://jsonplaceholder.typicode.com/user")
    print(response)
    if response.status_code==200:
        print("Status code is 200 ok")
        data=response.json()
        for i in data:
            print(f"Name: {i['name']},Email:{i['email']}")
    else:
        print(f"An Error{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An Error{e}")


#6. Fetch all users and print usernames in uppercase.

import requests

try:
    response=requests.get("https://jsonplaceholder.typicode.com/users")
    if response.status_code==200:
        print("Status code is 200 ok")
        data=response.json()
        for i in data:
            print(f"Name: {str(i['username'].upper())}")
    else:
        print(f"An Error{response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"An Error{e}")


#7. Implement timeout handling (2 seconds) and catch Timeout exception.
import requests
from requests.exceptions import Timeout

try:
    response = requests.get("https://jsonplaceholder.typicode.com/users",timeout=2)

    if response.status_code == 200:
        print("Request successful")
    else:
        print(f"Error: {response.status_code}")

except Timeout:
    print("Request timed out after 2 seconds")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")


#8. Use Session object to send multiple requests and demonstrate cookie persistence.

import requests

# Create a session object
session = requests.Session()

# First request → server sets a cookie
response1 = session.get("https://httpbin.org/cookies/set/user/reddy")

print("Response 1 cookies:")
print(response1.cookies)

# Second request → cookie is automatically sent
response2 = session.get("https://httpbin.org/cookies")

print("\nResponse 2 cookies (persisted):")
print(response2.json())

