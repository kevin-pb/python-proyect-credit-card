

try:    
    
    number = int(input("Introduce the number to evaluate: "))


    

    print("The credit card is " + str(luhn_comprobation_method(number)))

except ValueError:
    
    print("You entered an incorrect value")
