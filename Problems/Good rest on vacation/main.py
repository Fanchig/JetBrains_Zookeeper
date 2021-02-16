# put your python code here
duration_in_days = int(input())
daily_food_costs = int(input())
one_way_flight = int(input())
hotel_night = int(input())

print((duration_in_days * daily_food_costs)
      + (duration_in_days * hotel_night - hotel_night)
      + (one_way_flight * 2))