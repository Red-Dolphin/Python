# Exception

prompt = "How many tickets do you need?\n "
num_tickets = input(prompt) 
try:
     num_tickets = int(num_tickets) 
except ValueError: 
    print("Please try again.") 
else: 
    print("Your tickets are printing.")












