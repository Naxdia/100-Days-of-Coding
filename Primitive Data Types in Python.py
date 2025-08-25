#Tip calculator

print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = float(input("What percentage tip would you like to give? "))
split = int(input("How many people to split the bill? "))

total_bill = bill + (bill * tip / 100)

round(total_bill, 2)

if split == 0:
    print("Number of people cannot be zero.")
elif split == 1:
    print(f"You should pay: ${total_bill}")
else:
    bill_per_person = total_bill / split
    print(f"Each person should pay: ${bill_per_person}")