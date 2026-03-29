def find_common_participants(first_group, second_group, razdelitel = ","):#задаю новую функцию
    group_1 = set(first_group.split(razdelitel))
    #преобразую список в множество
    #разбиваю строку на подстроки, разделяя запятой
    group_2 = set (second_group.split(razdelitel))
    # преобразую список в множество
    # разбиваю строку на подстроки, разделяя запятой
    duble = group_1.intersection(group_2)#нахожу пересечения в двкх множествах
    return sorted(list(duble))



participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, razdelitel = "|"))
#вывожу с разделителем |
