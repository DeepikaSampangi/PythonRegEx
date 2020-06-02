import re

input_str: str = "12345"

pat1: str = "\d"
print(f"Number of matches of {pat1} in {input_str} are", len(re.findall(pat1, input_str)))

pat2: str = "\D"
print(f"Number of matches of {pat2} in {input_str} are", len(re.findall(pat2, input_str)))

input_str1: str = "12345D"
print(f"Number of matches of {pat2} in {input_str1} are", len(re.findall(pat2, input_str1)))

pat3: str = "\d{4}"
print(f"Number of matches of {pat3} in {input_str} are", len(re.findall(pat3, input_str)))

input_str2: str = "1 123 12 1234 12345"
pat4: str = "\d{3,4}"
print(f"Number of matches of {pat4} in {input_str2} are", len(re.findall(pat4, input_str2)))
