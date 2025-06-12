
import requests
url = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(url)
if response.status_code == 200:
    posts = response.json()
    for post in posts [:3]:
        print(f" Post {post ['Id']}: {post ['Title']}")
else:
    print("Error ", response.status_code)

