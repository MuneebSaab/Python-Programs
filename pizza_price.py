print("Thank you for choosing Python Pizza Deliveries!")
# Asking for Pizza Type
size = input() # What size pizza do you want? S, M, or L
# Asking to add extra Flavours costing extra money
add_pepperoni = input() # Do you want pepperoni? Y or N
extra_cheese = input() # Do you want extra cheese? Y or N

# Logic Starts
bill = 0
# Only Pizza Prices
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

# Extra Flavours Prices
if add_pepperoni == "Y":
    if size == "S":  # corrected the comparison operator from "=" to "=="
        bill += 2
    else:
        bill += 3
if extra_cheese == "Y":
  bill +=1

print(f"Your final bill is ${bill}.")
