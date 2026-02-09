# Problem: String Validators
# Difficulty: Easy
'''You are given a string S.
Your task is to find out if the string S contains: alphanumeric characters, alphabetical characters, digits, lowercase and uppercase characters.'''

if __name__ == '__main__':
    s = input()
    e="False"
    for i in s:
        if i.isalnum():
            e="True"
    print(e)
    c="False"
    for i in s:
        if i.isalpha():
            c="True"
    print(c)
    d="False"
    for i in s:
        if i.isdigit():
            d="True"
    print(d)
        
    a='False'
    for i in s:
        if i.islower():
            a="True"
        
    print(a)
    b="False"
    for i in s:
        if i.isupper():
            b="True"
    print(b)
