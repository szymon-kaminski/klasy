class Zwierze:
    def __init__(self, gatunek):
        self.gatunek = gatunek

    
    def dzwiek(self):
        print("To jest ogólny dzwiek zwierzecia.")


class Kot(Zwierze):
    def __init__(self, rasa):
        super().__init__("kot")
        self.rasa = rasa

    
    def dzwiek(self):
        print("Miau!")


class Papuga(Zwierze):
    def __init__(self, imie):
        super().__init__("papuga")
        self.imie = imie

    
    def dzwiek(self):
        print(f"{self.imie} mowi: 'Czesc!'")

def main():
    zwierzeta = [
        Kot("perski"),
        Papuga("Polly")
    ]

    for z in zwierzeta:
        print(f"Typ: {type(z)}")
        z.dzwiek()


if __name__ == "__main__":
    main()

class Robot:
    def dzialaj(self):
        print("Działam mechanicznie!")

class Czlowiek:
    def dzialaj(self):
        print("Myślę, więc jestem.")

class Android(Robot, Czlowiek):
    pass

def main():
    android = Android()
    android.dzialaj()  # Co się wypisze?

if __name__ == "__main__":
    main()