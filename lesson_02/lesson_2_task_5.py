def month_to_season(month_number):
    if month_number in (1, 2, 12):
        return "Зима"
    elif 3 <= month_number <= 5:
        return "Весна"
    elif 6 <= month_number <= 8:
        return "Лето"
    elif 9 <= month_number <= 11:
        return "Осень"
    else:
        return "Неверный номер месяца"


try:
    month = int(input("Введите номер месяца от 1 до 12: "))
    print(month_to_season(month))
except ValueError:
    print("Введите, пожалуйста, целое число от 1 до 12")
