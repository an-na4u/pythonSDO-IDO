# TODO  Напишите функцию count_letters
def count_letters(text):
    letters = []
    for symbols in text:
        if symbols.isalpha():
            letters.append(symbols.lower())
    dict = {}
    for i in text:
        if i in dict and i.isalpha():
            dict[i] += 1
        else:
            dict[i] = 1
    return dict


# TODO Напишите функцию calculate_frequency
def calculate_frequency(dict_):
    sum_of_letters = len(dict_)
    for key, value in dict_.items():
        dict_[key] = round(value / sum_of_letters,2)
    return dict_

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

# TODO Распечатайте в столбик букву и её частоту в тексте

number_of_symbols = count_letters(main_str)
frequency_of_symbols = calculate_frequency(number_of_symbols)

for key, value in frequency_of_symbols.items():
    print (key, ": ", value)