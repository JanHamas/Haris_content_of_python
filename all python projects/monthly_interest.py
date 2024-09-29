def main():
    print("This is a monthly payment loan calculator")
    print()
    
    
    principle = float(input("Enter the loan amount: "))
    rate = float(input("Enter the annual interest rate: "))
    years = int(input("Enter the number of years: "))
    months = years * 12
    rate = rate / 12 / 100

    payment = principle * rate / (1 - (1 + rate)**(-months))

    print() 
    print("The monthly payment is: %.2f" % payment)

main()