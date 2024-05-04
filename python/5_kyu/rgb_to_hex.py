def rgb(r, g, b):
    red = ""
    if r < 0:
        red = "00"
    elif r > 255:
        red = "ff"
    else:
        red = hex(r)[2:]
        if len(red) < 2:
            red = (2 - len(red)) * "0" + red

    green = ""
    if g < 0:
        green = "00"
    elif g > 255:
        green = "ff"
    else:
        green = hex(g)[2:]
        if len(green) < 2:
            green = (2 - len(green)) * "0" + green

    if b < 0:
        blue = "00"
    elif b > 255:
        blue = "ff"
    else:
        blue = hex(b)[2:]
        if len(blue) < 2:
            blue = (2 - len(blue)) * "0" + blue

    return (red + green + blue).upper()


print(rgb(-20, 275, 125))
