import re


input_ipv4: str = "123.21.34.0"

pat_ipv4: str = "\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"


if re.findall(pat_ipv4, input_ipv4):
    print(f"The input {input_ipv4} matches the pattern {pat_ipv4}")
else:
    print(f"The input {input_ipv4} doesnt match the pattern {pat_ipv4}")


# But then above pattern also  accepts 012.01.0.0 as a valid IP only but its an invalid one