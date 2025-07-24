#Palindrome
def palindrome():
    choice = input("""Please choose the option that you desire.
    1. For Word Palindrome. (1)
    2. For Number Palindrome. (2)
    Input your answer: """)


    def palindrome_number():
        num = input("Please input a number: ")
        str_num = str(num)
        if str_num == str_num[::-1]:
            print("The Input is a Palindrome.")
        else:
            print("The Input is not a Palindrome")

    def palindrome_word():
        word = input("Please input a word: ")
        if word == word[::1]:
            print("The Input is a Palindrome")
        else:
            print("The Input is not a Palindrome")


    if choice == "1":
        palindrome_number()
    elif choice == "2":
        palindrome_word()
    else:
        print("Incorrect Input Please Try Again.")

palindrome()


