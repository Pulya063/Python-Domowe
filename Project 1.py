from random import randint

# Zadanie 1
a = type(1 + 2)
b = type(1 + 4.5)
c = type(3 / 2)
d = type(4 / 2)
e = type(3 // 2)
f = type(-3 // 2)
g = type(11 % 2)
h = type(2  10)
i = type(8  (1/3))

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)
print(h)
print(i)

# Zadanie 3
imie = "Andrii"
kierunek = "Informatyka"
uczelnia = "WSIZ"

("Nazywam się" * imie, end = ' ')
print("Studiuje na kieruneku", kierunek, sep = '')

# Zadanie 4
print("Jak się nasywasz?")
name = input(imie)
print(imie)
print(f"Cześć {imie}, witaj na zajenciach UwU")

# Zadanie 5
bok1 = float(input("Podaj długość boku prostokąta: "))
bok2 = float(input("Podaj długość drugiego boku prostokąta: "))

obw = ((bok1 + bok2) * 2)
print(obw)

# Zadanie 5
bok1 = float(input("Podaj długość boku prostokąta: "))
bok2 = float(input("Podaj długość drugiego boku prostokąta: "))

obw = ((bok1 + bok2) * 2)
print(obw)

# Zadanie 6
dystans = float(input("Podaj pokonaną odległość : "))
srednie_spalanie = float(input("Podaj średnie spalanie samochodu: "))

# Cena paliwa w złotówkach za litr
cena = 6.5

# Obliczanie zużycia paliwa
zuzycie_paliwa = (dystans / 100) * srednie_palanie)
# Obliczanie kosztów podróży
koszt_podrozy = zuzycie_paliwa * cena

# Wyświetlanie wyników
print("Przewidywane zużycie paliwa: ", zuzycie_paliwa)
print("Szacowany koszt podróży: ", koszt_podrozy)

# Zadanie 7
dystans = randint(1, 500)
srednie_spalanie = float(input("Podaj średnie spalanie samochodu: "))

# Cena paliwa w złotówkach za litr
cena = 6.5

# Obliczanie zużycia paliwa
zuzycie_paliwa = (dystans / 100) * srednie_spalanie)
# Obliczanie kosztów podróży
koszt_podrozy = zuzycie_paliwa * cena

# Wyświetlanie wyników
print("Droga: ", dystans, "km")
print("Przewidywane zużycie paliwa: ", zuzycie_paliwa, "/ l")
print("Szacowany koszt podróży: ", koszt_podrozy, "/ PLN")
