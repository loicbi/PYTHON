# Python3 code to demonstrate working of
# Replace dictionary value from other dictionary
# Using loop

# initializing dictionary
test_dict = {"Gfg": 5, "is": 8, "Best": '1dd\'0', "for": 8, "Geeks": 9}

# printing original dictionary
print("The original dictionary is : " + str(test_dict))

# initializing updict
updict = {"Gfg": 10, "Best": 17}

for sub in test_dict:

    # checking if key present in other dictionary
    if sub in updict:
        test_dict[sub] = updict[sub]

# printing result
print("The updated dictionary: " + str(test_dict))
