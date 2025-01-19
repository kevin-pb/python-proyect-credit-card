try:    
    
    number = int(input("Introduce the number to evaluate: "))


    def sum_pair_position(number):
        
        digits = str(abs(number))  
        
        sum = 0

        for i, digit in enumerate(digits, start=1):
    
            if i % 2 == 0:
    
                if digit * 2 < 9:
                    sum += int(digit * 2)
        
                elif digit * 2 > 9:
    
                    result = digit // 10
        
                    rest = digit % 10
                    
        
        return sum


    def luhn_comprobation_method(value, cumulative_sum=0):
    
        if value > 9:
    
            result = value // 10
        
            rest = value % 10
        
            return luhn_comprobation_method(result, cumulative_sum + rest)
    
        total_sum = cumulative_sum + value
        
        total_sum = total_sum + multiplication_by_two() - sum_pair_position(number)

        if total_sum % 10 == 0:
            
            return True
        
        else:
            
            return False

    print("The credit card is " + str(luhn_comprobation_method(number)))

except ValueError:
    
    print("You entered an incorrect value")
