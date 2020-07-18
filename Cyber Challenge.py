from random import randint

p = True
a = 0   #multiplyer for variable x         
b = 0   #multiplyer for variable y
x = 0   #the ASCCI code  
y = 0   #the ASCCI code 

while p == True:                                      #program will continues to run forever until p == false
    x = randint(65,90)                                #generates ASCII code of A-Z
    y = randint(97, 122)                              #generates ASCII code of a-z

    a = randint(0, 9)                                 #generate the limits of multiplication for variable a
    b = randint(0, 9)                                 #generate the limits of multiplication for variable b
             
    c1 = a + b                                        #equation for condition 1, as only 9 character is needed

    if c1 == 9:                                       #when condition is met, the following output will be process
        c2 = (a*x) + (b*y)                            #equation for condition 2
        if c2 == 896:                                 #when condition is met, the following output will be process
            print('%s(%s) + %s(%s)'%(a ,x, b, y))     #this will print the possibilities
