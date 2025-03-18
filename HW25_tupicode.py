import requests


url_typicode = 'https://jsonplaceholder.typicode.com/'

# Получить 80-й пост
response_post = requests.get(f'{url_typicode}/posts/80')
print(response_post.json())

# ПОлучить все комментарии к посту 60
response_comments = requests.get(f'{url_typicode}/comments/60')
print(response_comments.json())

# Создать новый пост
new_post = {
    "userId": 101,
    "id": 101,
    "title": "new post",
    "body": "new post"
}
response_new_post = requests.post(f"{url_typicode}/posts", json=new_post)
print(response_new_post.json())

# Удалить пост 7
responce_delete = requests.delete(f"{url_typicode}/posts/7")
print(responce_delete.status_code)
