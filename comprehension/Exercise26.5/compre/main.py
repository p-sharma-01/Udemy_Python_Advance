weather_c ={
'Monday':12,
'Tuesday':14,
'Wednesday':15,
'Thursday':14,
'Friday':21,
'Saturday':22,
'Sunday':24,
}
# Do Not Change the code above
# Write your code below this line
weather_f={day:(9/5)*temp+32 for day,temp in weather_c.items()}
 


# Write your code above this line
# Do Not Change the code below
print(weather_f)