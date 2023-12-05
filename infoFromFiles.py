#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa

from constants import *


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
    for i in content:
        doctors.append(i.split(', '))

    for i in doctors:
        if '\n' in i[4]:
            i[4] = i[4].replace('\n', '')

    return doctors

def removeHeader(fileName):
    with open(fileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        content = lines[NUM_HEADER_LINES:-1]
    return content

def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.
    """

    inFile = removeHeader(fileName)       

    requestsList = []
    for line in inFile:
        data = line.strip().split(', ')
        requestsList.append(data)

    return requestsList




    


