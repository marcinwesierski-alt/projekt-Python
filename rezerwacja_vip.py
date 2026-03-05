from pokoj_vip import Pokoj
from gosc_vip import Gosc


class Rezerwacja:

    def __init__(self, nazwa_hotelu: str, liczba_pokoi: int):
        self.nazwa_hotelu = nazwa_hotelu
        self.pokoje = []

        for i in range(1, liczba_pokoi + 1):
            self.pokoje.append(Pokoj(i))

    def znajdz_pokoj(self, numer: int):
        for pokoj in self.pokoje:
            if pokoj.numer == numer:
                return pokoj
        return None

    def pokaz_stan(self):

        print(f"\n=== {self.nazwa_hotelu} ===")

        for pokoj in self.pokoje:
            print("-" * 40)
            print(pokoj)

        print("-" * 40)

    def melduj(self, numer: int, imie: str, nazwisko: str, data_od, data_do):

        pokoj = self.znajdz_pokoj(numer)

        if not pokoj:
            print("❌ Nie ma takiego pokoju!")
            return

        gosc = Gosc(imie, nazwisko)

        if pokoj.zarezerwuj(gosc, data_od, data_do):

            koszt = pokoj.koszt_pobytu(data_od, data_do)

            print("✅ Rezerwacja zakończona sukcesem!")
            print(f"💰 Koszt pobytu: {koszt} zł")

        else:
            print("❌ Nie udało się zarezerwować pokoju.")

    def wymelduj(self, numer: int):

        pokoj = self.znajdz_pokoj(numer)

        if not pokoj:
            print("❌ Nie ma takiego pokoju!")
            return

        if pokoj.zwolnij():
            print("Pokój został zwolniony.")
        else:
            print("Pokój był już wolny.")
