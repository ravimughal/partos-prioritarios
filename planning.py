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
    shorterTime(doctors, nextTime) #caso o horario do médico disponivel seja antes do horario nexTime, atualiza o horario
    request_order = priorityRequests(requests)
    doctors_order = priorityDoctors(doctors)

    combinations = combinationsDocRequest(doctors_order, request_order, nextTime)
    previousSched.extend(combinations)
    rmvShorterTimePreviousSched(previousSched, nextTime)
    previousSched = priorityTimeSched(previousSched)
    return previousSched


def priorityTimeSched(previousSched):
    """
    Ordena uma lista de eventos com base no horário e no nome do mês.

    A ordenação é realizada considerando duas chaves:
    1. O horário do evento convertido para minutos, onde eventos com menor tempo
    têm prioridade (ex: menos tempo para pausa diária).
    2. O nome do mês em ordem lexicográfica.

    Parameters:
    - previousSched (list): Uma lista de eventos, onde cada evento 
    contém informações como o horário (SCHED_TIME) e o nome do mês (SCHED_NAME_MOTH).

    Returns:
    list: Uma nova lista de eventos ordenados com base nas regras definidas.
    """
    ordened_time = sorted(
        previousSched, key=lambda x: (
            int(dateTime.timeToMinutes(x[SCHED_TIME])),  # menos tempo para pausa diaria
            x[SCHED_NAME_MOTH]  # ordem lexicográfica
        )
    )
    return ordened_time

def rmvShorterTimePreviousSched(previousSched, nextTime):
    """
    Remove eventos da lista `previousSched` cujo horário é menor que o horário especificado.

    Parameters:
    - previousSched (list): Uma lista de eventos
    - nextTime (str): O próximo horário a ser considerado para remoção de eventos, no formato 'HHhMM'.

    Returns:
    list: Uma nova lista de eventos após a remoção dos eventos cujo horário é menor que `nextTime`.
    """
    previousSched_copy = previousSched.copy()
    for sched in previousSched_copy:
        if dateTime.timeToMinutes(sched[SCHED_TIME]) < dateTime.timeToMinutes(nextTime):
            previousSched.remove(sched)
    return previousSched

