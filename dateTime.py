#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa



def hourToInt(time):
    """

    """
    t = time.split("h")
    return int(t[0])

def minutesToInt(time):
    """

    """
    t = time.split("h")
    return int(t[1])
    

def timeToMinutes(time):
    """
    
    """
    hour = hourToInt(time)
    minutes = minutesToInt(time)
    return (hour * 60 + minutes)

def minutesToHour(minutes):
    horas = minutes // 60
    minutos_restantes = minutes % 60

    # Formata a string no estilo HHhMM
    formato_horas = "{:02}h{:02}".format(horas, minutos_restantes)

    return formato_horas

def sumHours(time1, time2):
    total_minutes = timeToMinutes(time1) + timeToMinutes(time2)
    return minutesToHour(total_minutes)

def timeToDailyPause(time):
    """
    Calcula o tempo restante até a próxima pausa com base no tempo atual em minutos.

    Parâmetros:
    - time (int): O tempo atual em minutos.

    Retorna:
    int: O tempo restante até a próxima pausa. Se o tempo atual for igual ou superior a 240 minutos,
    retorna a diferença entre 480 minutos e o tempo atual. Caso contrário, retorna a diferença
    entre 240 minutos e o tempo atual.
    """
    time = int(time)
    
    if time >= 240:
        return 480 - time
    else:
        return 240 - time

def timeToWeeklyPause(time):
    """
    Calcula o tempo acumulado até a próxima pausa semanal com base no tempo atual em minutos.

    Parâmetros:
    - time (str): O tempo atual no formato 'hh:mm'.

    Retorna:
    int: O tempo acumulado até a próxima pausa semanal em minutos.
    """
    time = timeToMinutes(time)

    return time

def intToTime(hour, minutes):
    """

    """
    h = str(hour)
    m = str(minutes)

    if hour < 10:
        h = "0" + h

    if minutes < 10:
        m = "0" + m

    return h + "h" + m

if __name__ == '__main__':
    #print(sumHours('0h20', '19h30'))
    pass