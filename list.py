# List using for loop
square=[]

# range=[2,10] // can be use this format

for x in range(1,10):
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
square2=['Ram','Sam','Jadu','Riya','Akas','Sayani']
print(square2)
square2.append('Ishita') #list.append() takes exactly one argument
print(square2)
square2.remove('Ram') # .remove use to delete certain element => list.remove
print(square2)
                      # square2.remove('-1') ** can't use in this form

#  insert element in a certain position 
square2.insert(0,"Name list")
print(square2)
print(square2.pop(3)) # pop expected at most 1 argument