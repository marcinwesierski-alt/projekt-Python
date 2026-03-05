from datetime import datetime
from rezerwacja_vip import Rezerwacja


def main():
    hotel = Rezerwacja("Python Resort", 5)

    while True:
        print("\n--- SYSTEM HOTELU VIP ---")
        print("1. Pokaż stan pokoi")
        print("2. Zarezerwuj pokój")
        print("3. Zwolnij pokój")
        print("4. Wyjście")

        wybor = input("Wybierz opcję (1-4): ")

        if wybor == "1":
            hotel.pokaz_stan()

        elif wybor == "2":

            # numer pokoju
            try:
                numer = int(input("Podaj numer pokoju: "))
            except ValueError:
                print("❌ Numer pokoju musi być liczbą.")
                continue

            pokoj = hotel.znajdz_pokoj(numer)

            if not pokoj:
                print("❌ Pokój o podanym numerze nie istnieje.")
                continue

            # data od
            try:
                data_od_str = input("Data zameldowania (rrrr-mm-dd): ")
                data_od = datetime.strptime(data_od_str, "%Y-%m-%d")
            except ValueError:
                print("❌ Niepoprawny format daty.")
                continue

            if not pokoj.czy_dostepny(data_od, data_od):
                print("❌ Pokój jest już zarezerwowany w tym terminie.")
                continue

            # data do
            try:
                data_do_str = input("Data wymeldowania (rrrr-mm-dd): ")
                data_do = datetime.strptime(data_do_str, "%Y-%m-%d")
            except ValueError:
                print("❌ Niepoprawny format daty.")
                continue

            if data_do <= data_od:
                print("❌ Data wymeldowania musi być późniejsza niż zameldowania.")
                continue

            # dane gościa dopiero na końcu
            imie = input("Podaj imię: ")
            nazwisko = input("Podaj nazwisko: ")

            hotel.melduj(numer, imie, nazwisko, data_od, data_do)

        elif wybor == "3":
            try:
                numer = int(input("Podaj numer pokoju do zwolnienia: "))
                hotel.wymelduj(numer)
            except ValueError:
                print("❌ Numer pokoju musi być liczbą.")

        elif wybor == "4":
            print("Zamykanie systemu VIP...")
            break

        else:
            print("❌ Niepoprawna opcja. Wybierz 1-4.")


if __name__ == "__main__":
    main()