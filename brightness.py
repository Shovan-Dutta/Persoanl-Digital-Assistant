import screen_brightness_control as sbc

def current():
    current_brightness = sbc.get_brightness()
    return(current_brightness)

def decrease():
    v = current()
    if v >= 10:
        sbc.set_brightness(v-10)
        return("Decreased Brightness")
    else:
        return("Brightness is already at 0 percent")

def increase():
    v = current()
    if v <= 90:
        sbc.set_brightness(v+10)
        return("Increased Brightness ")
    else:
        return("Brightness is already at 100 percent")
