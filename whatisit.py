while True:
    str = input()
    if str.islower():
        print("This string is lowercase.")
    if str.isupper():
        print("This string is uppercase.")
    if str.isalpha():
        print('This string is alphabetical.')
    if str.isalnum():
        print('This string is alphanumeric.')
    if str.isdecimal():
        print('This string is numeric.')
    if str.isspace():
        print('This string is empty space.')
    if str.istitle():
        print('This string is titular.')
