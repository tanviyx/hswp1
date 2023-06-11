#Reciprocal of the entered data

from fractions import Fraction

def get_reciprocal():
    try:
        numerator = int(input("Enter the numerator: "))
        denominator = int(input("Enter the denominator: "))

        if denominator == 0:
            print("Invalid fraction: Denominator cannot be zero.")
        else:
            reciprocal = Fraction(denominator, numerator)
            print("Reciprocal:", reciprocal)

    except ValueError:
        print("Invalid input: Please enter integers.")

get_reciprocal()
