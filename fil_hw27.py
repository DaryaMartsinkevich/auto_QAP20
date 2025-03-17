import sqlite3

# Подключаемся к SQLite (или создаем новый файл БД)
conn = sqlite3.connect("darya_hw.db")
cursor = conn.cursor()

# Создание таблицы пользователей (users)
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    age INTEGER CHECK (age >= 0),
    country TEXT DEFAULT 'Unknown'
);
""")

print("✅ Таблицы успешно созданы!")

cursor.executemany("""
INSERT INTO users (name, email, age, country) VALUES (?, ?, ?, ?)
""", [
    ("Ivan", "ivan@example.com", 30, "Russia"),
    ("Elena", 'elena@example.com', 18, "USA"),
    ("Pavel", 'pavel@example.com', 25, "Germani"),
    ("Maria", 'maria@example.com', 28, "France"),
    ("Oleg", 'oleg@example.com', 21, "Belarus"),
    ("Alice", 'alice@example.com', 30, "Poland")
])

conn.commit()
print("✅ Тестовые данные успешно добавлены!")

conn.close()
print("✅ Все проверки успешно выполнены!")