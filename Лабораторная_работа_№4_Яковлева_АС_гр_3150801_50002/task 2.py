import csv#импортирую файл csv в код
import json#импортирую файл json в код

INPUT_FILENAME = "input.csv"# создаем константу для файла csv
OUTPUT_FILENAME = "output.json"# создаем константу для файла json


def task() -> None:# задаем фукцию, которая ничего не выводит
    data = []# задаем пустой список для файла csv
    with open(INPUT_FILENAME, 'r', encoding="utf-8") as file:
        # открываю файл в режиме чтения
        reader = csv.DictReader(file, delimiter = ",")
        # создаю объект , который читает файл как список словарей
        for row in reader:# создаю цикл
            data.append(row)# добавляю словарь row в data



    with open(OUTPUT_FILENAME, 'w',encoding="utf-8" ) as j_file:
        # открываю файл в режиме записи
        json.dump(data, j_file, indent=4, ensure_ascii=False)
        # записываю пайтон объекты из словарей data
        # в файл в формате json




if __name__ == '__main__':
    # Нужно для проверки
    task()#вызываем функцию

    with open(OUTPUT_FILENAME, 'r', encoding='utf-8') as output_f:
        # открываем файл в режиме чтения
        for line in output_f:
            # цикл, перебирающий каджую строку в файле
            print(line, end="")
            # вывод без добавления символа новой строки