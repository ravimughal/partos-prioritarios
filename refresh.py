#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa

import infoFromFiles
import planning
import dateTime
import sys


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

    doctors_list = infoFromFiles.readDoctorsFile(doctorsFileName)
    request_list = infoFromFiles.readRequestsFile(requestsFileName)
    schedule_list = infoFromFiles.readScheduleFile(scheduleFileName)
    
    lists = planning.updateSchedule(doctors_list, request_list, schedule_list, 1)

    doctors_list = lists[1]
    request_list = lists[0]
    
    print("Doctors: ",doctors_list)
    print("Request: ",request_list)
    return 0

if __name__ == '__main__':
    """
    doctors = sys.argv[1]
    schedule = sys.argv[2]
    requests = sys.argv[3]
    resultado = plan(doctors, schedule, requests)
    """
    
    resultado = plan('doctors10h00.txt','schedule10h00.txt','requests10h30.txt') #testset1
    #resultado = plan('doctors14h00.txt','schedule14h00.txt','requests14h30.txt') #testset2
    #resultado = plan('doctors16h00.txt','schedule16h00.txt','requests16h30.txt') #testset3





    
    


        

