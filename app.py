from db import (
    dodaj_zadanie,
    pokaz_zadania,
    zmien_status_zadania,
    usun_zadanie,
    znajdz_zadanie,
)


def menu():
    while True:
        print(f"\n--- Lista ToDo---")
        print("1. Wyświetl zadania")
        print("2. Dodaj zadanie")
        print("3. Usuń zadanie")
        print("4. Zmień status zadania")
        print("5. Zamknij")

        try:
            choice = int(input("Wybierz: "))
        except ValueError:
            print("Tylko cyfry")
            continue

        if choice == 1:
            pokaz_zadania()
        elif choice == 2:
            print("--- Dodawanie zadania ---")
            nazwa = input("Zadanie: ")
            print("--- Wybierz status ---")
            print("1. Do wykonania")
            print("2. Wykonane")
            print("3. Cofnij")

            try:
                choice = int(input("Wybierz: "))
            except ValueError:
                print("Tylko cyfry")
                continue

            if choice == 1:
                dodaj_zadanie(nazwa, "Do wykonania")
            elif choice == 2:
                dodaj_zadanie(nazwa, "Wykonane")
            elif choice == 3:
                continue
            else:
                print("Bładne polecenie")

        elif choice == 3:
            print("--- Usuwanie zadania ---")
            try:
                id = int(input("Podaj id zadania: "))
            except ValueError:
                print("Tylko cyfry")
                continue
            if znajdz_zadanie(id):
                usun_zadanie(id)
            else:
                print("Brak zadania o podanym id")
        elif choice == 4:
            print("--- Zmiana statusu zadania ---")
            try:
                id = int(input("Podaj id zadania: "))
            except ValueError:
                print("Tylko cyfry")
                continue
            if znajdz_zadanie(id):
                print("1. Do wykonania")
                print("2. Wykonane")
                try:
                    choice = int(input("Wybierz: "))
                except ValueError:
                    continue
                if choice == 1:
                    zmien_status_zadania("Do wykonania", id)
                elif choice == 2:
                    zmien_status_zadania("Wykonane", id)
                else:
                    print("Tylko cyfry")
                    return
            else:
                print("Brak zadania o podanym id")
        elif choice == 5:
            print("Zamykanie")
            break
        else:
            print("Tylko cyfrey 1-5")
            continue


menu()
