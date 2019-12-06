# Program for Baseball Elimination

#  Algorithms Programming Assignment

#  Author - Puneet Soni & Shubham Rohal

# Import the BaseballElimination function from the Baseball elimination package
from BaseballElimination import BaseballElimination

# Main Function
def main():

    # Enter the file name and the input file should exist in the same folder
    # or can refer Input_files folder mention in the package

    print("----------------------------------Program for Baseball Elimination: ----------------------------------\n")

    filename = input("Enter the file name to input the teams: ")

    division = BaseballElimination(filename)

    for team in division.teams():
        if (division.isEliminated(team)):
            print(team)

        else:
            print(team, "is not eliminated")


if __name__ == "__main__":
    main()
