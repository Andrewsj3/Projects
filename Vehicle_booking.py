"""This program allows the user to hire a vehicle out of a set list of vehicles
. It continually asks the user how many seats they will need, and displays list
of vehicles available. The user then books a vehicle. When '-1' is entered,
the program displays statistics and exits.
Jack Andrews
25/02/22
"""


def main():
    cars = [("Suzuki Van", 2), ("Toyota Corolla", 4), ("Honda CRV", 4),
            ("Suzuki Swift", 4), ("Mitsubishi Airtrek", 4),
            ("Nissan DC Ute", 4), ("Toyota Previa", 7), ("Toyota Hiace", 12),
            ("Toyota Hiace", 12)]
    available = cars.copy()
    hired = []
    while True:
        seats = int_checker("How many seats are needed? (Enter -1 to quit) ")
        if seats == 0:  # Value returned if user enters -1
            break
        print_vehicles(available, seats)
        idx, name = book_vehicle(cars, available, seats)
        del available[idx]
        hired.append((idx, name))
    print("Vehicles booked today:")
    for car_idx, hirer in hired:
        print(f"No. {car_idx + 1} - {cars[car_idx][0]} - Booked by: {hirer}")


def int_checker(msg, confirm=True):
    # Converts input to int but can ask user to confirm before returning
    data = input(msg)
    if data == '-1':
        return 0
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
        print(
            f"{data} is either invalid or not an integer, please enter again")
        return int_checker(msg, confirm=confirm)


def print_vehicles(vehicles, req_seats):
    warn = "(Not enough seats)"  # Warns user if car doesn't have enough seats
    for number, vehicle_data in enumerate(vehicles, start=1):
        vehicle, seats = vehicle_data
        print(f"{number}) {vehicle}, seats: {seats}"
              f" {warn if req_seats > seats else ''}")


def book_vehicle(vehicles, available_vehicles, seats):
    vehicle_to_book = int_checker("\nWhich vehicle do you want to book? ") - 1
    if available_vehicles[vehicle_to_book][1] < seats:
        print("This vehicle does not have enough seats, please enter again.")
        # Failsafe to ensure user cannot accidentally book wrong car
        return book_vehicle(vehicles, available_vehicles, seats)
    name = input("Enter your name: ").capitalize()
    print(f"{available_vehicles[vehicle_to_book][0]} booked by {name}\n")
    return vehicle_to_book, name
    # Returning number of vehicle and hirer to be used in other functions


if __name__ == '__main__':
    main()