def shorterTime(doctors, nextTime):
    """
    Atualiza o horário do parto de médicos cujo horário de parto atual é anterior ao próximo
    horário especificado. Se o horário livre do médico for antes do próximo horário especificado,
    o próximo horário do médico é atualizado para o próximo horário especificado.

    Parameters:
    - doctors (list): Uma lista de médicos, onde cada médico é representado por uma lista.
    Cada lista de médico deve ter um índice específico (DOCT_CHILDBIRTH_IDX) contendo
    seu horário de parto atual.
    - nextTime (int): O próximo horário de parto a ser considerado, em minutos.

    Modificações:
    - A função atualiza o horário de parto (índice DOCT_CHILDBIRTH_IDX) de médicos na lista
    cujo horário de parto atual é menor que o próximo horário especificado. Se o horário livre
    do médico for anterior ao próximo horário especificado, o próximo horário do médico é
    atualizado para o próximo horário especificado.

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
    Ordena a lista de médicos com base na disponibilidade de horário de parto e critérios de prioridade.

    Parâmetros:
    - doctors (list): Uma lista de médicos contendo informações de vários médicos.

    Retorna:
    - list: A lista de médicos ordenada com base na disponibilidade de horário de parto e critérios de prioridade.
    """
    final_list = doctors

    # ordena médicos por primeiro disponível e considerando os critérios de desempate
    ordened_time = sorted(
        final_list, key=lambda x: (
            dateTime.timeToMinutes(x[DOCT_CHILDBIRTH_IDX]),
            -int(x[DOCT_CATEGORY_IDX]),  # categoria decrescente
            -int(dateTime.timeToDailyPause(x[DOCT_DAILYWORK_IDX])),  # menos tempo para pausa diaria
            int(dateTime.timeToWeeklyPause(x[DOCT_WEEKLYWORK_IDX])),
            
            x[DOCT_NAME_IDX] # ordem lexicográfica
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
    Gera combinações de pedidos de mães com médicos, evitando médicos em pausa semanal.

    Parâmetros:
    - doctors (list): Uma lista de médicos contendo informações de vários médicos.
    - requests (list): Uma lista de pedidos de mães contendo informações de várias mães.

    Retorna:
    - list: Uma lista de combinações contendo informações sobre o horário de parto, o nome da mãe e o nome do médico.
    """
    combinations = []

    for mother in requests:
        for doctor in doctors: 
            if isWklPause(doctor) == True: #caso doctor esteja em pausa semanal, ignoraremos
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
    Atualiza as informações de um médico e reorganiza a lista de médicos com as atualizações.

    Parâmetros:
    - doctor (list): Uma lista representando as informações do médico que será atualizado.
    - doctors (list): Uma lista de médicos contendo informações de vários médicos.

    Retorna:
    - list: A lista 'doctors' atualizada após as modificações.
    """
    #print(doctor[DOCT_CHILDBIRTH_IDX], doctor[DOCT_NAME_IDX])
    doctor[DOCT_CHILDBIRTH_IDX] = dateTime.sumHours(doctor[DOCT_CHILDBIRTH_IDX], HOUR_CHILDBIRTH) #atualiza o novo horario disponivel do médico
    #print(doctor[DOCT_CHILDBIRTH_IDX], doctor[DOCT_NAME_IDX])

    doctor[DOCT_DAILYWORK_IDX] = int(doctor[DOCT_DAILYWORK_IDX]) + MIN_CHILDBIRTH #soma 20 minutos do trabalho diário
    doctor[DOCT_WEEKLYWORK_IDX] = dateTime.sumHours(doctor[DOCT_WEEKLYWORK_IDX], HOUR_CHILDBIRTH) # soma 20 minutos do tranalho semanal

    doctor = checkDoctors(doctor) #verifica se haverá intervalo diário ou pausa semanal
    doctors = priorityDoctors(doctors) #reorganiza a lista de doctores com as atualizações
    return doctors

def checkDoctors(doctor):
    """
    Verifica se o doutor está no tempo de pausa diária ou semanal e realiza as ações correspondentes.

    Parâmetros:
    - doctor (list): Uma lista representando as informações do doutor, onde
    DOCT_DAILYWORK_IDX e DOCT_WEEKLYWORK_IDX são os índices
    que contêm informações sobre o tempo de trabalho diário e semanal, respectivamente.

    Retorna:
    - list: A lista 'doctor' modificada com as ações correspondentes aplicadas.
    """

    if doctor[DOCT_DAILYWORK_IDX] > 240 and doctor[DOCT_DAILYWORK_IDX] <= 260:
        doctor[DOCT_CHILDBIRTH_IDX] = dateTime.sumHours(doctor[DOCT_CHILDBIRTH_IDX], BREAK_TIME)
    
    hour = dateTime.timeToMinutes(doctor[DOCT_WEEKLYWORK_IDX])
    if hour >=  WKL_WORK:
        doctor[DOCT_CHILDBIRTH_IDX] = WKL_PAUSE
    
    return doctor
    
def isWklPause(doctor):
    """
    Verifica se o doutor está em pausa semanal.

    Parâmetros:
    - doctor (list): Uma lista representando as informações do doutor, onde DOCT_WEEKLYWORK_IDX
    é o índice que contém a informação sobre a pausa semanal.

    Retorna:
    - bool: True se o doutor está em pausa semanal, False caso contrário.
    """
    if doctor[DOCT_CHILDBIRTH_IDX] == WKL_PAUSE:
        return True
    return False

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

    return final_list

if __name__ == '__main__':
    doctors_data = infoFromFiles.readDoctorsFile('doctors16h00.txt')
    requests_data = infoFromFiles.readRequestsFile('requests16h30.txt')
    
    schedule_data = infoFromFiles.readScheduleFile('schedule16h00.txt')
    time_file = infoFromFiles.getTime('schedule16h00.txt')
    nextTime = dateTime.sumHours(time_file, TIME_30_MIN)
    result = updateSchedule(doctors_data, requests_data, schedule_data, nextTime)
