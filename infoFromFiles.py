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
    with open(fileName, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        start_finish_lines = lines[7:-1]

    doctors = []
    for i in start_finish_lines:
        doctors.append(i.split(', '))

    for i in doctors:
        if '\n' in i[4]:
            i[4] = i[4].replace('\n', '')

    return doctors

def readRequestsFile(fileName):
    """
    Reads a file with a list of requested assistances with a given file name into a collection.

    
    """

    """inFile = removeHeader(open(fileName, "r"))       

    requestsList = [] 
    for line in inFile:
        requestData = line.rstrip().split(", ")
        requestsList.append(requestData)        

    return requestsList


    """

if __name__ == '__main__':
    print(readDoctorsFile('doctors10h30.txt'))