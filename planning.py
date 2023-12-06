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


    
    index_of_risk = 3
    index_of_bracelet = 2

    high_risk_list = []
    medium_risk_list = []
    low_risk_list = []
    
    red_bracelet_list = []
    yellow_bracelet_list = []
    green_bracelet_list = []

    final_list = []




    
    for sublist in requests:
        if index_of_risk < len(sublist):
            risk = sublist[index_of_risk]
            if risk == 'high':
                high_risk_list.append(sublist)
            elif risk == 'medium':
                medium_risk_list.append(sublist)
            elif risk == 'low':
                low_risk_list.append(sublist)


                
    if len(high_risk_list) > 0:
        final_list.extend(high_risk_list)
    elif len(medium_risk_list) > 0:
        final_list.extend(medium_risk_list)
    elif len(low_risk_list) > 0:
        final_list.extend(low_risk_list)


    for sublist in final_list:
        if index_of_bracelet < len(sublist):
            bracelet = sublist[index_of_bracelet]
            if bracelet == 'red':
                red_bracelet_list.append(sublist)
            elif bracelet == 'yellow':
                yellow_bracelet_list.append(sublist)
            elif bracelet == 'green':
                green_bracelet_list.append(sublist)


    if len(red_bracelet_list) > 0:
        final_list = red_bracelet_list.copy()
    elif len(yellow_bracelet_list) > 0:
        final_list = yellow_bracelet_list.copy()
    elif len(green_bracelet_list) > 0:
        final_list = green_bracelet_list.copy()


    if len(final_list) > 1:
        highest_age = int(final_list[0][1])
        mother_with_highest_age = final_list[0]

        for mother in final_list[1:]:
            current_age = int(mother[1])
            if current_age > highest_age:
                highest_age = current_age
                mother_with_highest_age = mother

        final_list = [mother_with_highest_age]

    print('lista final: ',final_list)
    print()
    print('high: ',high_risk_list)
    print()
    print('medium: ',medium_risk_list)
    print()
    print('low: ',low_risk_list)
    print()
    print('red: ',red_bracelet_list)
    print()
    print('yellow: ',yellow_bracelet_list)
    print()
    print('green: ',green_bracelet_list)
    

if __name__ == '__main__':
    doctors_data = infoFromFiles.readDoctorsFile('doctors10h00.txt')
    requests_data = infoFromFiles.readRequestsFile('requests10h30.txt')
    result = updateSchedule(doctors_data, requests_data, 1, 2)
