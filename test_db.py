from db import (
    dodaj_zadanie,
    pokaz_zadania,
    znajdz_zadanie,
    usun_zadanie,
    cursor,
    zmien_status_zadania,
)


def test_dodaj_zadanie():
    dodaj_zadanie("Test zadanie", "Do wykonania")
    cursor.execute("SELECT * FROM zadania ORDER BY id DESC LIMIT 1")
    zadanie = cursor.fetchone()
    assert zadanie is not None
    assert zadanie[1] == "Test zadanie"


def test_usun_zadanie():
    dodaj_zadanie("Do usuniecia", "Do wykonania")
    cursor.execute("SELECT * FROM zadania ORDER BY id DESC LIMIT 1")
    zadanie = cursor.fetchone()
    id = zadanie[0]
    usun_zadanie(id)
    assert znajdz_zadanie(id) is None


def test_zmien_status():
    dodaj_zadanie("Test statusu", "Do wykonania")
    cursor.execute("SELECT * FROM zadania ORDER BY id DESC LIMIT 1")
    zadanie = cursor.fetchone()
    id = zadanie[0]
    zmien_status_zadania("Wykonane", id)
    zaktualizowane = znajdz_zadanie(id)
    assert zaktualizowane[2] == "Wykonane"
