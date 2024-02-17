import sqlite3

conn = sqlite3.connect('photos.db')
cursor = conn.cursor()

for i in range(1, 7):
    photo_path = f'/tg bot/photos/{i}.jpg'
    with open(photo_path, 'rb') as file:
        photo_data = file.read()
    cursor.execute("INSERT INTO photos (photo_data) VALUES (?)", (photo_data,))
    conn.commit()

conn.close()
