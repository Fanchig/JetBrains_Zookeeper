# put your python code here
megan_hours = int(input())
megan_minutes = int(input())
megan_seconds = int(input())

rain_hours = int(input())
rain_minutes = int(input())
rain_seconds = int(input())

print(((rain_hours * 3600) + (rain_minutes * 60) + rain_seconds)
      - ((megan_hours * 3600) + (megan_minutes * 60) + megan_seconds))


# 60 sec in 1 min
# 3600 sec in 60 min
