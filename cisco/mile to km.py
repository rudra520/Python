kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles
kilometers_to_miles = kilometers

miles_to_kilometers *= 1.61
kilometers_to_miles /= 1.62

print(miles, "miles is", round(miles_to_kilometers, 2), "kilometers")
print(kilometers, "kilometers is", round(kilometers_to_miles, 2), "miles")
