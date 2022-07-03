try:
    x=int(input("give your number\n"))
    if x==0 :
        print("your number is neither positive nor negative")
    elif x>0 :
        print('your number is positive')

    else :
     print("your number is negative")    
except ValueError:         # when input is not a number
    print("Pease input number")     