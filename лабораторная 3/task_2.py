# TODO Напишите функцию find_common_participants
def find_common_participants(list_1,list_2, sell=","):
    first_group = set(list_1.split(sell))
    second_group = set(list_2.split(sell))
    matching_surnames = first_group.intersection(second_group)
    matching_surnames = list(matching_surnames)
    matching_surnames.sort()
    return(matching_surnames)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой
print(find_common_participants(participants_first_group,participants_second_group,sell="|"))