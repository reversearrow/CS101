# Palindrom Program

def is_palindrome(string):
    if string == "":
        return True

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False
