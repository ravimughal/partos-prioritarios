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


def timeToDailyPause(time):
    """
    Calculates the time remaining until the next break based on the 
    current time in minutes
    
    Parameters:
    - time (int): The current time in minutes

    Returns:
    int: The time remaining until the next break. If the current time
    is 240 minutes or more, returns the diference between 480 minutes
    and the current time. Otherwise, return the difference between 240
    minutes and the current time.
    """
    time = int(time)
    
    if time >= 240:
        return 480 - time
    else:
        return 240 - time

def timeToWeeklyPause(time):
    """
    Calculates the accumulated time until the next weekly break based on 
    the current time in minutes

    Parameters:
    - time (str): The current time in 'hh:mm' format.

    Retorna:
    int: The accumulated time until the next weekly break in minutes
    """
    time = timeToMinutes(time)

    return time

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
    print(timeToDailyPause(440))