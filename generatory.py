def licz_od_1_do(n):
    for i in range(1, n + 1):
        yield i

for liczba in licz_od_1_do(5):
    print(liczba)
