
import pandas as pd
#list of house price, squaremeters and room numbers
houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

#a for loop to compute price per square meter per house
for house in houses_nested_list:
    price_m2 = house[0]/house[1]
    print(price_m2)

#append the result of the for loop to the original list
house.append(price_m2)

houses_nested_list

#Creating a dictionary

house_0_dict = {
    "price_aprox_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}

#Calculating the price per sqaure meter for house_0_dict and add it to the dictionary under the key "price_per_m2"

#using JSON to store data as a list of dictionaries
houses_rowwise = [
    {
        "price_aprox_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_aprox_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_aprox_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_aprox_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_aprox_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]