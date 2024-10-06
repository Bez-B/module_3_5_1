def get_multiplied_digits(number):
    str_number = str(number)
    list_1 = []
    for i in str_number:
        if int(i):
            list_1.append(i)
    str_number = ''.join(list_1)
    first = int(str_number[0])
    if len(str_number) > 1:
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        return first


result = get_multiplied_digits(150703000)
print(result)
