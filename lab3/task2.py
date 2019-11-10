import re
my_list = [int (i) for i in re.findall(r'[+-]?\d+', input("Список: "))]

def two_divider(under_parse_list):
    new_list = []
    for element in under_parse_list:
        if element%2 == 0:
            new_list.append(element)
    return new_list

print(two_divider(my_list))