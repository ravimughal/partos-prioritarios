#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 141
# 62504 Ravi Mughal 
# 62496 Maria Marisa

from constants import *
import dateTime

def readDoctorsFile(fileName):
    """
    Reads a file with a list of doctors into a collection.

    Requires:
    fileName is str with the name of a .txt file containing
    a list of doctors organized as in the examples provided in
    the general specification (omitted here for the sake of readability).
    Ensures:
    list of lists where each list corresponds to a doctor listed in
    the file fileName (with all the info pieces belonging to that doctor),
    following the order provided in the lines of the file.
    """

    content = removeHeader(fileName)

    doctors = []
    for line in content:
        data = line.strip().split(', ')
        doctors.append(data)
    
    doctors = emptyList(doctors)

    return doctors

def removeHeader(fileName):
    """
    Removes the header lines from a file and returns the remaining content.

    Parameters:
    - fileName (str): The path to the file containing the header lines.

    Returns:
    - content (list): A list containing the lines of the file after removing the header.
    """
    with open(fileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        content = lines[NUM_HEADER_LINES:]

    return content

def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances using the provided file name.

    Parameters:
    - fileName (str): The path to the file containing the list of requested assistances.

    Returns:
    - requestsList (list): A list of lists representing requested assistances. Each inner list
    contains data extracted from a line in the file, split by ', '. Empty lists are removed
    from the result.

    """

    inFile = removeHeader(fileName)       

    requestsList = []
    for line in inFile:
        data = line.strip().split(', ')
        requestsList.append(data)

    requestsList = emptyList(requestsList)
    return requestsList

def emptyList(listOfLists):
    """
    Remove sublistas vazias de uma lista.

    Parâmetros:
    - listOfLists (list): Lista contendo sublistas.

    Retorna:
    list: Nova lista contendo apenas as sublistas não vazias.
    """
    return [sublist for sublist in listOfLists if any(sublist)]




def getHeader(filename):
    """
    Retorna o cabeçalho do arquivo especificado como uma string.

    Parameters:
    - filename (str): O caminho do arquivo a ser lido.

    Returns:
    str: Uma string contendo as primeiras linhas do arquivo, correspondentes ao cabeçalho.
    """
    with open(filename, 'r') as file:
        lines = file.readlines()
        header = lines[:NUM_HEADER_LINES]
        header[NUM_TIME_LINE] = dateTime.sumHours(header[NUM_TIME_LINE], TIME_30_MIN) + '\n'
    return ''.join(header)

def readScheduleFile(file):
    """
    Read schedule data from a file and return a list of lists.

    Parameters:
    - file (str): The path to the file containing schedule data.

    Returns:
    - scheduleList (list): A list of lists representing schedule data. Each inner list
    contains data extracted from a line in the file, split by ', '. Empty lists are
    removed from the result.
    """
    content = removeHeader(file)
    scheduleList = []
    for line in content:
        data = line.strip().split(', ')
        scheduleList.append(data)

    scheduleList = emptyList(scheduleList)
    return scheduleList

