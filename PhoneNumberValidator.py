import re

input_number: str = input("Please provide a number to check validity : ")

pat_phone_number: str = "[1-9]{1}\d{2}-\d{3}-\d{4}"

if re.search(pat_phone_number, input_number):
    print(f"Given number is a valid phone number: {input_number}")
else:
    print(f"Given number is not a valid phone number: {input_number}")