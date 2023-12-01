#-*- coding: utf-8 -*-

# 2023-2024 Programação 1 (LTI)
# Grupo 546
# 75000 Alberto Albertino 
# 75001 Maria Marisa



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
    pass


def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    
    """

    inFile = removeHeader(open(fileName, "r"))       

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList


