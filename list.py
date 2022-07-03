# List using for loop

square=[]

# range=[2,10] // you may use this format

for x in range(1,10): # Range function
    square.append(x**2 )
print(square)
print(square[-1]) # Accessing certain element
del(square[1:3])
print(square)

# 2nd example

square1=[x**2+1 for x in range(1,10)]
print(square1)

# length of a list

x=len(square)
print('length is', x)

# list in string format

square2=['ram','sam','jadu','riya','akas','sayani']
print(square2)
square2.append('Ishita')            #list.append() takes exactly one argument
print(square2)
square2.remove('ram')     # .remove use to delete certain element => list.remove
print(square2)
                          # square2.remove('-1') ** can't use in this form

#  insert element in a certain position 

square2.insert(0,"Name list")
print(square2)
print(square2.pop(2))       # pop expected at most 1 argument

# sorting of a list

print(sorted(square2))
print(square2.sort())

# Combining two list

square3=square1 + square2
print(square3)

# Range function

for number in range(0,5):
    print(number)
 
# minimum value in a list

minimum=min(square)    
print('min value',minimum)

# maximum in a list

maximum=max(square)
print('max value',maximum)

# Sum of a list

sumation=sum(square)
print('sum is',sumation)

# Slicing of a list

square4=square3[5:14]
print(square4)
square5=square3[-5:]            # Negative indexing
print(square5)

# Copying of a list

square6=square5[:]
print('Copied List\n',square6)

# making uper case in name
# 1. Using for loop
square6=[]
for x in square2:
    square6.append(x.upper())
print('using for loop\n',square6)    
# 2. Using comprehension
square7=[name.upper() for name in square2]
print("using comprehention\n",square7)