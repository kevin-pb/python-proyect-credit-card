def sum_digits(value, sum=0):

    if value > 9:

        result = value // 10

        rest = value % 10

        return sum_digits(result, sum + rest)

    return sum + value


def get_digits(value, digits=[]):

    if value > 9:

        result = value // 10

        rest = value % 10

        digits.append(rest)

        return get_digits(result, digits)

    else:

        digits.append(value)

        return list(reversed(digits))


def luhn_verify(num):

    digits = get_digits(num)

    result = 0

    for i, digit in enumerate(digits):

        digit = digits[i]

        tmp = 0

        is_possition_pair = (int(i) + 1) % 2 == 0

        if is_possition_pair:

            tmp = sum_digits(digit * 2)

        else:

            tmp = digit

        result += tmp

    print(">>>>>>>>> " + str(result))
    return result % 10 == 0
