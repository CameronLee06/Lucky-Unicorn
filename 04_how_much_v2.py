# Functions go here
def num_check(question, low, high):
    error = "please enter an whole number between 1 and 10\n"

    valid = False
    while not valid:
        try:
            # ask the question
            response = int(input("How much would you like to play with?"))

            # if the amount is too low / too high give
            if low < response <= high:
                return response


                # output an error
            else: 
                print(error)

        except ValueError:
            print("Error, please try again")


# *** Main Routine ****

how_much = num_check("How much do you want to play with? ", 1, 10)
print("you chose to play with ${:.2f}".format(how_much))