exam_hour = int(input())
exam_minute = int(input())
arrive_hours = int(input())
arrive_minute = int(input())

exam_minute += exam_hour * 60
arrive_minute += arrive_hours * 60

time_left = exam_minute - arrive_minute

time = ""

if time_left > 30:
    time = "Early"
elif time_left < 0:
    time = "Late"
else:
    time = "On time"

result = ""

hours = abs(time_left) // 60
minutes = abs(time_left) % 60

if hours > 0:
    result += f"{hours}:{minutes:02d} hours"
elif minutes > 0:
    result += f"{minutes} minutes"

if time_left < 0:
    result += " after the start"
elif time_left > 0:
    result += " before the start"

print(time)
print(result)