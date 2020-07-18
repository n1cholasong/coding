import math
print('Quadratic Equation Calculator')

for x in range(999):
    
    print('')
    
    a = float(input('A = '))
    b = float(input('B = '))
    c = float(input('C = '))

    d = (b**2) - (4*a*c)

    print('')
    print('Discriminant =', d) 
    
    if d < 0:
        print('No real solution!')

    elif d > 0:
        sqrt = math.sqrt(d)
        sol1 = (-b + math.sqrt(d)) / (2*a)
        sol2 = (-b - math.sqrt(d)) / (2*a)
        print('=', sqrt)
        print('\nx = %s\nx = %s' %(sol1, sol2))

    print('')
    print('=============== NEXT QUESTION ===============')
    
   

