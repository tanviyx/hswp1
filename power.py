import math


while True:
    base=int(input("Please enter the base number: "))
    exponent=int(input("Please enter the power: "))

    power=math.pow(base, exponent)

    print (base, "raised to the power",exponent, "=", power)
    print ("________________________________")

    ch=input("Do you wish to continue? 1-->Yes 2-->No ")
    if ch=="2":
        break
             
