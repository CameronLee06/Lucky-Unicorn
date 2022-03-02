# Checks for yes/no
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
    print("game continues\n")
elif show_instructions == "no":
    print("show instructions \n")


how_much = num_check("How much do you want to play with? ", 1, 10)
print("you chose to play with ${:.2f}".format(how_much))

