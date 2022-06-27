
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

