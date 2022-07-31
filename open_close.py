import windowsapps
import os

# to open any windows program
def open(query):
    try:
        result = query.find('open')
        op = query[result+5:]
        windowsapps.open_app(op)
        return(1)
    except Exception:
        return(0)

def close(query):
    try:
        result = query.find('close')
        op = query[result+5:]
        os.system('TASKKILL /F /IM '+ op +'.exe')
        return (1)
    except Exception:
        return(0)