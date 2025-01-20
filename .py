try:    
    
    number = int(input("Introduce the number to evaluate: "))


    def sum_pair_multiplied_by_two_position(number):
        
        digits = str(abs(number))  
        
        sum_of_digits_even_positions = 0
        sum_of_digits_even_positions_multiplied_by_two = 0

        for i, digit in enumerate(digits, start=1):
    
            if i % 2 == 0:

                sum_of_digits_even_positions += digit

                if digit * 2 < 9:
                    sum_of_digits_even_positions_multiplied_by_two += int(digit) * 2
        
                elif digit * 2 > 9:
    
                    result = (int(digit) * 2) // 10
        
                    rest = (int(digit) * 2) % 10
                    
                    sum_of_digits_even_positions_multiplied_by_two += int(result + rest)
        
        return [sum_of_digits_even_positions, sum_of_digits_even_positions_multiplied_by_two]


    def luhn_comprobation_method(value, cumulative_sum=0):
    
        print(value)
        if value > 9:
    
            result = value // 10
        
            rest = value % 10
        
            return luhn_comprobation_method(result, cumulative_sum + rest)
    
        print(value)
    
        pair_position = sum_pair_multiplied_by_two_position(value)
        print(pair_position[0])
        print(pair_position[1])
        print(pair_position)
    
        total_sum = cumulative_sum + value
        
        total_sum = total_sum + pair_position[1] - pair_position[0]

        if total_sum % 10 == 0:
            
            return True
        
        else:
            
            return False

    print("The credit card is " + str(luhn_comprobation_method(number)))

except ValueError:
    
    print("You entered an incorrect value")
