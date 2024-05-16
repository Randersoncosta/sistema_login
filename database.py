import sqlite3

conn = sqlite3.connect("Sistema.db")

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL ,             
    password TEXT NOT NULL            
)""")

print("Conexão ao banco de dados feito com Sucesso!!!")

conn.commit()