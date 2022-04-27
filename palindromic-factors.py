def find_factors(value):
    i = 1
    factors = []
    while(i<=value):
        if (value%i) == 0:
            factors.append(i)
        i=i+1
    return factors

def is_palindrome(factor):
    factor = str(factor)
    rev = factor[::-1]
    return factor == rev

n = int(input('How many values will you enter: '))
values = []
for i in range(n):
    a = int(input('Enter value ' + str(i+1) + ': '))
    values.append(a)

caseNumber = 1
for i in values:
    palindromicFactors = 0
    for f in find_factors(i):
        if is_palindrome(f) == True:
            palindromicFactors = palindromicFactors + 1

    print('Case #' + str(caseNumber) + ': ' + str(palindromicFactors))
    caseNumber = caseNumber + 1
    
