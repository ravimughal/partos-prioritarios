import infoFromFiles

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


    request_order = priority(requests)
    print(request_order)

def priority(list):
    

    index_of_risk = 3
    index_of_bracelet = 2

    high_risk_list = []
    medium_risk_list = []
    low_risk_list = []

    final_list = []

    for sublist in list:
        if index_of_risk < len(sublist):
            risk = sublist[index_of_risk]
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
        if sublist[index_of_bracelet] == 'red':
            red_bracelet_list.append(sublist)
        elif sublist[index_of_bracelet] == 'yellow':
            yellow_bracelet_list.append(sublist)
        elif sublist[index_of_bracelet] == 'green':
            green_bracelet_list.append(sublist)

   
    red_bracelet_list = sorted(red_bracelet_list, key=lambda x: (int(x[1]), 0), reverse=True)
    yellow_bracelet_list = sorted(yellow_bracelet_list, key=lambda x: (int(x[1]), 1), reverse=True)
    green_bracelet_list = sorted(green_bracelet_list, key=lambda x: (int(x[1]), 2), reverse=True)

    
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
    
    return final_list


if __name__ == '__main__':
    doctors_data = infoFromFiles.readDoctorsFile('doctors16h00.txt')
    requests_data = infoFromFiles.readRequestsFile('requests16h30.txt')
    result = updateSchedule(doctors_data, requests_data, 1, 2)
