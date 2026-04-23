hr = int(input("Starting time (hours) "))
mins = int(input("Starting time (minutes) "))
dura = int(input("Event duration (minutes) "))

hr = hr + (mins + dura) // 60
mins = (mins + dura) % 60
if hr >= 24:
    hr = hr - 24  
print("Ending time is: ", hr, ":", mins)    
