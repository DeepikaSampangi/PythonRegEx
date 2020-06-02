import re

input_emails: str = "abc@abc.com, xx, xyz@.com, @.com, 123@abc.com, 1@a, 1.com. abc@com"

pat = "[\w.!%-+=]{1,20}@[\w._-]{1,20}.[a-zA-Z]{2,3}"

print("Valid Email Ids list is", re.findall(pat, input_emails))