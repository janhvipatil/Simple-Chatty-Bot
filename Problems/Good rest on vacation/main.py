# put your python code here

days = int(input())
total_food_cost = int(input()) * days
flight_cost = int(input()) * 2
cost_of_hotel = int(input()) * (days - 1)

print(flight_cost + cost_of_hotel + total_food_cost)
