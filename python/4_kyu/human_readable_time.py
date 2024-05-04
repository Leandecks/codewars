def format_duration(seconds):
    if seconds == 0:
        return "now"

    seconds_year = 31536000
    seconds_day = 86400
    seconds_hour = 3600
    seconds_minute = 60

    years = str(seconds // seconds_year)
    days = str(seconds % seconds_year // seconds_day)
    hours = str(seconds % seconds_year % seconds_day // seconds_hour)
    minutes = str(seconds % seconds_year % seconds_day % seconds_hour // seconds_minute)
    secs = str(seconds % seconds_year % seconds_day % seconds_hour % seconds_minute)

    time = [
        ["years", years],
        ["days", days],
        ["hours", hours],
        ["minutes", minutes],
        ["seconds", secs]
    ]

    time = [t for t in time if t[1] != "0"]
    time = [[k[0][:-1], k[1]] if k[1] == "1" else [k[0], k[1]] for k in time]

    result = ""

    for k in range(len(time)):
        if k == len(time) - 1:
            result += time[k][1] + " " + time[k][0]
        elif k == len(time) - 2:
            result += time[k][1] + " " + time[k][0] + " and "
        else:
            result += time[k][1] + " " + time[k][0] + ", "

    return result


print(format_duration(132030240))
