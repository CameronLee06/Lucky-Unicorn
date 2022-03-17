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


def statement_generator(statement, decoration):
    
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)


    return ""

# *** Main Routine ***

# Ask the user if they have played before

print()
statement_generator("Welcome to the Lucky Unicorn Game", "-")
print()

show_instructions = yes_no("Have you played this game before? " )

if show_instructions == "yes":
    print("Okay, next part\n")
elif show_instructions == "no":
    print("show instructions \n")


balance = num_check("Choose a starting amount between 1-10 ", 1, 10)

rounds_played = 0

play_again = input("Press <Enter> to play...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    print()
    # print round number 
    rounds_statement = "*** Round #{} ***".format(rounds_played)
    statement_generator(rounds_statement, "^")
    
    chosen_num = random.randint(1,100)
    
    # adjust balance
    # if the random #is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <=5:
        chosen = "unicorn"
        decoration = "*"
        balance += 4

    # if the random # is between 6 and 36
    #user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <=36:
        balance -=1
        chosen = "donkey"
        decoration = "D"
    else:
        if chosen_num % 2 == 0:
            chosen = "horse"
            decoration = "H"

        # otherwise set it to a zebra
        else:
            chosen = "zebra"
            balance -= 0.5
            decoration = "Z"

    feedback = "You got a {}.  Your balance is $""{:.2f}".format(chosen, balance)
    statement_generator(feedback, decoration)

    if balance < 1:

        play_again = "xxx"
        print("Sorry you have run out of money")
        break

    

    play_again = input("Press Enter to play again or 'xxx' to quit")

print()
print("Final Balance", balance)

