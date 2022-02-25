def main():
    speeders = {}
    wanted_for_arrest = ["James Wilson", "Helga Norman", "Zachary Conroy"]
    print("For each speeder, input their name and their speed over the limit."
          "\nEnter $ to terminate input and display statistics.\n")
    while True:
        print('#' * 20)
        speeder = validate_name("What is the speeder's name? ")
        if speeder in wanted_for_arrest:
            print(f"{speeder} - WARRANT TO ARREST")
        elif speeder == 0:  # validate_name returns 0 if name is '$'
            break
        speed = int_checker("How far over the limit was the speeder? ")
        fine = calc_fine(speed)
        speeders[speeder] = fine  # Enters details of speeder
        print(f"{speeder} to be fined ${fine}")
        print('#' * 20)

    print_statistics(speeders)


def validate_name(prompt):  # Tests input against a number of regex patterns
    # to ensure it is a valid name
    import re
    while True:
        name = input(prompt)
        if name == '$':
            return 0
        if re.search(r"^[A-Z][a-z]+-[A-Z][a-z]+\s[a-z]+$", name) or\
           re.search(r"\b(Mc|Mac)[A-z][a-z]+", name) or\
           re.search(r"^[A-Z][a-z]+\svan\s(der\s)?[A-Z][a-z]+$", name) or\
           re.search(r"^[A-Z][a-z]+\s[A-Z][a-z]+$", name):
            break  # All valid patterns, rest of patterns are invalid
        elif not re.search(r".", name):
            print("Name cannot be blank, please enter again")
            continue

        elif re.search(r"[0-9]", name):
            print("Numbers are not allowed, please enter again")
            continue

        elif re.search(r"\b[a-z]", name):
            print("Names must start with a capital letter, please enter again")
            continue

        elif re.search(r"\s\s", name):
            print("Two or more spaces are not allowed, please enter again")
            continue

        elif re.search(r"[!@#$%^&*()_+=\[\]{};'\":|,.<>/?]", name):
            print("Special characters are not allowed, please enter again")
            continue

        elif not re.search(r"\A\w+\s\w+$", name) and \
                not re.search(r"\A\w+-?\w+\s\w+-?\w+$", name):
            print("Please enter a first name and a last name")
            continue

        elif re.search(r"\b\w[a-z]*[A-Z]+",
                       name):
            print("No capital letters allowed in the middle of the name,"
                  " please enter again")
            continue

        else:  # If input matches no known 'bad' patterns, theoretically
            # should only happen in the case of non alphanumeric character
            print("Invalid name")
            continue

    assert name is not None, "Referenced before assignment"
    return name


def int_checker(msg):
    # Converts input to int but asks user to confirm before returning
    data = input(msg)
    try:
        data = int(data)
        if data < 1:  # Disallows 0 or below as valid input
            raise ValueError
        confirm = input("Confirm? (y/n) ").lower()
        if confirm == 'y':
            return data
        elif confirm == 'n':
            return int_checker(msg)
        else:
            print(f"{confirm} is not a valid option, please enter again")
            return int_checker(msg)
    except ValueError:  # Catching errors so program doesn't crash
        print(f"{data} is either invalid or not a number, please enter again")
        return int_checker(msg)


def calc_fine(speed):  # Calculates fines
    if speed < 10:
        return 30
    elif speed in range(11, 15):  # Using range instead of 'if speed >= number
        # and speed < number'
        return 80
    elif speed in range(15, 20):
        return 120
    elif speed in range(20, 25):
        return 170
    elif speed in range(25, 30):
        return 230
    elif speed in range(30, 35):
        return 300
    elif speed in range(35, 40):
        return 400
    elif speed in range(40, 45):
        return 510
    elif speed >= 45:
        return 630


def print_statistics(speeders):
    i = 1
    print(f"Total fines: {len(speeders)}")
    for name, _ in speeders.items():
        print(f"{i}) {name}\tAmount over limit: {speeders.get(name)}")
        i += 1


if __name__ == '__main__':
    main()
