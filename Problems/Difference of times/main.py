# put your python code here

hours_start = int(input()) * 3600
minutes_start = int(input()) * 60
seconds_start = int(input())

hours_end = int(input()) * 3600
minutes_end = int(input()) * 60
seconds_end = int(input())

final_hours = hours_end - hours_start
final_minutes = minutes_end - minutes_start
final_seconds = seconds_end - seconds_start

total_seconds = final_hours + final_minutes + final_seconds

print(total_seconds)
