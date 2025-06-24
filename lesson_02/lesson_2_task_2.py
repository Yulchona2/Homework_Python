def is_year_leap(x):
    return True if (x % 4 == 0) else False


year = int(input("Введите год: "))
result = is_year_leap(year)
print(f"Год {year} високосный?: {result}")
