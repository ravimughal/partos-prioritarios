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


def combinationsDocRequest(doctors, requests):
    combinations = []

    for mother in requests:
        for doctor in doctors:
            if mother[MOTH_RISK_IDX] == 'high' and int(doctor[DOCT_CATEGORY_IDX]) >= 2:
                combinations.append([mother[MOTH_NAME_IDX], doctor[DOCT_NAME_IDX]])
                break
            elif mother[MOTH_RISK_IDX] != 'high':
                combinations.append([mother[MOTH_NAME_IDX], doctor[DOCT_NAME_IDX]])
                break
            
    print(combinations)

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