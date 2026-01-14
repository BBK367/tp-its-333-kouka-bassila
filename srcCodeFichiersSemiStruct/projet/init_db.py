import sqlite3

conn = sqlite3.connect("database.db")
print("Base ouverte")

conn.execute("""
CREATE TABLE IF NOT EXISTS etudiants (
    nom TEXT,
    addr TEXT,
    pin TEXT
)
""")

print("Table etudiants OK")
conn.close()
