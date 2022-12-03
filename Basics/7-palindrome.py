def check_palindrome(phrase):
    return "String is Palindrome" if phrase == phrase[::-1] else "String is not Palindrome"


print(check_palindrome("level"))
print(check_palindrome("book"))
