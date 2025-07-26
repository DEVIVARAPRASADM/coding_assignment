def format_indian_currency(amount):
    s = str(amount)
    if '.' in s:
        integer_part, decimal_part = s.split('.')
        decimal_part = '.' + decimal_part
    else:
        integer_part = s
        decimal_part = ''

    n = len(integer_part)
    if n <= 3:
        return integer_part + decimal_part

    last3 = integer_part[-3:]
    rest = integer_part[:-3]
    result = ''

    while len(rest) > 2:
        result = ',' + rest[-2:] + result
        rest = rest[:-2]

    if rest:
        result = rest + result

    return result + ',' + last3 + decimal_part if result else last3 + decimal_part

amount = 123456.7891
formatted = format_indian_currency(amount)
print("Formatted Amount:", formatted)  
