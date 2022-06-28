
import pandas as pd
import pickle
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
#with this json format, its pretty easy to do calculations row wise but quite a challenge to do column wise calculations
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

#reorganizing the dictionary above
houses_columnwise = {
    "price_aprox_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}
#storing data in dictionary of lists
clothes = {"shirt": ["red", "M"], "sweater": ["yellow", "L"], "jacket": ["black", "L"]}
pd.DataFrame.from_dict(clothes)

#Pickle files, used in serializing and deserializing
#serializing is the process of turning an object in memory into a stream of bytes so as you can store it on a disk
#or send it over a network
#This code saves the dictionary as a pickle file in the file path provided. "wb" means we are serializing the file
pickle.dump(clothes, open("D:\python\pycharm\clothes.pkl", "wb"))

#we can read the pickle file from the data storage with the code below. "rb" means we are deserializing the file
with open("D:\python\pycharm\clothes.pkl", "rb") as f:
    unpickled = pickle.load(f)
