#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 141
# 62504 Ravi Mughal 
# 62496 Vitor Augusto

import infoFromFiles
import dateTime
from constants import *

def updateSchedule(doctors, requests, previousSched, nextTime):
    
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
    shorterTime(doctors, nextTime) #If the available doctor's schedule is before the nexTime schedule, update the schedule
    request_order = priorityRequests(requests)
    doctors_order = priorityDoctors(doctors)

    combinations = combinationsDocRequest(doctors_order, request_order, nextTime)
    previousSched.extend(combinations)
    rmvShorterTimePreviousSched(previousSched, nextTime)
    previousSched = priorityTimeSched(previousSched)
    return previousSched


def priorityTimeSched(previousSched):
    """
    Sorts a list of events based on time and month name.

    The ordering is carried out considering two keys:
    1. The event time converted to minutes, where events with a shorter time
    have priority (e.g. less time for daily breaks).
    2. The name of the month in lexicographic order.

    Parameters:
    - previousSched (list): A list of events, where each event contains information 
    such as the time (SCHED_TIME) and the name of the month (SCHED_NAME_MOTH).

    Returns:
    list: A new list of events ordered based on defined rules.
    """
    ordened_time = sorted(
        previousSched, key=lambda x: (
            int(dateTime.timeToMinutes(x[SCHED_TIME])),  # less time for daily breaks
            x[SCHED_NAME_MOTH]  # lexicographic order
        )
    )
    return ordened_time

def rmvShorterTimePreviousSched(previousSched, nextTime):
    """
    Removes events from the `previousSched` list whose time is less than the
    specified time.
   
    Parameters:
    - previousSched (list): A list of events
    - nextTime (str): The next time to consider for removing events, in the format 'HHhMM'.

    Returns:
    list: A new list of events after removing events whose time is less than `nextTime`.
    """
    previousSched_copy = previousSched.copy()
    for sched in previousSched_copy:
        if dateTime.timeToMinutes(sched[SCHED_TIME]) < dateTime.timeToMinutes(nextTime):
            previousSched.remove(sched)
    return previousSched

def shorterTime(doctors, nextTime):
    """
    Updates the delivery time of doctors whose current delivery time is earlier
    than the next one specified time. If the doctor's free time is before the next
    specified time, the doctor's next time is updated to the next specified time.

    Parameters:
    - doctors (list): A list of doctors, where each doctor is represented by a list.
    Each doctor list must have a specific index (DOCT_CHILDBIRTH_IDX) containing
    your current delivery time.
    - nextTime (int): The next delivery time to be considered, in minutes.

    Modifications:
    - The function updates the delivery time (DOCT_CHILDBIRTH_IDX ​​index) of doctors in the list
    whose current delivery time is less than the next specified time. If free time
    before the next specified time, the doctor's next time is updated for the next specified time.

    Returns:
    None
    """
    nextTimeMinutes = dateTime.timeToMinutes(nextTime)
    for doctor in doctors:
        timeMinutes = dateTime.timeToMinutes(doctor[DOCT_CHILDBIRTH_IDX])
        if timeMinutes < nextTimeMinutes:
            doctor[DOCT_CHILDBIRTH_IDX] = nextTime
    
    return

def priorityDoctors(doctors):
    """
    Sorts the list of doctors based on delivery time availability and priority
    criteria.
    
    Parameters:
    - doctors (list): A list of doctors containing information from multiple doctors

    Returns:
    - list: The list of doctors sorted based on delivery time availability and priority
    criteria.
    """
    final_list = doctors

    # Orders doctors by first available and considering the tiebreaker criteria
    ordened_time = sorted(
        final_list, key=lambda x: (
            dateTime.timeToMinutes(x[DOCT_CHILDBIRTH_IDX]),
            -int(x[DOCT_CATEGORY_IDX]),  # descending category
            -int(dateTime.timeToDailyPause(x[DOCT_DAILYWORK_IDX])),  # less time for daily breaks
            int(dateTime.timeToWeeklyPause(x[DOCT_WEEKLYWORK_IDX])),
            
            x[DOCT_NAME_IDX] # lexicographic order
        )
    )
    
    index_to_move = None
    for i, sublist in enumerate(ordened_time):
        if 'weekly leave' in sublist:
            index_to_move = i
            break

    if index_to_move is not None:
        ordened_time.append(ordened_time.pop(index_to_move))


    return ordened_time


