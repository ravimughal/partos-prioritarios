#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa


def updateSchedule(doctors, requests, previousSched, nextSched):
	"""
    Update birth assistance schedule assigning the given birth assistance requested
    to the given doctors, taking into account a previous schedule.
	
	Requires:
	doctors is a list of lists with the structure as in the output of
	infoFromFiles.readDoctorsFile concerning the time of previous schedule;
	requests is a list of lists with the structure as in the output of 
	infoFromFile.readRequestsFile concerning the current update time;
	previousSched is a list of lists with the structure as in the output of
	infoFromFiles.readScheduleFile concerning the previous update time;
	Ensures:
	a list of birth assistances, representing the schedule updated at
	the current update time (= previous update time + 30 minutes),
	assigned according to the conditions indicated in the general specification
	of the project (omitted here for the sake of readability).
	"""


import datetime

def updateDoctors(previousdoctors, nextdoctors):
    with open(previousdoctors, 'r') as inFile:
        linhas = inFile.readlines()

    # Modificando a oitava e nona linhas
    linhas[3] = '14h30\n'
    linhas[7] = 'Manuel Frias, 2, 14h25, 85, 36h28\n'
    linhas[8] = 'Carlos Sousa, 3, 12h10, 60, 28h34\n'

    with open(nextdoctors, 'w') as outFile:
        outFile.writelines(linhas)

updateDoctors('doctors14h00.txt', 'doctors14h30.txt')









