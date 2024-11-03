# TODO Напишите функцию для поиска индекса товара
def search_items(word,items):
    for j in range(len(items)):
            if word not in items[j]:
                pass
            elif word in items[j]:
                return j
            else:
                return None

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = search_items(find_item,items_list)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")

