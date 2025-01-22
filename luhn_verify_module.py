#"sum_digits" sum all the digits in a number

def sum_digits(value, sum=0):

#   The value passed is checked to see if it
#   is two or more digits long in order to 
#   break it down into figures.
    
    if value > 9:
        
#       Divide by ten to break down the number.
#       Example: 123 : 10 = 12.3
#       
#       In this case we can break down the number as follows:
#       result = 12
#       
#       rest = 3 
        
        result = value // 10

        rest = value % 10

#       We call the function within itself and in this way we apply recursion, 
#       which allows us to repeat the code above. Although this time we call it with other parameters:
#       
#       (result, sum + rest)
# 
#       Sallows us to add the digits for each time the function is executed.
        
        return sum_digits(result, sum + rest)

#   Once the last number is no longer greater than two digits, the last value is sum.

    return sum + value


#"get_digits" get all the digits in a number

def get_digits(value, digits=[]):

#   The value passed is checked to see if it
#   is two or more digits long in order to 
#   break it down into figures.

    if value > 9:

#       Divide by ten to break down the number.
#       Example: 123 : 10 = 12.3
#       
#       In this case we can break down the number as follows:
#       result = 12
#       
#       rest = 3 

        result = value // 10

        rest = value % 10

#       We add the remainder that is equal to the last
#       digit of the number to the "digits" list

        digits.append(rest)

#       We apply recursion to call the function and execute the code again,
#       in this way we save the last element in digits.

        return get_digits(result, digits)

    else:

#       Once the last number is no longer greater than two digits,
#       the last value is added and reversed so that the digits are in order.

        digits.append(value)

        return list(reversed(digits))

#"luhn_verify" calls the "sum_digits" function and the "get_digits" function; using them,
#checks a number by applying Luhn's method.

def luhn_verify(num):

#   We save in a variable the result of the "get_digits" function that returns a list
#   with all the digits of the passed number 

    digits = get_digits(num)

    result = 0

#   We iterate the values ​​of the list returned by "get_digits" saving in "i" 
#   the number of the iteration and in "digit" the value of that position in the iteration

    for i, digit in enumerate(digits):

        digit = digits[i]

        tmp = 0

#       A boolean value is stored in a variable referring to
#       whether it is an even iteration or not.

        is_possition_pair = (int(i) + 1) % 2 == 0

        if is_possition_pair == False:

            tmp = sum_digits(digit * 2)

        else:

            tmp = digit

        result += tmp

    return result % 10 == 0
