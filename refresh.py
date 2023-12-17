#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 141
# 62504 Ravi Mughal 
# 62496 Vitor Augusto

import infoFromFiles
import planning
import dateTime
import sys
from constants import *
import infoToFiles




def plan(doctorsFileName, scheduleFileName, requestsFileName):
    """
    Runs the birthPlan application.

    Requires:
    doctorsFileName is a str with the name of a .txt file containing a list
    of doctors at date d and time t, organized as in the examples provided;
    scheduleFileName is a str with the name of a .txt file containing a list
    of birth assistances assigned to doctors at date d and time t, as in the examples provided;
    requestsFileName is a str with the name of a .txt file containing a list
    of cruises requested at date d and time t+30mins;
    Ensures:
    writing of two .txt files containing the updated list of doctors assigned
    to mothers and the updated list of birth assistances, according to 
    the requirements in the general specifications provided (omitted here for 
    the sake of readability);
    these two output files are named, respectively, doctorsXXhYY.txt and
    scheduleXXhYY.txt, where XXhYY represents the time 30 minutes
    after the time t indicated in the files doctorsFileName,
    scheduleFileName and requestsFileName, and are written in the same directory
    of the latter.
    """
    files = [doctorsFileName, scheduleFileName, requestsFileName]
    files = planning.checkExtension(files)
    doctorsFileName = files[0]
    scheduleFileName = files[1]
    requestsFileName = files[2]
    
    dateTime.checkTime(files)

    doctors_data = infoFromFiles.readDoctorsFile(doctorsFileName)
    requests_data = infoFromFiles.readRequestsFile(requestsFileName)    
    schedule_data = infoFromFiles.readScheduleFile(scheduleFileName)
    time_file = dateTime.getTime(scheduleFileName)
    nextTime = dateTime.sumHours(time_file, TIME_30_MIN)
    sched = planning.updateSchedule(doctors_data, requests_data, schedule_data, nextTime)
    header = infoFromFiles.getHeader(scheduleFileName)
    newFileName = infoToFiles.formatNameFile(scheduleFileName)
    infoToFiles.writeScheduleFile(sched, header, newFileName)
    newDoctorsFileName = infoToFiles.formatNameFile(doctorsFileName)
    infoToFiles.writeDoctorsFile(doctors_data, header, newDoctorsFileName)

try: 

    doctorsFile = sys.argv[1]
    scheduleFile = sys.argv[2]
    requestsFile = sys.argv[3]

    plan(doctorsFile, scheduleFile, requestsFile)

except FileNotFoundError:
    print("File Not Found")
    ascii_file_not_found = [
    "  ______ _ _        _   _       _     ______                    _ ",
    " |  ____(_) |      | \\ | |     | |   |  ____|                  | |",
    " | |__   _| | ___  |  \\| | ___ | |_  | |__ ___  _   _ _ __   __| |",
    " |  __| | | |/ _ \\ | . ` |/ _ \\| __| |  __/ _ \\| | | | '_ \\ / _` |",
    " | |    | | |  __/ | |\\  | (_) | |_  | | | (_) | |_| | | | | (_| |",
    " |_|    |_|_|\\___| |_| \\_|\\___/ \\__| |_|  \\___/ \\__,_|_| |_|\\__,_|",
    "                                                                  "
]
    for line in ascii_file_not_found:
        print(line)
    
    print(FileNotFoundError('Make sure you follow the python3 refresh.py inputFile1 inputFile2 inputFile3'))
