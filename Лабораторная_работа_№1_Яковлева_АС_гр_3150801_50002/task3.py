list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# находим индекс для разделения списка на две равные части
middle_index = len(list_players) // 2

# формируем первую команду из первой половины списка
first_team = list_players[:middle_index]

# формируем вторую команду из второй половины списка
second_team = list_players[middle_index:]

print( first_team)
print( second_team)