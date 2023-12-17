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
     
    request_order = priorityRequests(requests)
    doctors_order = priorityDoctors(doctors)
    return [request_order, doctors_order]

def priorityDoctors(doctors):
    final_list = doctors

    # ordena médicos por primeiro disponível e considerando os critérios de desempate
    ordened_time = sorted(
        final_list, key=lambda x: (
            dateTime.timeToMinutes(x[DOCT_CHILDBIRTH_IDX]),
            -int(x[DOCT_CATEGORY_IDX]),  # categoria decrescente
            -int(dateTime.timeToDailyPause(x[DOCT_DAILYWORK_IDX])),  # menos tempo para pausa diaria
            -int(dateTime.timeToWeeklyPause(x[DOCT_WEEKLYWORK_IDX])),  # menos tempo para pausa semanal
            x[DOCT_NAME_IDX]  # ordem lexicográfica
        )
    )

    return ordened_time

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

    # ordem das pulseiras: red > yellow > green
    high_risk_list = sorted(
        high_risk_list, key=lambda x: (
            x[MOTH_RISK_IDX],  # risco em ordem crescente
            PRIORITY_COLOR.index(x[MOTH_BRACELET_IDX]),  # prioridade da pulseira
            -int(x[MOTH_BRACELET_IDX]) if x[MOTH_BRACELET_IDX].isdigit() else 0,  # idade em ordem decrescente
            x[MOTH_NAME_IDX]  # ordem lexicográfica
        )
    )
    medium_risk_list = sorted(
        medium_risk_list, key=lambda x: (
            x[MOTH_RISK_IDX],
            PRIORITY_COLOR.index(x[MOTH_BRACELET_IDX]),  # prioridade da pulseira
            -int(x[MOTH_BRACELET_IDX]) if x[MOTH_BRACELET_IDX].isdigit() else 0,  # idade em ordem decrescente
            x[MOTH_NAME_IDX]
        )
    )
    low_risk_list = sorted(
        low_risk_list, key=lambda x: (
            x[MOTH_RISK_IDX],
            PRIORITY_COLOR.index(x[MOTH_BRACELET_IDX]),  # prioridade da pulseira
            -int(x[MOTH_BRACELET_IDX]) if x[MOTH_BRACELET_IDX].isdigit() else 0,  # idade em ordem decrescente
            x[MOTH_NAME_IDX]
        )
    )

    # Adiciona critério de desempate para nome lexicográfico
    final_list.extend(high_risk_list)
    final_list.extend(medium_risk_list)
    final_list.extend(low_risk_list)

    print('Final List:', final_list)

    return sorted(final_list, key=lambda x: x[MOTH_NAME_IDX])

if __name__ == '__main__':
    doctors_data = infoFromFiles.readDoctorsFile('doctors10h00.txt')
    requests_data = infoFromFiles.readRequestsFile('requests10h30.txt')
    
    schedule_data = infoFromFiles.readScheduleFile('schedule10h00.txt')
    result = updateSchedule(doctors_data, requests_data, schedule_data, 2)
    request_order = result[0]
    doctors_order = result[1]