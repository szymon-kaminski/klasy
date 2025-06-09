class Osoba:
    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek


    def przedstaw_sie(self):
        print(f"Cześć, mam na imię {self.imie} i mam {self.wiek} lat.")


class Pracownik(Osoba):
    def __init__(self, imie, wiek, stanowisko):
        super().__init__(imie, wiek)
        self.stanowisko = stanowisko


    def przedstaw_sie(self):
        super().przedstaw_sie()
        print(f"Pracuję jako {self.stanowisko}.")


def main():
    osoba = Osoba("Anna", 30)
    osoba.przedstaw_sie()

    pracownik = Pracownik("Jan", 30, "programista")
    pracownik.przedstaw_sie()

if __name__ == "__main__":
    main()

print()


class Zwierze:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    
    def dzwiek(self):
        print(f"To jest zwierze.")


class Pies(Zwierze):
    def __init__(self, gatunek, rasa):
        super().__init__(gatunek)
        self.rasa = rasa

    
    def dzwiek(self):
        super().dzwiek()
        print(f"hau hau! Jestem {self.rasa}, czyli {self.gatunek}.")


def main():
    zwierze = Zwierze("pies")
    zwierze.dzwiek()

    pies = Pies("pies", "jamnik")
    pies.dzwiek()

if __name__ == "__main__":
    main()