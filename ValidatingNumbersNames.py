import re

# \w is equalivalent to [a-zA-Z0-9]
# \W is equalivalent to [^a-zA-Z0-9]

input_phn_no_v: str = "111-222-3333"
input_phn_no_iv: str = "a11-bb2-ccc3"

pat1: str = "\d{3}-\d{3}-\d{4}"
pat2: str = "\w{3}-\w{3}-\w{4}"


if re.search(pat1, input_phn_no_v) and re.search(pat2, input_phn_no_iv):
    print(f"{input_phn_no_v} is valid phone number for pattern {pat1}")
    print(f"{input_phn_no_iv} is valid phone number for pattern {pat2}")

else:
    print("Given is invalid")

print(f"{input_phn_no_iv} is invalid phone number for pattern {pat1}")


# \s is equivalent to [\f\n\r\t\v]
# \S is equivalent to [^\f\n\r\t\v]

input_full_name: str = "Ryan Serhant"

pat3: str = "\w{1,20}\s\w{1,20}"
if re.search(pat3, input_full_name):
    print(f"Given string {input_full_name} is a valid one as per patter {pat3}")
else:
    print("A'int a valid Full name")