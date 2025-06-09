class Zwierze:
    def dzwiek(self):
        print("Dzwiek zwierzecia")


class Kot(Zwierze):
    def dzwiek(self):
        print("Miau!")


class Pies(Zwierze):
    def dzwiek(self):
        super().dzwiek()
        print("Hau hau!")


def main():
    z = Zwierze()
    z.dzwiek()

    k = Kot()
    k.dzwiek()

    p = Pies()
    p.dzwiek()


if __name__ == "__main__":
    main()

print()

class Samochod:
    def start(self):
        print("Silnik uruchomiony")


class Samochod_elektryczny(Samochod):
    def start(self):
        print("Silnik elektryczny uruchomiony.")


def main():
    sam_spal = Samochod()
    sam_spal.start()

    sam_el = Samochod_elektryczny()
    sam_el.start()


if __name__ == "__main__":
    main()
