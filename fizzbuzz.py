from __future__ import print_function

for i in range(1,100): 
    number = True
    if(i%3==0):
        number = False
        print("fizz",end='')
    if(i%5==0):
        number = False
        print("buzz",end='')
    if(number):
        print(i,end='')
    print("\n")
    
