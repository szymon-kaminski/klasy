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

####################################################
####################################################
class Produkt:
    vat = 0.23

    def __init__(self, nazwa, cena_netto):
        self.nazwa = nazwa
        self.cena_netto = cena_netto

    def cena_brutto(self):
        return self.cena_netto * (1 + Produkt.vat)

    @classmethod
    def zmien_vat(cls, nowy_vat):
        if cls.czy_liczba_dodatnia(nowy_vat):
            cls.vat = nowy_vat
        else:
            print("Vat musi być liczbą dodatnią!")

    @staticmethod
    def czy_liczba_dodatnia(x):
        return isinstance(x, (int, float)) and x > 0

# Przykład użycia:    
produkt1 = Produkt("Mleko", 4.00)
print(f"Brutto: {produkt1.cena_brutto():.2f} zł")

Produkt.zmien_vat(0.1)  # zmieniamy VAT na 10%
print(f"Nowy brutto: {produkt1.cena_brutto():.2f} zł")

Produkt.zmien_vat(-0.5)  # próba ustawienia niepoprawnego VAT