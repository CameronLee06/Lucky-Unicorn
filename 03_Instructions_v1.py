
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


def instructions():
    print("**** How To Play ****")
    print()
    print("The rules of the game go here")
    print()
    return ""


show_instructions = ""
while show_instructions.lower() != "xxx":
    # Ask the user if they have played before
    show_instructions = yes_no("Have you played this game before?" )

    if show_instructions == "yes":
        print("game continues\n")
    elif show_instructions == "no":
        print("show instructions \n")

if show_instructions == "yes":
    instructions()
else:
    print("Program Continues")
