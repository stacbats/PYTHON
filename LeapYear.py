# Leap Year by Stacy Bates

#   Leap year
#   Leap year has 366 days non leap is 365
#   Criteria
#   Needs to be / 4 evenly, except every year / 100 unless year is also / 400.


Year = int(input("Which year do you want to check? "))

if Year % 4 == 0:
    if Year % 100 == 0:
        if Year % 400 == 0:
            print ("Leap Year")
        else:
            print(" Not a Leap Year")
    else:
        Print("Leap Year")

else:
    print(" Not a Leap Year")
            

