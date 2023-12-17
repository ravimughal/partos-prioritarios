#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 141
# 62504 Ravi Mughal 
# 62496 Vitor Augusto

import dateTime
from constants import *



def writeScheduleFile(sched, header, fileName):
    """
    Writes a collection of scheduled birth assistances into a file.

    Requires:
    sched is a list with the structure as in the output of
    planning.updateSchedule representing the cruises assigned;
    header is a string with a header, as in the examples provided in 
    the general specification (omitted here for the sake of readability);
    fileName is a str with the name of a .txt file.
    Ensures:
    writing of file named fileName representing the birth assistances in schedule,
    one per line, as organized in the examples provided
    in the general specification (omitted here for the sake of readability); 
    the lines in this file keeps the ordering top to bottom of 
    the assistances as ordered head to tail in sched.
    """
    with open(fileName, 'w', encoding='utf-8') as file:
        
        file.write(header)
        for row in sched:
            line = ', '.join(map(str, row))
            file.write(line + '\n')
        
        


def formatNameFile(file):
    """
    Formats the file name, replacing the current time with the updated time.

    Args:
        file (str): The file name to be formatted.

    Returns:
        str: The formatted file name.

    Raises:
        ValueError: If the time cannot be extracted from the file name.
    """
    currentTime = dateTime.extractTime(file)

    if currentTime:
        newTime = dateTime.sumHours(currentTime, TIME_30_MIN)
        newFile = file.replace(currentTime, newTime)

        return newFile
    else:
        raise ValueError("Erro: Não foi possível extrair o horário do nome do arquivo.")
        

def writeDoctorsFile(doctors, header, fileName):
    """
    Writes a list of doctors to a TXT file.

    Args:
        doctors (list): The list of doctors to be written to the file.
        header (str): The header row for the TXT file.
        fileName (str): The name of the TXT file to be written.
    """
    with open(fileName, 'w', encoding='utf-8') as file:
        file.write(header)

        for row in doctors:
            line = ', '.join(map(str, row))
            file.write(line + '\n')
