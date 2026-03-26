salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
capital_pillow = 0 # ввожу переменную для подши безопасности

for months in range (1, 11): #ввожу цикл в рамках 10 месяццев
    whole_spending = spend * (1 + increase) ** (months-1) #формула для подсчета трат в разные меяцы
    capital_pillow += (whole_spending - salary) #формула для подсчета подушки безопасности
    if capital_pillow == whole_spending:
        break # останавливаю цикл если подушка безопасности равна тратам

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", int (capital_pillow))
