from datetime import date

d0 = date(1977, 4, 22)
d1 = date(2019, 8, 22)
d2 = date(2077, 4, 22)
delta = d1 - d0
print(delta.days)

print("you are " + str(delta.days) + " days old")

delta2 = d2 -d0

print("you have " + str(delta2.days) + " days left to live")

# print("Today is the %d day of your life") % delta.days