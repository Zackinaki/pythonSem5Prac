# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел.
#  Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

# 2 2
# 4

def sum_2(a, b):
    return (sum_2(a + 1, b - 1) if b else a)


a = int(input("Vvedite 1 chislo: "))
b = int(input("Vvdedite 2 chislo: "))

print("Resultat summi chisel", a, "i", b, "ravna", sum_2(a, b))
