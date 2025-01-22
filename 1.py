"""function luhnVerify(num) {
    let digits = getDigits(num);
    let result = 0;
   
     // extra data
    let full = [];
    let odd = [];
    let pair = [];

    for (let i in digits) {
        let digit = digits[i];
        let tmp = 0;
        let isPossitionPair = (parseInt(i) + 1) % 2 === 0;

        if (isPossitionPair) {
            tmp = sumDigits(digit * 2);

            // extra data
            pair.push(tmp);
        } else {
            tmp = digit;

            // extra data
            odd.push(tmp);
        }

        result += tmp;

        // extra data
        full.push(tmp);
    }
    return {
        isValid: result % 10 === 0,
        extra: { sum: result, digits, pair, odd, full }
    };
}
"""

def get_digits(value, digits=[]):
    
    if value > 9:
        
        result = value // 10
        
        rest = value % 10

        digits = list(digits)

        digits.append(rest)
        
        return get_digits(result, digits)
    
    else:
        
        digits = list(digits)
        
        digits.append(value)
        
        return digits.reverse()

print(get_digits(199))

def luhn_verify(num):
    
    digits = get_digits(num)
    pass