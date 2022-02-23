def main():
    item = input("What is the auction for? ")
    reserve_price = float_checker("What is the reserve price? ")
    print(f"\nThe auction for the {item} has started!")
    print("Input -1 to end the bid.")
    highest_bid = 0
    while True:  # Start of bidding
        print(f"The highest bid is ${highest_bid}")
        bid = float_checker("What is your bid? ", confirm=False)
        if bid == -1:  # Ends auction
            print("Auction over")
            if highest_bid >= reserve_price:
                print(f"The {item} was sold for ${highest_bid:.2f}")
            else:
                print(f"The {item} was not sold")
            exit(0)
        if bid > highest_bid:
            highest_bid = bid
        else:
            print("You need to bid higher.")


def float_checker(msg, confirm=True):
    # Converts input to float but can ask user to confirm before returning
    data = input(msg)
    try:
        data = float(data)
        if data < 0 and data != -1:  # Prevents price from being negative
            raise ValueError
        if confirm:
            if input("Confirm? (y/n) ").lower() == 'y':
                return data
            else:
                return float_checker(msg, confirm=confirm)
            # Keeps confirm settings from when the function was last called
        elif not confirm:
            return data
        else:
            print(f"{confirm} is not a valid option, please enter again")
            return float_checker(msg, confirm=confirm)
    except ValueError:  # Catching errors so program doesn't crash
        print(f"{data} is either invalid or not a number, please enter again")
        return float_checker(msg, confirm=confirm)


if __name__ == '__main__':
    main()
