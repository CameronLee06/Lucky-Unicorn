import random

# main routine goes here 

STARTING_BALANCE = 100

balance = STARTING_BALANCE
# Testing loop to generate 20 tokens
for item in range(0,100):
    chosen_num = random.randint(1,100)
    
    # adjust balance
    if 1 <= chosen_num <=5:
        chosen = "unicorn"
        balance += 4
    elif 6 <= chosen_num <=36:
        balance -=1
    else:
        if chosen_num = 2 == 0:
        balance -=0.5

# output
print("Starting Balance: ${:.2f}".format(STARTING_BALANCE))
print("Final Balance: ${:.2f}".format(balance))

