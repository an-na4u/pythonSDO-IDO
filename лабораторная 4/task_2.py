
import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task():
    with open(INPUT_FILENAME) as file:
        lines = [line for line in csv.DictReader(file)]

    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(lines, indent=4))
    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    #Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
