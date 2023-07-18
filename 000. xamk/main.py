year = int(input("Enter year: "))
# b = int(input("Enter another number: "))
# c = int(input("Enter another number: "))

if year % 400 == 0:
    print("leap year")
elif year % 4 == 0 and year % 100 != 0:
    print("leap year")
else:
    print("not leap year")
