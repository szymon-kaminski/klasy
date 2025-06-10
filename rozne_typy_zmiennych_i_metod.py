class Pracownik:
    firma = "tech corp"

    def __init__(self, imie):
        self.imie = imie

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} z firmy {self.firma}")


    @classmethod
    def zmien_firme(cls, nowa_firma):
        cls.firma = nowa_firma

    @staticmethod
    def przywitaj():
        print("Witamy w firmie!")


p1 = Pracownik("Anna")
p2 = Pracownik("Szymon")

p1.przedstaw_sie()

Pracownik.zmien_firme("Microsoft")
p2.przedstaw_sie()

Pracownik.przywitaj()