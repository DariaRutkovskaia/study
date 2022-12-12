print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
people = int(input("How many people to split the bill?"))
tip_percentage = int(input("How much tip would you like to give? 10, 12, or 15? "))/100
total_bill = bill*(1+tip_percentage)
bill_per_person = "{:.2f}".format(round(total_bill/people,2))
print(f"Each person should pay ${bill_per_person}")