import sqlite3

conn = sqlite3.connect("zadania.db")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS zadania (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nazwa TEXT NOT NULL,
        status TEXT NOT NULL
    )
""")
conn.commit()


def dodaj_zadanie(nazwa, status):
    cursor.execute(
        """
        INSERT INTO zadania (nazwa, status)
        VALUES (?, ?)
    """,
        (nazwa, status),
    )
    conn.commit()
    print(f"Zadanie '{nazwa}' dodane!")


def pokaz_zadania():
    cursor.execute("SELECT * FROM zadania")
    zadania = cursor.fetchall()
    if not zadania:
        print("Brak zadań!")
    for zadanie in zadania:
        print(f"ID: {zadanie[0]} | Nazwa: {zadanie[1]} | Status: {zadanie[2]}")


def zmien_status_zadania(nowy_status, id):
    cursor.execute("UPDATE zadania SET status = ? WHERE id = ?", (nowy_status, id))
    conn.commit()
    print(f"Zadanie nr {id}, zmieniono status na: {nowy_status}")


def usun_zadanie(id):
    cursor.execute("DELETE FROM zadania WHERE id = ?", (id,))
    conn.commit()
    print(f"Zadanie nr {id} usunięte!")


def znajdz_zadanie(id):
    cursor.execute("SELECT * FROM zadania WHERE id = ?", (id,))
    return cursor.fetchone()  # zwraca zadanie lub None
