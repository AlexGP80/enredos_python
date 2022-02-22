def switch_period(period):
    if period == "AM":
        return "PM"
    return "AM"

def add_time(start, duration, weekday=""):

    weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    num_weekday = 0
    if (weekday):
        num_weekday = weekdays.index(weekday.title())

    new_time = ""

    start_time, start_period = start.split()

    start_hour, start_minute = start_time.split(":")

    duration_hour, duration_minute = duration.split(":")

    gross_minute = int(start_minute) + int(duration_minute)
    result_minute = int(gross_minute%60)
    gross_hour = int(start_hour) + int(duration_hour) + int(int(gross_minute)/60)
    result_hour = int(gross_hour%12)
    if result_hour == 0:
        result_hour = 12
    periods_later = int(gross_hour/12)
    result_period = start_period
    if periods_later%2 != 0:
        result_period = switch_period(start_period)
    extra_period = 0
    if (start_period == "PM"):
        extra_period = 1
    days_later = int((periods_later+extra_period)/2)
    result_num_weekday = (num_weekday + days_later)%7
    if not days_later:
        days_later = ""
    elif days_later == 1:
        days_later = " (next day)"
    else:
        days_later = f" ({days_later} days later)"

    result_weekday = ""
    if (weekday):
        result_weekday = f", {weekdays[result_num_weekday]}"
    # print(str(result_hour) + ":" + str(result_minute) + " " + result_period)


    new_time = f"{result_hour}:{result_minute:02} {result_period}{result_weekday}{days_later}"


    return new_time
