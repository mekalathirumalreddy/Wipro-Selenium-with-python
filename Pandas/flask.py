import requests

base_url = "https://jsonplaceholder.typicode.com"

# GET users
res = requests.get(base_url + "/users")
print(res.status_code)

# GET single post
res = requests.get(base_url + "/posts/1")
print(res.status_code)

# POST create post
res = requests.post(base_url + "/posts", json={
    "title": "Sample Title",
    "body": "Sample Body",
    "userId": 1
})
print(res.status_code)

# PUT update post
res = requests.put(base_url + "/posts/1", json={
    "title": "Updated Title",
    "body": "Updated Body",
    "userId": 1
})
print(res.status_code)

# DELETE post
res = requests.delete(base_url + "/posts/1")
print(res.status_code)
