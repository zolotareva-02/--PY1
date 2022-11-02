def get_count_char(str_):
    ...  # TODO посчитать количество каждой буквы в строке в аргументе str_
    my_dict = {}
    str_ = str_.lower()
    for k in str_:
        if k not in my_dict and k.isalpha():
            my_dict.setdefault(k, 1)
        else:
            if k in my_dict:
                my_dict[k] += 1
    return my_dict

def percentage(sym_dict):
    for k, value in sym_dict.items():
        sym_dict[k] = str(value * 100 / sum(sym_dict.values())) + "%"
    return sym_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
