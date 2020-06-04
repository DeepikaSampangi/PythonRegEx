import re

input_str: str = input("Enter any string to check password strength : ")

# Check occurence of a char more than 3 times
pat_char_occurence: str = "(.)\1\1"

#check occurence of a substring more than once
pat_sub_str_occurence: str = "(..)(.*?)\1"

if re.match('\n', input_str) or re.match(' ', input_str) :
    print("Password cannot contain new line or space ")

if 9 <= len(input_str) <= 20:

    if re.search(pat_char_occurence, input_str):
        print("Weak Passwrod : Chracter repeated more than 3 times")

    if re.search(pat_sub_str_occurence, input_str):
        print("Weak Password : Same substring repeated more than once")
    else:
        print("Strong Password")
else:
    print("Weak password")