def combinationsDocRequest(doctors, requests, nexTime):
    """
    Generates combinations of orders from mothers with doctors, avoiding doctors
    on weekly breaks.
  
    Parameters:
    - doctors (list): A list of doctors containing information from multiple doctors.
    - requests (list): A mother order list containing information from multiple mothers.

    Returns:
    - list: A list of combinations containing information about the delivery time,
    the mother's name and the doctor's name.
    """
    combinations = []

    for mother in requests:
        for doctor in doctors: 
            if isWklPause(doctor) == True: #If doctor is on weekly break, we will ignore
                combinations.append([nexTime, mother[MOTH_NAME_IDX], 'redirected to other network'])
                break
            elif mother[MOTH_RISK_IDX] == 'high' and int(doctor[DOCT_CATEGORY_IDX]) >= 2:
                combinations.append([doctor[DOCT_CHILDBIRTH_IDX],mother[MOTH_NAME_IDX], doctor[DOCT_NAME_IDX]])
                doctors = updateDoctors(doctor, doctors)
                break
            elif mother[MOTH_RISK_IDX] == 'high' and int(doctor[DOCT_CATEGORY_IDX]) < 2:
                combinations.append([nexTime, mother[MOTH_NAME_IDX], 'redirected to other network'])
                break
            elif mother[MOTH_RISK_IDX] != 'high':
                combinations.append([doctor[DOCT_CHILDBIRTH_IDX],mother[MOTH_NAME_IDX], doctor[DOCT_NAME_IDX]])
                doctors = updateDoctors(doctor, doctors)
                break

            
    return combinations

def updateDoctors(doctor, doctors):
    """
    Updates a doctor's information and rearranges the list of doctors with 
    the updates.
   
    Parameters:
    - doctor (list): A list representing the doctor information that will be updated
    - doctors (list): A list of doctors containing information from multiple doctors

    Returns:
    - list: The 'doctors' list updated after changes.
    """
    #print(doctor[DOCT_CHILDBIRTH_IDX], doctor[DOCT_NAME_IDX])
    doctor[DOCT_CHILDBIRTH_IDX] = dateTime.sumHours(doctor[DOCT_CHILDBIRTH_IDX], HOUR_CHILDBIRTH) #Update the doctor's new available hours
    #print(doctor[DOCT_CHILDBIRTH_IDX], doctor[DOCT_NAME_IDX])

    doctor[DOCT_DAILYWORK_IDX] = int(doctor[DOCT_DAILYWORK_IDX]) + MIN_CHILDBIRTH #adds 20 minutes of daily work
    doctor[DOCT_WEEKLYWORK_IDX] = dateTime.sumHours(doctor[DOCT_WEEKLYWORK_IDX], HOUR_CHILDBIRTH) # totals 20 minutes of weekly work

    doctor = checkDoctors(doctor) #checks whether there will be a daily break or weekly break
    doctors = priorityDoctors(doctors) #reorganizes the list of doctors with updates
    return doctors

def checkDoctors(doctor):
    """
    Check whether the doctor is on daily or weekly break time and performs
    the corresponding actions.

    Parameters:
    - doctor (list): A list representing the doctor's information, where
    DOCT_DAILYWORK_IDX and DOCT_WEEKLYWORK_IDX are the indices which contain
    information about daily and weekly working time respectively.
      
    Returns:
    - list: The 'doctor' list modified with corresponding actions applied.
    """

    if doctor[DOCT_DAILYWORK_IDX] >= 240 and doctor[DOCT_DAILYWORK_IDX] < 260:
        doctor[DOCT_CHILDBIRTH_IDX] = dateTime.sumHours(doctor[DOCT_CHILDBIRTH_IDX], BREAK_TIME)
    
    hour = dateTime.timeToMinutes(doctor[DOCT_WEEKLYWORK_IDX])
    if hour >=  WKL_WORK:
        doctor[DOCT_CHILDBIRTH_IDX] = WKL_PAUSE
    
    return doctor
    
