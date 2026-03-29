
def function(items_list, find_item):#задаю новую функцию
    if find_item in items_list:#проверяю есть ли искомый элемент в сптске
        return items_list.index(find_item)#если элемент есть, то выводим индекс первого вхождения
    else:
        return None#если элемент не найден, ничего не выводим


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:#ввожу цикл
    index_item = function(items_list, find_item)
    #говорю, что данная переменная выполняет условия моей функции
    if index_item is not None:#говорим, что переменная не равна None
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
