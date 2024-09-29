# in this program we used replace function which take two arguments the first one
# is taken for old string that you want to replace with another word 
# and the second one is taken for new string
def word_replacement():
    str1 = "Hay gays how can i help you today"
    word_to_replace = input("enter the replace word ")
    word_replacement = input("enter the word replacemnt")
    print(str1.replace(word_to_replace,word_replacement))
word_replacement()