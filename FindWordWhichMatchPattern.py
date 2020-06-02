import re

input_str: str = "hour, our, tour, pour, sour, thour, ear, fear, dear, year, hear, pear, bear, early, yearly, 3ear, #ear"

# Range of all the small letters
pat1: str = "[a-z]ear"
pat2: str = "[a-z]our"
#Range of all the small letters between a-f
pat3: str = "[a-f]ear"
#Range excluding a set of letter
pat4: str = "[^a-f]ear"

res1: list = re.findall(pat1, input_str)
res2: list = re.findall(pat2, input_str)
res3: list = re.findall(pat3, input_str)
res4: list = re.findall(pat4, input_str)


if res1 and res2 and res3 and res4:
    print(f"Words matching pattern {pat1} are {res1}")
    print(f"Words matching pattern {pat2} are {res2}")
    print(f"Words matching pattern {pat3} are {res3}")
    print(f"Words matching pattern {pat4} are {res4}")
else:
    print(f"No words match the pattern {pat1} and {pat2}")
