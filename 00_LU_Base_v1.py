# Checks for yes/no
import random
def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()

        if response== "yes" or response== "y":
            return "yes"

        elif response == "n" or response== "no":
            return "no"

        else:
            print("Please answer yes / no")

# Checks for number between higher and lower
def num_check(question, low, high):
    error = "please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input(question))

            # if the amount is too low / too high give
            if low <= response <= high:
                return response


                # output an error
            else: 
                print(error)

        except ValueError:
            print("Error, please try again")

# *** Main Routine ***

# Ask the user if they have played before
show_instructions = yes_no("Have you played this game before?" )

if show_instructions == "yes":
    print("Okay, next part\n")
elif show_instructions == "no":
    print("show instructions \n")


balance = num_check("How much do you want to play with? ", 1, 10)

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    # print round number 
    print("*** Round #{} ***".format(rounds_played))
    
    chosen_num = random.randint(1,100)
    
    # adjust balance
    # if the random #is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <=5:
        chosen = "unicorn"
        balance += 4

    # if the random # is between 6 and 36
    #user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <=36:
        balance -=1
        chosen = "donkey"
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            balance -= 0.5

    print("You got a {}.  Your balance is $""{:.2f}".format(chosen, balance))

    if balance < 1:
        break
        play_again = "xxx"
        print("Sorry you have run out of money")

    

    play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final Balance", balance)

