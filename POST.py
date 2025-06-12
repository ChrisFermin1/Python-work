import requests
url = "https://jsonplaceholder.typicode.com/posts"
data = {
    "id": "1",
    "title":"Banned",
    "body": "The shoes that started it all....",
    "brand":"Air Jordan",
    "model":"1"
    }
response = requests.post(url, json=data)
if response.status_code == 201:
    print("Post successful!", response.status_code)
    print(f"Post {data['id']} : {data['title']} : {data['body']} the {data['brand']}  {data['model']}")

else:
    print("Error ", response.status_code)