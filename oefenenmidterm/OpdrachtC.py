import math

vuurkracht= int(input())
zwaartekracht = int(input())
afstand = int(input())

alpha = math.asin((afstand * zwaartekracht)/(vuurkracht **2)) /2

print("{0:.2f}".format(alpha))