## To find speed --
from sys import stdout


def distance_time():
    distance= int(input("Enter distance :"))
    time =  int(input("Enter time :"))
    speed = distance/time
    print(f"The speed is {speed}")

## To find distance --
def speed_time():
    speed= int(input("Enter speed :"))
    time =  int(input("Enter time :"))
    distance = speed * time
    print(f"The Distance is {distance} Km")
    print("Done")

## To find time --
def speed_distance():
    speed= int(input("Enter speed :"))
    distance =  int(input("Enter distance :"))
    time = distance/speed
    print(f"The Distancetime is {time} Km")
    print("Done")

s_d_t= input("""Enter what do you want to do 
\na for distance and time into speed 
\nb for speed and time into distance 
\nc for speed and distance into time: """)
if s_d_t == 'a':
    distance_time()
elif s_d_t == 'b':
    speed_time()
elif s_d_t == 'c':
    speed_distance()