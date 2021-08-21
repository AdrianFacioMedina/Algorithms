def digitCount(value):
    if value==0: return 1;
    digits = 0;
    while(value>=1):  
        value = value/10
        digits+=1
    return digits

def findOnes(value):
    totalDigits = digitCount(value)
    counter = [ [0]*10 for d in range(totalDigits+1) ]
    powers =[0]*(totalDigits+1)
    
    power = 1
    for position in range(1,totalDigits+1):
        powers[position]=power;
        for digit in range(1,10):
            if(digit == 1):
                counter[position][digit] = (
                    counter[position-1][9] +
                    power +
                    counter[position-1][9] )
            else:
                counter[position][digit] = (
                    counter[position][digit-1] +
                    counter[position-1][9] )     
        power*=10

    countOnes=0;
    remainder=value
    for position in reversed(range(1,totalDigits+1)):
        digit = remainder // powers[position]
        remainder = remainder %  powers[position]
        
        if digit==1:
            countOnes += counter[position-1][9] + 1 + remainder  
        elif digit > 0:
            countOnes += counter[position][digit-1]
    return countOnes;
