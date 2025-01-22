from luhn_verify_module import sum_digits
from luhn_verify_module import get_digits
from luhn_verify_module import luhn_verify

try:    
    
    number = int(input("Introduce the number of the credit card: "))
    
    if luhn_verify(number) == True:
        
        print("The credit card is valid")
        
    else:
        
        print("The credit card is invalid")

except ValueError:
    
    print("You entered an incorrect value")
