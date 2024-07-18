input_string = '''8 15 9 30 19 19 4 58
8 14 18 58 27 18 44 45
3 8 58 31 6 10 4 7
12 15 43 14 16 5 16 48
3 9 17 13 15 6 36 50
14 6 21 38 25 6 12 18
2 7 21 52 6 18 56 48
0 2 48 28 4 13 21 13
10 0 46 44 17 19 57 7
6 12 58 8 11 2 7 17
25 8 20 14 29 17 58 7
20 14 2 13 29 13 55 49
6 1 40 23 15 16 28 14'''

# Split the input string into a list of integers
input_list = list(map(int, input_string.split()))

time_differences = []

#break the list into timestamps, first 4 is start time, last 4 is end time
for i in range(0, len(input_list), 8):
    day1, hour1, min1, sec1, day2, hour2, min2, sec2 = input_list[i:i + 8]

#calculate the time difference
    time_difference_days = day2 - day1
    time_difference_hours = hour2 - hour1
    time_difference_minutes = min2 - min1
    time_difference_seconds = sec2 - sec1

    # if sec difference is less than 0, increase seconds and reduce minutes
    if time_difference_seconds < 0:
        time_difference_seconds += 60
        time_difference_minutes -= 1
    #if min difference is less than 0, increase min and reduce hours
    if time_difference_minutes < 0:
        time_difference_minutes += 60
        time_difference_hours -= 1
    # if hour difference is less than 0, increase minutes and reduce hour, also if hour >24 add into days
    if time_difference_hours < 0:
        time_difference_hours += 24
        time_difference_days -= 1

#output should be a list of tuples, and is printed
    time_differences.append("({} {} {} {})".format(time_difference_days, time_difference_hours, time_difference_minutes,time_difference_seconds))


print(*time_differences)