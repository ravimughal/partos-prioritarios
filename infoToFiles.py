#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa

import planning
import infoFromFiles
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
    current_time = dateTime.extractTime(file)

    if current_time:
        new_time = dateTime.sumHours(current_time, TIME_30_MIN)
        new_file = file.replace(current_time, new_time)

        return new_file
    else:
        print("Erro: Não foi possível extrair o horário do nome do arquivo.")
        return None

formatNameFile('schedule10h00.txt')

def writeDoctorsFile(doctors, header, fileName):
    pass

if __name__ == '__main__':
    doctors_data = infoFromFiles.readDoctorsFile('doctors10h00.txt')
    requests_data = infoFromFiles.readRequestsFile('requests10h30.txt')    
    schedule_data = infoFromFiles.readScheduleFile('schedule10h00.txt')
    time_file = infoFromFiles.getTime('schedule10h00.txt')
    nextTime = dateTime.sumHours(time_file, TIME_30_MIN)
    sched = planning.updateSchedule(doctors_data, requests_data, schedule_data, nextTime)
    header = infoFromFiles.getHeader('schedule10h00.txt')
    newFileName = formatNameFile('schedule10h00.txt')
    writeSchedule = writeScheduleFile(sched, header, newFileName)