"""This program asks for a driver name and then continually asks the user to
start a new trip. The user then enters the time of the trip in minutes and the
program outputs the fee. When the user enters 'n', the program displays the
driver's name, and totals and averages for cost and time (see lines 27-31).
Jack Andrews
24/2/22
"""


def main():
    # Initializing data to keep count of totals and averages
    trip_list = []
    trip_cost = []
    total_mins = int()
    total_cost = int()
    driver = input("What is the driver's name? ").capitalize()
    while True:
        start_trip = input("Do you want to start a new trip? (y/n) ").lower()
        if start_trip == 'y':
            len_trip = int_checker("How long was the trip (in minutes)? ")
            trip_list.append(len_trip)  # Updating current data
            total_mins += len_trip
            price = calc_cost(len_trip)
            print(f"The price of the trip was ${price}")
            trip_cost.append(price)
            total_cost += price
        elif start_trip == 'n':
            # Prints out analysis including totals and averages for cost and
            # time taken
            print(f"The driver today was {driver}.")
            print(f"Total time of all trips was {total_mins} minutes.")
            print(f"Average time for each trip was {avg(trip_list):.2f}"
                  f" minutes.")
            print(f"Total income for today is ${total_cost}.")
            print(f"Average cost of each trip was ${avg(trip_cost):.2f}.")
            exit(0)
        else:  # Handling unexpected input so program doesn't crash
            print("Invalid input, please enter again.")


def calc_cost(minutes):
    from collections import namedtuple
    constants = namedtuple("consts", "BASE_COST")
    consts = constants(10)  # Creates constant with unalterable value
    price = consts.BASE_COST + 2 * minutes
    return price


def int_checker(msg, confirm=True):
    # Converts input to int but can ask user to confirm before returning
    data = input(msg)
    try:
        data = int(data)
        if data < 1:  # Disallows 0 or below as valid input
            raise ValueError
        if confirm:
            if input("Confirm? (y/n) ").lower() == 'y':
                return data
            else:
                return int_checker(msg, confirm=confirm)
                # confirm=confirm remembers the value of the parameter when the
                # function was last called
        elif not confirm:
            return data
        else:
            print(f"{confirm} is not a valid option, please enter again")
            return int_checker(msg, confirm=confirm)
    except ValueError:  # Catching errors so program doesn't crash
        print(f"{data} is either invalid or not an integer,"
              f" please enter again")
        return int_checker(msg, confirm=confirm)


def avg(lst):  # Takes a number list and returns the average of the items.
    output = 0
    if len(lst) == 0:
        return 0  # Avoiding ZeroDivision errors
    for item in lst:
        output += item
    return output / len(lst)


if __name__ == '__main__':
    main()
