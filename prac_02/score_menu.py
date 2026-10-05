MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    # Get a valid score before starting the menu
    score = get_valid_score()

    # Display menu and get user's choice
    print(MENU)
    choice = input(">>> ").upper()

    # Keep running until the user chooses Q
    while choice != "Q":

        if choice == "G":
            score = get_valid_score()

        elif choice == "P":
            print(determine_result(score))

        elif choice == "S":
            show_stars(score)

        else:
            print("Invalid choice")

        # Show menu again
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell")


def get_valid_score():
    score = int(input("Enter score (0-100): "))

    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Enter score (0-100): "))

    return score


def determine_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Pass"
    else:
        return "Bad"


def show_stars(score):
    print("*" * score)


main()