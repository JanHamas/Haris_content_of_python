'''
In Python, the split() method is used to divide a string into a list of substrings based on a specified delimiter (separator). By default, the split() method separates the string at spaces, but you can specify a different delimiter if needed.

'''
def main():
    email_input = input("Enter email: ") #hamasjan@gmail.com
    (username,domain) = email_input.split("@")
    (domain,extention) = domain.split(".")
    print("Username: ",username)
    print("Domain: ",domain)
    print("Extention: ",extention)
    
main()