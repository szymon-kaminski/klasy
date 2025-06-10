class Zwierze:
    def dzwiek(self):
        print("Dzwięk zwierzęcia")


class Pies(Zwierze):
    def dzwiek(self):
        super().dzwiek()
        print("Hau hau!")

def main():
    pies = Pies()
    pies.dzwiek()

if __name__ == "__main__":
    main()

class Osoba:
    def __init__(self, imie):
        self.imie = imie
        print(f"Tworzę osobę: {self.imie}")

class Pracownik(Osoba):
    def __init__(self, imie, zawod):
        super().__init__(imie)
        self.zawod = zawod
        print(f"Zawód: {self.zawod}")

def main():
    p = Pracownik("Szymon", "programista")

if __name__ == "__main__":
    main()


class Pojazd:
    def __init__(self, nazwa):
        self.nazwa = nazwa
        print(f"Pojazd: {self.nazwa}")

class Motocykl(Pojazd):
    def __init__(self, nazwa, silnik):
        super().__init__(nazwa)
        self.silnik = silnik
        print(f"Silnik: {self.silnik}")

def main():
    m = Motocykl("Yamaha R1", "spalinowy")

if __name__ == "__main__":
    main()
        