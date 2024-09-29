def leaf_year():
    year = int(input("Enter year: "))
    if year%4==0:
        print("This is a leap year")
    else:
        print("This is not leap year")
while True:
    leaf_year()