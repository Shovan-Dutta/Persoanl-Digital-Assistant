import datetime
import calendar

# tells the day of the week
def tellday():
    try:
        today = datetime.date.today()
        date = today.strftime("%d %m %Y")
        d = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        s = calendar.day_name[d]
        return(s)
    except Exception:
        return("some error occured")

# tells the current time
def tim():
    try:
        strTime = datetime.datetime.now().strftime("%H:%M:%S") 
        return (strTime)
    except Exception:
        return ("something went wrong")

#tells the date
def dat():
    try:
        today = datetime.date.today()
        d = today.strftime("%B %d, %Y")
        return (d)
    except Exception:
        return("something went wrong")

#tells the hour
def hour():
    try:
        hour = int(datetime.datetime.now().hour)
        return (hour)
    except Exception:
        return("something went wrong")