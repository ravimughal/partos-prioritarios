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

    #ordena médicos por primeiro disponível
    ordened_time = sorted(
        final_list, key=lambda x: (
            dateTime.timeToMinutes(x[DOCT_CHILDBIRTH_IDX]), 
            -int(x[DOCT_CATEGORY_IDX]), #categoria decrescente
            -int(dateTime.timeToDailyPause(x[DOCT_DAILYWORK_IDX])),#menos tempo para pausa diaria
            -int(dateTime.timeToWeeklyPause(x[DOCT_WEEKLYWORK_IDX])), #menos tempo para pausa semanal
            x[DOCT_NAME_IDX] #ordem lexicográfica
            )
        )

    return ordened_time

def combinationsDocRequest(doctors, requests):
    print(requests)

def priorityRequests(requests):
    """
    Organiza uma lista de sublistas com informações de risco e pulseira por prioridade.

    A função recebe uma lista de sublistas, onde cada sublista contém informações.
    As informações de risco estão no índice 3 e as informações da pulseira estão no índice 2.
    A função organiza a lista em três categorias de risco: 'alto', 'médio' e 'baixo'.
    Em seguida, organiza cada categoria pelo valor da pulseira em ordem decrescente.

    Parâmetros:
    - list: Uma lista de sublistas contendo informações. Cada sublista deve ter pelo menos
            os índices 2 (pulseira) e 3 (risco).

    Retorna:
    Uma lista organizada em ordem de prioridade, primeiro por risco e depois por cor da pulseira.
    """
    high_risk_list = []
    medium_risk_list = []
    low_risk_list = []

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
    final_list.extend(high_risk_list)
    final_list.extend(medium_risk_list)
    final_list.extend(low_risk_list)
    

    red_bracelet_list = []
    yellow_bracelet_list = []
    green_bracelet_list = []

    for sublist in final_list:
        if sublist[MOTH_BRACELET_IDX] == 'red':
            red_bracelet_list.append(sublist)
        elif sublist[MOTH_BRACELET_IDX] == 'yellow':
            yellow_bracelet_list.append(sublist)
        elif sublist[MOTH_BRACELET_IDX] == 'green':
            green_bracelet_list.append(sublist)

    
    red_bracelet_list = sorted(red_bracelet_list, key=lambda x: (int(x[1]), 0), reverse=True)
    yellow_bracelet_list = sorted(yellow_bracelet_list, key=lambda x: (int(x[1]), 1), reverse=True)
    green_bracelet_list = sorted(green_bracelet_list, key=lambda x: (int(x[1]), 2), reverse=True)

    #print('Antes de reemanipular: ',final_list)
    ######################################################
    # TRECHO DE CÓDIGO A SER CONCERTADO
    final_list = []

    if len(red_bracelet_list) > 0:
        for sublist in red_bracelet_list:
            if int(sublist[1]) == int(red_bracelet_list[0][1]):
                final_list.append(sublist)

    if len(yellow_bracelet_list) > 0:
        for sublist in yellow_bracelet_list:
            if int(sublist[1]) == int(yellow_bracelet_list[0][1]):
                final_list.append(sublist)

    if len(green_bracelet_list) > 0:
        for sublist in green_bracelet_list:
            if int(sublist[1]) == int(green_bracelet_list[0][1]):
                final_list.append(sublist)
    print("Depois de reemanipular",final_list)
    ####################################################
    return final_list


if __name__ == '__main__':
    doctors_data = infoFromFiles.readDoctorsFile('doctors10h00.txt')
    requests_data = infoFromFiles.readRequestsFile('requests10h30.txt')
    
    schedule_data = infoFromFiles.readScheduleFile('schedule10h00.txt')
    result = updateSchedule(doctors_data, requests_data, schedule_data, 2)
    request_order = result[0]
    doctors_order = result[1]

    
    combination = combinationsDocRequest(doctors_order, request_order)
