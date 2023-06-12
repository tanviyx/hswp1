#Reciprocal of the entered data

def reciprocal(input):
    try:
        if input == 0:
            print("Invalid fraction: Denominator cannot be zero.")
        else:
            reciprocal = 1/input

    except ValueError:
        print("Invalid input: Please enter integers.")
    return reciprocal 
