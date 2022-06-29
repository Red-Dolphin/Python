square=[]
# range=[2,10]
for x in range(1,10):
    square.append(x**2 )
print(square)
print(square[-1])
del(square[1:3])
print(square)
# 2nd example
square1=[x**2+1 for x in range(1,10)]
print(square1)