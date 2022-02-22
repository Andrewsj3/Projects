"""This program is designed to manage pickup and drop off of children at MGS
Childcare. Users can either pick up or drop off one child or several children
at once. They can also see the names of children currently in the daycare.
When the user is finished, they select the option to exit the program.
Written by Jack Andrews
22/2/22
"""


def menu(lst):
    print("\nHere are your options:\n"
          "1: Check a child in or out\n"
          "2: View the list of children currently staying\n"
          "3: Exit the program")
    option = input(">>> ")
    print("\n", end='')
    if option == '1':
        check_in_out(lst)
    elif option == '2':
        print_roll(lst)
    elif option == '3':
        print("Goodbye!")
        exit(0)
    else:  # Handles case where user enters invalid input
        print(f"{option} isn't a valid option, please enter again.")
        menu(lst)


def check_in_out(child_list: list):
    children = []
    option = input("Do you want to check a child in or out? (i/o) ").lower()
    if option == 'i':
        qty_children = int_checker("How many children do you want to check "
                                   "in? ")
        # Allows user to check in multiple children
        time = int_checker("How many hours will the child/ren be staying? ")
        for i in range(qty_children):
            child = input("Enter name of child: ").capitalize()  # Makes sure
            # names start with a capital
            children.append(child)
        calc_cost(qty_children, time)  # Prints the cost of x children staying
        # for y hours
        while True:
            confirm = input(f"Confirm dropoff of {qty_children}"
                            f" children for {time} hours? (y/n) ").lower()
            # Final confirm, allows the user to cancel if they made an error
            if confirm == 'y':
                for i in children:
                    child_list.append(i)
                print("Children successfully registered.")
                break
            elif confirm == 'n':
                print("Returning to menu...")
                menu(child_list)
            else:  # Handles unexpected cases
                print(f"{confirm} is not a valid option, please enter again.")
    elif option == 'o':
        if len(child_list) == 0:  # Checks if there are no children in
            # the daycare
            print("There are no children to check out.")
            return None
        qty_children = int_checker("How many children do you want to check"
                                   " out? ")
        # Allows user to check out multiple children
        for i in range(qty_children):
            child = input("Enter name of child: ").capitalize()
            if child in child_list:
                child_list.pop(child_list.index(child))
                # Removes child from list
                print(f"{child} has been checked out.")
            else:  # If program cannot find the child in the list
                print(f"{child} is not in the list. These are the children"
                      f" currently checked in:")
                print_roll(child_list)  # Allows user to see all children
                # currently in daycare
                print("Perhaps you were looking for someone else?")
    else:  # Handles unexpected cases
        print(f"{option} is not a valid option, please enter again.")


def int_checker(msg):
    # Converts input to int but asks user to confirm before returning
    data = input(msg)
    try:
        data = int(data)
        confirm = input("Confirm? (y/n) ").lower()
        if confirm == 'y':
            return data
        elif confirm == 'n':
            return int_checker(msg)
        else:
            print(f"{confirm} is not a valid option, please enter again")
            return int_checker(msg)
    except ValueError:  # Catching errors so program doesn't crash
        print(f"{data} is not a number, please enter again")
        return int_checker(msg)


def calc_cost(num_children, num_hours):
    from collections import namedtuple
    constants = namedtuple("const", "HOURLY_RATE")
    consts = constants(12)  # Creating constant for hourly rate
    # Unlike normal constants in Python, the value of this constant cannot be
    # changed at runtime
    cost = num_children * num_hours * consts.HOURLY_RATE
    print(f"The cost for {num_children} children staying for {num_hours} hours"
          f" is ${cost}")


def print_roll(lst):
    if len(lst) > 0:
        print("These are the children currently checked in:")
        for index, child in enumerate(lst, start=1):
            print(f"{index}: {child}")
            # Formats the list into something more readable
    else:
        print("There are no children currently in the daycare.")


def main():
    # Initialize child list and print welcome message, then start the program
    child_list = []
    print("Welcome to MGS Childcare!")
    while True:
        menu(child_list)


if __name__ == "__main__":
    main()
