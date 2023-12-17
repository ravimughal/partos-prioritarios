#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 141
# 62504 Ravi Mughal 
# 62496 Vitor Augusto

import re
from constants import *

def extractTime(filename):
    """
    Extracts the time from the filename using regular expressions.

    Args:
        filename: The filename to extract the time from.

    Returns:
        Optional[str]: The extracted time string if found, otherwise None.
    """
    match = re.search(r'(\d{1,2}h\d{2})', filename)
    if match:
        return match.group(1)
    else:
        raise ValueError(f"File name {filename} doesn't match the expected time pattern")

def getTime(filename):
    """
    Retrieves the time from the specified file.

    Args:
        filename (str): The filename from which to extract the time.

    Returns:
        str: The extracted time string.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        time = lines[NUM_TIME_LINE].strip()
    
    return time

def checkTime(filename):
    """
    Verifies that the filenames match the time information in their headers.

    Args:
        filenames (list(str)): A list of filenames to check.

    Raises:
        ValueError: If the header time doesn't match the filename.
    """
    for i in filename:
        timeHeader = getTime(i)
        timeNameFile = extractTime(i)
        if timeHeader != timeNameFile:
            raise ValueError(f"File name {i} doesn't match the time in the header: expected {timeNameFile}, actual {timeHeader}")




def hourToInt(time):
    """
    Extracts the hour component from a time string and converts it to an integer.

    Args:
        time (str): The time string to process.

    Returns:
        int: The extracted hour as an integer.
    """
    t = time.split("h")
    return int(t[0])

def minutesToInt(time):
    """
    Extracts the minutes component from a time string and converts it to an integer.

    Args:
        time (str): The time string to process.

    Returns:
        int: The extracted minutes as an integer.
    """
    t = time.split("h")
    return int(t[1])
    

def timeToMinutes(time):
    """
    Converts a time string to the corresponding number of minutes.

    Args:
        time (str): The time string to convert.

    Returns:
        int: The corresponding number of minutes.
    """
    if time == 'weekly leave':
        return 9999999
    hour = hourToInt(time)
    minutes = minutesToInt(time)
    return (hour * 60 + minutes)

def minutesToHour(minutes):
    """
    Converts a total number of minutes into a formatted time string in the style "HHhMM".

    Parameters:
    - minutes (int): The total number of minutes to be converted.

    Returns:
    - formato_horas (str): A formatted time string representing the total minutes as "HHhMM".
    """
    horas = minutes // 60
    minutos_restantes = minutes % 60

    # Formata a string no estilo HHhMM
    formato_horas = "{:02}h{:02}".format(horas, minutos_restantes)

    return formato_horas

def sumHours(time1, time2):
    """
    Sums two time values in the format "HHhMM" and returns the result as a formatted time string.

    Parameters:
    - time1 (str): A time string in the format "HHhMM".
    - time2 (str): Another time string in the format "HHhMM".

    Returns:
    - sumTimeString (str): A formatted time string representing the sum of time1 and time2.
    """
    total_minutes = timeToMinutes(time1) + timeToMinutes(time2)
    return minutesToHour(total_minutes)

def timeToDailyPause(time):
    """
    Calcula o tempo restante até a próxima pausa com base no tempo atual em minutos.

    Parâmetros:
    - time (int): O tempo atual em minutos.

    Retorna:
    int: O tempo restante até a próxima pausa. Se o tempo atual for igual ou superior a 240 minutos,
    retorna a diferença entre 480 minutos e o tempo atual. Caso contrário, retorna a diferença
    entre 240 minutos e o tempo atual.
    """
    time = int(time)
    if time >= 240:
        return 480 - time
    else:
        return 240 - time

def timeToWeeklyPause(time):
    """
    Calculates the accumulated time until the next weekly break based on the current time in minutes.

    Parameters:
    - time (str): The current time in the format 'HHhMM'.

    Returns:
    int: The accumulated time until the next weekly break in minutes.
    """
    
    tempoTotal = timeToMinutes(time)
    return tempoTotal

def intToTime(hour, minutes):
    """
    Converts integers representing hours and minutes into a formatted time string.

    Parameters:
    - hour (int): An integer representing the hour (0 to 23).
    - minutes (int): An integer representing the minutes (0 to 59).

    Returns:
    - timeString (str): A formatted time string in the format "HHhMM", where 'hh' is the hour
    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m

if __name__ == '__main__':
    checkTime(['doctors10h00.txt', 'schedule10h00.txt', 'requests10h30.txt'])