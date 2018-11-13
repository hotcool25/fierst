my_str = str("""all that doth flow we cannot liquid name 
Or else would fire and water be the same:  But that is 
liquid which is moist and wet Fire that property can never get 
Then'tis not cold that doth the fire put out But'tis 
the wet that makes it die. no""")
letter_max = " "
max_val = 0
for letter in "aoiuye":
    countt = my_str.count(letter)
    print(letter, countt)
    if max_val < countt:
        max_val = countt
        letter_max = letter
print(letter_max, "meets", max_val, "tines")
