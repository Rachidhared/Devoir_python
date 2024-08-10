import sqlite3

conn = sqlite3.connect('ecole.db')
connexion = conn.cursor()

connexion.execute('''
CREATE TABLE IF NOT EXISTS eleves (
    id INTEGER PRIMARY KEY,
    nom TEXT,
    prenom TEXT,
    age INTEGER
)''')

conn.commit()

connexion.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('Mao', 'Imran', 24))
connexion.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('Abdoul', 'Filsan', 20))
connexion.execute("INSERT INTO eleves (nom, prenom, age) VALUES (?, ?, ?)", ('Awwa', 'Ayoub', 23))

conn.commit()

connexion.execute("UPDATE eleves SET age = ? WHERE id = ?", (26, 2))

conn.commit()

connexion.execute("SELECT * FROM eleves")
print("Tous les enregistrements :")
print(connexion.fetchall())

connexion.execute("SELECT nom, prenom, age FROM eleves WHERE age > 23")
print("\nElèves de plus de 23 ans :")
print(connexion.fetchall())

conn.close()
