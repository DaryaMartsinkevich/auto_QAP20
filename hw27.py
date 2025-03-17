import sqlite3

from requests import delete

# Подключаемся к SQLite (или создаем новый файл БД)
conn = sqlite3.connect("darya_hw.db")
cursor = conn.cursor()

# Вывод всех пользователей
cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()
print("Пользователи в базе данных:")
for row in rows:
    print(row)

# Добавляем нового пользователя
new_user = ("Darya", "darya@example.com", 33, "Poland")
cursor.execute("INSERT INTO users (name, email, age, country) VALUES (?, ?, ?, ?)", new_user)
conn.commit()

# Проверяем, что пользователь добавлен
cursor.execute("SELECT * FROM users WHERE name = 'Darya';")
user_in_db = cursor.fetchone()
print(f"Добавлен пользователь {user_in_db}")

# Удаляем пользователя после теста
cursor.execute("DELETE FROM users WHERE name = 'Darya';",)
conn.commit()

# Проверяем, что пользователь удален
cursor.execute("SELECT * FROM users WHERE name = 'Darya';",)
delete_user = cursor.fetchone()

# Закрываем соединение
conn.close()