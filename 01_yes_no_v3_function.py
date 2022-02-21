
def yes_no(question):

    valid = False
    while not valid:
        response = input(question).lower()

        if response== "yes" or response== "y":
            response= "yes"
            return response

        elif response== "n" or response== "no":
            return response

        else:
            print("Please answer yes / no")


show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = yes_no("Have you played this game before?" )

    