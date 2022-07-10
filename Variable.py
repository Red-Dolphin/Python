# Global variable
x="Tapan"
def myfunc():
    print("My name is ",x)
myfunc()

# Local varible:- when declare inside of a function
def youfunc():
    x="Big Boss"   # x act as a local variable
    print("Hi",x)
youfunc()    

# use of "global" key word to make a variable global
 
def myfunc():
    global y
    y="Indian"
myfunc()
print("I'm an",y)

# Replace the global variable

x = "awesome"

def myfunc():
  global x
  x = "fantastic" # variable will be replaced by global one

myfunc()

print("Python is " + x)