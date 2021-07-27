"""
Mcree: High Noon

Author : Sreyeesh Garimella 

Get the time when it's high noon somewhere in the world. This is fan made app for Overwatch !


"""

  
from datetime import datetime
import pytz
import time
from playsound import playsound



utc = pytz.utc

# this is already list of  all time zones and not the actual time.

world_timezones = pytz.all_timezones
# now = datetime.now()

now = datetime.now()
the_time = now.strftime("%H:%M %p")
print("Current Time = ",the_time)

# print(len(world_timezones))
# print(world_timezones[0:359])
# print(type(world_timezones))

for t in world_timezones[0:359]:
    print(t)
    current_time = datetime.now(pytz.timezone(t)).strftime('%H:%M %p')
    
    if current_time in world_timezones[0:359] == '12:00 PM':
        playsound('high_noon.mp3')
        # print("It\'s {t} high noon.")
        print(f"In {t} it\'s {current_time} high noon.")
       
           
    else:
        # print("It ain\'t my  time.")
        playsound('My_Time.mp3')
        print(f"In {t} ain\'t {current_time} my time")
    
        
        # print('prepare to attack.')
    
    
 