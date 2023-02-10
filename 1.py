# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.

# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

def step(a, b):
    if (b == 1):
        return (a)
    if (b != 1):
        return (a * step(a, b - 1))


a = int(input("Vvedite chislo: "))
b = int(input("Vvdedite stepen': "))

print("Resultat:", step(a, b))
