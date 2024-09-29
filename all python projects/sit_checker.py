import urllib.request as urllib

def main(url):
    
    print("checking conectivity")
    
    response = urllib.urlopen(url)
    print("conected to",url,"succusfully")
    print("The response cod was: ",response.getcode())
    
print("this is a site conectivity program")

input_url = input("Enter the site url you want to check: ")

main(input_url)