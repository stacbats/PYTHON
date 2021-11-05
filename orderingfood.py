# python coding


print ("Welcome to Python Pizza Deliveries!")

# variables

size = input(" What size pizza do want?  S, M, or L ")
add_pepperoni = input(" Do you want Pepperoni?  Y or N ")
extra_cheese = input("Do you want extra cheese?  Y or N ")

# now to execute programme

bill = 0

if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25
    
# add pepperoni
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# add cheese

if extra_cheese == "Y":
    bill += 1

# provide total
print(f"Your final price is $ {bill}")
    
