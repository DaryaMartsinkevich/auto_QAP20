import requests


users = requests.get("https://9f95-188-123-155-41.ngrok-free.app/users")
print(users.json())
data = {"name": "Charlie", "email": "charlie@example.com"}
headers = {"Content-Type": "application/json"}
response = requests.post("https://9f95-188-123-155-41.ngrok-free.app/users", json=data, headers=headers)
print(response.json())
created_user = dict(response.json())
user_id = created_user.get('id')
print(user_id)
data_update = {"name": "Charlie",
               "email": "charlie@example.com",
               "job": "QA Engineer",
               "update": "TRUE"
               }
response_update = requests.put(f"https://9f95-188-123-155-41.ngrok-free.app/users/{user_id}", json=data_update, headers=headers)
print(response_update.json())
response_delete = requests.delete(f"https://9f95-188-123-155-41.ngrok-free.app/users/{user_id}")
print(response_delete.status_code)
check_user = requests.get(f"https://9f95-188-123-155-41.ngrok-free.app/{user_id}")
print(check_user.status_code)