def isWklPause(doctor):
    """
    Check if the doctor is on a weekly break

    Parameters:
    - doctor (list): A list representing the doctor's information, where
    DOCT_WEEKLYWORK_IDX is the index that contains information about the
    weekly break.

    Returns:
    - bool: True if the doctor is on a weekly break, False otherwise
    """
    if doctor[DOCT_CHILDBIRTH_IDX] == WKL_PAUSE:
        return True
    return False

def priorityRequests(requests):
    
    """
    Organizes a list of sublists with risk informations and bracelet by 
    priority.
    The function receives a list of sublists, where each sublist contains 
    informations.
    Risk information is in index 3 and bracelet information is in index 2.
    The function organizes a list into tree risk categories: 'high', 
    'medium' and 'low';
    Then, organize each category by bracelet value in descending order.
    
    Parameters:
    - list: A list of sublists containing information. 
    Each sublist must have at least indexes 2 (bracelet) and 3 (risk).
   
    Returns:
    A list organized in order of priority, first by risk and then by bracelet color
    
    """

    high_risk_list = []
    medium_risk_list = []
    low_risk_list = []
    PRIORITY_COLOR = ['red', 'yellow', 'green']
    final_list = []

    for sublist in requests:
        if MOTH_RISK_IDX < len(sublist):
            risk = sublist[MOTH_RISK_IDX]
            if risk == 'high':
                high_risk_list.append(sublist)
            elif risk == 'medium':
                medium_risk_list.append(sublist)
            elif risk == 'low':
                low_risk_list.append(sublist)

    # bracelet order: red > yellow > green
    high_risk_list = sorted(
        high_risk_list, key=lambda x: (
            x[MOTH_RISK_IDX],  # risk in ascending order
            PRIORITY_COLOR.index(x[MOTH_BRACELET_IDX]),  # bracelet priority
            -int(x[MOTH_BRACELET_IDX]) if x[MOTH_BRACELET_IDX].isdigit() else 0,  # age in descending order
            x[MOTH_NAME_IDX]  # lexicographic order
        )
    )
    medium_risk_list = sorted(
        medium_risk_list, key=lambda x: (
            x[MOTH_RISK_IDX],
            PRIORITY_COLOR.index(x[MOTH_BRACELET_IDX]),  # bracelet priority
            -int(x[MOTH_BRACELET_IDX]) if x[MOTH_BRACELET_IDX].isdigit() else 0,  # age in descending order
            x[MOTH_NAME_IDX]
        )
    )
    low_risk_list = sorted(
        low_risk_list, key=lambda x: (
            x[MOTH_RISK_IDX],
            PRIORITY_COLOR.index(x[MOTH_BRACELET_IDX]),  # bracelet priority
            -int(x[MOTH_BRACELET_IDX]) if x[MOTH_BRACELET_IDX].isdigit() else 0,  # age in descending order
            x[MOTH_NAME_IDX]
        )
    )

    # Adds tiebreaker criteria for lexicographic name
    final_list.extend(high_risk_list)
    final_list.extend(medium_risk_list)
    final_list.extend(low_risk_list)

    return final_list

def checkExtension(files):
    """
    Checks the extension of files in the list. If a file does not have the
    extension '.txt', automatically adds the '.txt' extension. Returns the
    updated list of files. 

    Parameters:
    - files (list): List of file names.

    Retorna:
    list: Updated list of filenames with '.txt' extension.
    """
    new_files = []
    for file in files:
        if not file.endswith('.txt'):
            file += '.txt'
        new_files.append(file)
    return new_files
    