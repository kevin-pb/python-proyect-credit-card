# Credit dard

This project uses the Luhn method to check if a credit card number is valid.

# Luhn method

The "Luhn" method was created for credit card validation. The Luhn method is as follows:
First we multiply the digits of the number in even positions by two and if it is a two-digit result we add its digits. After that we add the rest of the digits and the result of the sum of the even digits multiplied by two. If the result is a number divisible by ten, the card is valid.

# Run & Configure

python -m graphic_interface

# References

- [luhn-algorithm](https://www.geeksforgeeks.org/luhn-algorithm/)

- [Recursividad en Python](https://www.youtube.com/watch?v=yX5kR63Dpdw)