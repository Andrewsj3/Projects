"""This program keeps track of employee absences. It continually asks the user
to input the employee's full name along with the amount of days off. When the
user enters '$', the program outputs the average days of absence per year per
employee, the employee with the most days absent, those who had no days of
absence, and those who were absent for longer than average.
Jack Andrews
25/2/22
"""


def main():
    import re
    employees = {}
    non_absentees = []
    above_avg_absence = []
    print("Please enter names of employees below along with amount of days "
          "absent.\nEnter $ to terminate input and display statistics.")
    while True:
        try:
            data = input(">>> ").title()
            if data == '$':
                break
            else:
                f_name, s_name, days_absent = data.split()
            # Below regex patterns ensure name entered is valid

            if not days_absent.isdigit():
                print("You must enter a number for days absent.")

            elif re.fullmatch(r"^[A-Z][a-z]+$", f_name) and\
            re.fullmatch(r"^[A-Z][a-z]+$", s_name):
                print("Employee details recorded.")
                days_absent = int(days_absent)
                employees[f"{f_name} {s_name}"] = days_absent
                # Recording employee data
                if days_absent == 0:
                    non_absentees.append(f"{f_name} {s_name}")

            else:
                print("Names are invalid.")

        except ValueError:
            print("You are expected to enter a first name, a last name, "
                  "and the amount of days absent.")

    print_statistics(non_absentees, employees, above_avg_absence)


def avg(__obj):  # Finds average value in list of values
    days = 0
    for _, num in __obj:
        days += num
    if len(__obj) != 0:
        print("The average number of days of absence per year is"
              f" {days / len(__obj):.2f}")
        return days / len(__obj)
    else:
        return 0


def print_statistics(non_absentees, employees, above_avg_absence):
    if len(employees) != 0:
        non_absentees.sort()
        average = avg(employees.items())
        for people, days in employees.items():
            if days > average:
                above_avg_absence.append(people)
        person = max(employees, key=employees.get)
        # Finds person with most days of absence using the key parameter
        print(f"{person} had the most days absent with {employees.get(person)}"
              f" days off.\n")
        print("\nThose who had no days of absence this year were:")
        for everyone in non_absentees:
            print(everyone)
        print("\nThose who were absent for more days than average were:")
        for everyone in above_avg_absence:
            print(everyone)
    else:
        print("No employees entered")


"""Test data
Alice Wonder 6
Simon White 20
Jane Green 0
Ben Blue 8
Maisie Magenta 4
Coral Cool 7
Amanda Apple 0"""


if __name__ == '__main__':
    main()
