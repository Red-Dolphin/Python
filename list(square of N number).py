# square root of natural number




n=int(input("Give how many numbe you want\n"))
if n<0 :
    print('sorry please give positive number')
square=[]
for x in range(1,n):
    square.append(x**2)
print(square)  
total=0                         # Don't put this inside for loop
for y in range(0,(n-1)):

             # total=0 The sum will returns to the last value of the list 
    total=total +  square[y]
print(total)    
# you can also find sumation using sum function
sumation=sum(square)
print('The sum is',sumation)