from datetime import datetime


class Pokoj:
    def __init__(self, numer: int, cena: float = 100.0):
        self.numer = numer
        self.cena = cena
        self.rezerwacje = []

    def czy_dostepny(self, data_od, data_do):
        for rez in self.rezerwacje:
            if not (data_do <= rez["data_od"] or data_od >= rez["data_do"]):
                return False
        return True

    def zarezerwuj(self, gosc, data_od, data_do):

        if data_do <= data_od:
            print("❌ Data wymeldowania musi być późniejsza niż zameldowania.")
            return False

        if not self.czy_dostepny(data_od, data_do):
            print("❌ Pokój jest zajęty w podanym terminie.")
            return False

        self.rezerwacje.append({
            "gosc": gosc,
            "data_od": data_od,
            "data_do": data_do
        })

        self.rezerwacje.sort(key=lambda x: x["data_od"])
        return True

    def zwolnij(self):

        dzis = datetime.today()

        for rez in self.rezerwacje:
            if rez["data_od"] <= dzis < rez["data_do"]:
                rez["data_do"] = dzis
                return True

        return False

    def aktualna_rezerwacja(self):
        dzis = datetime.today()

        for rez in self.rezerwacje:
            if rez["data_od"] <= dzis < rez["data_do"]:
                return rez

        return None

    def koszt_pobytu(self, data_od, data_do):
        dni = (data_do - data_od).days
        return dni * self.cena

    def __repr__(self):

        dzis = datetime.today()

        status = "WOLNY"
        if self.aktualna_rezerwacja():
            status = "ZAJĘTY"

        tekst = f"\nPokój nr {self.numer}\n"
        tekst += f"Cena za noc: {self.cena} zł\n"
        tekst += f"Status: {status}\n"

        if not self.rezerwacje:
            tekst += "Brak rezerwacji\n"
            return tekst

        tekst += "\nRezerwacje:\n"

        for rez in self.rezerwacje:

            if rez["data_od"] <= dzis < rez["data_do"]:
                ozn = "AKTUALNA"
            elif rez["data_od"] > dzis:
                ozn = "PRZYSZŁA"
            else:
                ozn = "ZAKOŃCZONA"

            koszt = self.koszt_pobytu(rez["data_od"], rez["data_do"])

            tekst += (
                f"\n  Gość: {rez['gosc']}\n"
                f"  Termin: {rez['data_od'].date()} - {rez['data_do'].date()}\n"
                f"  Status rezerwacji: {ozn}\n"
                f"  Koszt pobytu: {koszt} zł\n"
            )

        return tekst
