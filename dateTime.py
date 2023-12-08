#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa



def hourToInt(time):
    """

    """
    t = time.split("h")
    return int(t[0])

def minutesToInt(time):
    """

    """
    t = time.split("h")
    return int(t[1])
    

def timeToMinutes(time):
    """
    
    """
    hour = hourToInt(time)
    minutes = minutesToInt(time)
    return (hour * 60 + minutes)


def leftToPause(time):
    time = int(time)
    
    if time >= 240:
        return 480 - time
    else:
        return 240 - time

def intToTime(hour, minutes):
    """

    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m

if __name__ == '__main__':
    print(leftToPause(440))