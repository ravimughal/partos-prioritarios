#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa

import infoFromFiles

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
    
    
        
    return doctors,requests
        
	
if __name__ == '__main__':
    doctors_data = infoFromFiles.readDoctorsFile('doctors10h00.txt')
    requests_data = infoFromFiles.readRequestsFile('requests10h30.txt')
    result = updateSchedule(doctors_data, requests_data, 1, 2)
                   
    print(result)
	
