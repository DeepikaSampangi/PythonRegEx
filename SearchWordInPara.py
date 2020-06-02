import re

search_para: str = '''
You are not who you think you are,
you are not what others think you are,
you are what you think others think of you
'''

# The re.search method returns the search object if no occurance returns None
key: str = "you"
res1: object = re.search(key, search_para)
if res1:
    print(f"The input contains \"{key}\" keyword at :{res1.span()}")
else:
    print(f"The input doesnt contain \"you\" keyword:{res1}")


# re.findall returns list of all the occurances of the word if no occurance returns empty list
key: str = "you"
res2: list = re.findall(key, search_para)

if res2:
    print(f"All the occurances of the key {key} in the input are :{res2}")
else:
    print(f"there is no occurance of key {key} in the input :{res2}")


#re.finditer returns a iterable object with the locations of the keyword even if the keyword isnt present
key: str = "you"
res3: object = re.finditer(key, search_para)

if res3:
    for i in res3:
        print(f"{i} Postion at {i.span()}")

    print(f"All the occurances of the key \"{key}\" in the input are  returned as :{res3}")
else:
    print(f"there is no occurance of key {key} in the input :{res3}")
