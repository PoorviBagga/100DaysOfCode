print("Welcome to the tip calculator.")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill? "))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
total = (tip*bill)/100 + bill
amount = round(total/people,1)
print(f"Each person should pay:  ${amount}")
