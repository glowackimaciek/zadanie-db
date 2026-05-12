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


def dodaj_zadanie(conn, cursor, nazwa, status):
    cursor.execute(
        """
        INSERT INTO zadania (nazwa, status)
        VALUES (?, ?)
    """,
        (nazwa, status),
    )
    conn.commit()
    print(f"Zadanie '{nazwa}' dodane!")


def pokaz_zadania(cursor):
    cursor.execute("SELECT * FROM zadania")
    zadania = cursor.fetchall()
    if not zadania:
        print("Brak zadań!")
    for zadanie in zadania:
        print(f"ID: {zadanie[0]} | Nazwa: {zadanie[1]} | Status: {zadanie[2]}")


def zmien_status_zadania(conn, cursor, nowy_status, id):
    cursor.execute("UPDATE zadania SET status = ? WHERE id = ?", (nowy_status, id))
    conn.commit()
    print(f"Zadanie nr {id}, zmieniono status na: {nowy_status}")


def usun_zadanie(conn, cursor, id):
    cursor.execute("DELETE FROM zadania WHERE id = ?", (id,))
    conn.commit()
    print(f"Zadanie nr {id} usunięte!")


dodaj_zadanie(conn, cursor, "Nauka SQLite", "Do zrobienia")
pokaz_zadania(cursor)

dodaj_zadanie(conn, cursor, "Drugie zadanie", "Do zrobienia")
pokaz_zadania(cursor)
zmien_status_zadania(conn, cursor, "Wykonane", 1)
pokaz_zadania(cursor)
usun_zadanie(conn, cursor, 2)
pokaz_zadania(cursor)
