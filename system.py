# python script showing battery details 
import psutil 

#gives battery information
def battery_info():
# returns a tuple 
    battery = psutil.sensors_battery() 
    return(battery.percent, battery.power_plugged) 

def current_sys():
    # gives a single float value
    c = psutil.cpu_percent()
    # you can have the percentage of used RAM
    ur = psutil.virtual_memory().percent
    # you can calculate percentage of available memory
    fr = round(psutil.virtual_memory().available * 100 / psutil.virtual_memory().total)
    return(c,ur,fr)
