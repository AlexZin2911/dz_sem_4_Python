# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите натуральное положительное число: "))
i = 1 
lst = []
old = num
while i <= num:
    if num % i == 0:
        lst.append(i)
        num //= i
        i = 2
    else:
        i += 1
print(f"Простые множители числа {old} -> {lst}")