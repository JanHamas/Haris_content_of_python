def main():
    print("This is a program that convert dollor to pkr")
    dollor = eval(input("Enter the amount of dollor: "))
    pkr = convert_to_pkr(dollor)
    print("The amount in PKR is: ", pkr)

convert_to_pkr = lambda dollor: dollor * 277.85
main()