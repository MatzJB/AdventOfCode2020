import re


def is_db_row_ok(raw_string):
    x = re.search(r"(\d+)-(\d+)\ (\w)\: (\w+)", raw_string)
    occurance_min = int(x.group(1))
    occurance_max = int(x.group(2))
    character = x.group(3)
    string = x.group(4)
    string_count = string.count(character)
    return string_count >= occurance_min and string_count <= occurance_max

def is_db_row_ok2(raw_string):
    x = re.search(r"(\d+)-(\d+)\ (\w)\: (\w+)", raw_string)
    char_index_1 = int(x.group(1))
    char_index_2 = int(x.group(2))
    character = x.group(3)
    string = x.group(4)
    return (string[char_index_1-1] == character) ^ (string[char_index_2-1] == character)


with open('input.txt') as f:
    rows = f.readlines()

number_of_ok_rows = 0

[number_of_ok_rows := number_of_ok_rows + x for x in map(is_db_row_ok2, rows)]

print(number_of_ok_rows)
