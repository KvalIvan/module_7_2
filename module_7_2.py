from pprint import pprint


def custom_write(file_name, strings):
    strings_positions = {}
    string_number = 0
    file = open(file_name, 'w', encoding='utf-8')
    for string in strings:
        string_number += 1
        string_list = [string_number, file.tell()]
        file.write(f'{string}\n')
        f'{string_list}, {string}'
        strings_positions[(string_number, file.tell())] = string
    file.close()
    return pprint(strings_positions)


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

custom_write('test.txt', info)