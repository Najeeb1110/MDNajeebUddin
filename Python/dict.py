#Dictionary
bugatti={
    "brand":"volkswagen",
    "model": "buggatti",
    "year" : 2018,
    "speed": 400,
    "milage": 1.8
}

# assigning keys to a list
keys = bugatti.keys()

# loop to iterate over the keysi
for keys in bugatti:
   #printing values using keys
   print(bugatti[keys])