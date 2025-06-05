import datetime


ksiazki = []
studenci = []
MAX_STUDENTOW = 15
MAX_WYPOZYCZEN = 5

for i in range(1, 26):
    ksiazki.append({
        "id": i,
        "autor": f"Autor {i}",
        "tytul": f"Tytul {i}",
        "rok": 2000 + i % 20,
        "strony": 100 + i,
        "ilosc": 10
    })

def pokaz_ksiazki():
    for ksiazka in ksiazki:
        print(f"{ksiazka['id']}. {ksiazka['tytul']} - {ksiazka['autor']} ({ksiazka['rok']}), stron: {ksiazka['strony']}, dostępne: {ksiazka['ilosc']}")

def dodaj_ksiazke():
    id = len(ksiazki) + 1
    autor = input("Autor: ")
    tytul = input("Tytuł: ")
    rok = int(input("Rok wydania: "))
    strony = int(input("Liczba stron: "))
    ilosc = int(input("Ilość dostępnych egzemplarzy: "))
    ksiazki.append({"id": id, "autor": autor, "tytul": tytul, "rok": rok, "strony": strony, "ilosc": ilosc})

def edytuj_ksiazke():
    pokaz_ksiazki()
    id = int(input("Podaj ID książki do edycji: "))
    for ksiazka in ksiazki:
        if ksiazka['id'] == id:
            ksiazka['autor'] = input("Nowy autor: ")
            ksiazka['tytul'] = input("Nowy tytuł: ")
            ksiazka['rok'] = int(input("Nowy rok wydania: "))
            ksiazka['strony'] = int(input("Nowa liczba stron: "))
            ksiazka['ilosc'] = int(input("Nowa ilość: "))
            print("Zmieniono dane książki.")
            return
    print("Nie znaleziono książki.")

def usun_ksiazke():
    pokaz_ksiazki()
    id = int(input("Podaj ID książki do usunięcia: "))
    global ksiazki
    ksiazki = [k for k in ksiazki if k['id'] != id]
    print("Usunięto książkę.")

def dodaj_studenta():
    if len(studenci) >= MAX_STUDENTOW:
        print("Maksymalna liczba studentów osiągnięta.")
        return
    imie = input("Imię i nazwisko: ")
    studenci.append({"imie": imie, "wypozyczenia": []})
    print("Dodano studenta.")

def wypozycz_ksiazke():
    imie = input("Imię studenta: ")
    student = next((s for s in studenci if s['imie'] == imie), None)
    if not student:
        print("Student nie istnieje.")
        return
    if len(student['wypozyczenia']) >= MAX_WYPOZYCZEN:
        print("Nie można wypożyczyć więcej niż 5 książek.")
        return
    pokaz_ksiazki()
    id = int(input("ID książki do wypożyczenia: "))
    for ks in ksiazki:
        if ks['id'] == id and ks['ilosc'] > 0:
            ks['ilosc'] -= 1
            data_zwrotu = datetime.date.today() + datetime.timedelta(days=14)
            student['wypozyczenia'].append((ks['tytul'], data_zwrotu))
            print(f"Wypożyczono książkę. Zwrot do: {data_zwrotu}")
            return
    print("Nie można wypożyczyć tej książki.")

def raport_przypomnienia():
    print("\n📋 Przypomnienie o zwrotach:")
    dzis = datetime.date.today()
    for student in studenci:
        for tytul, data in student['wypozyczenia']:
            if data < dzis:
                print(f"{student['imie']} - {tytul} przeterminowana (do {data})")

def menu():
    while True:
        print("\n--- MENU ---")
        print("1. Lista książek")
        print("2. Dodaj książkę")
        print("3. Edytuj książkę")
        print("4. Usuń książkę")
        print("5. Dodaj studenta")
        print("6. Wypożycz książkę")
        print("7. Raport przypomnienia")
        print("0. Wyjście")

        wybor = input("Wybierz opcję: ")
if wybor == "1":
     pokaz_ksiazki()
elif wybor == "2":
            dodaj_ksiazke()
elif wybor == "3":
            edytuj_ksiazke()
elif wybor == "4":
            usun_ksiazke()
elif wybor == "5":
            dodaj_studenta()
elif wybor == "6":
            wypozycz_ksiazke()
elif wybor == "7":
            raport_przypomnienia()
elif wybor == "0":
            break
        else:
            print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    menu()
