import csv
with open('BetterBaseball - Sheet1.csv', mode='r') as csv_file:
    csv_reader = csv.reader(csv_file)
    next(csv_reader)
    data_array = [row for row in csv_reader]
    team1 = ["C","1B","2B","3B","SS","OF","OF","OF","DH","P","P","P","P","P"]
    team2 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team3 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team4 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team5 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team6 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team7 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team8 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team9 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team10 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team11 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]
    team12 = ["C", "1B", "2B", "3B", "SS", "OF", "OF", "OF", "DH", "P", "P", "P", "P", "P"]

    teamlist=[team1,team2,team3,team4,team5,team6,team7,team8,team9,team10,team11,team12]
    id=9
    print(data_array[id])
    if len(data_array[id][2]) > 2:
        positions_list=data_array[id][2].split(',')
        position = data_array[id][2]
        for position in positions_list:
            if position == "RF" or position == "LF" or position == "CF":
                if teamlist[0][5] == "OF":
                    teamlist[0][5] = data_array[id][4]
                    break
                elif teamlist[0][6] == "OF":
                    teamlist[0][5] = data_array[id][4]
                    break
                elif teamlist[0][7] == "OF":
                    teamlist[0][6] = data_array[id][4]
                    break
                elif teamlist[0][8] == "DH":
                    teamlist[0][8] = data_array[id][4]
                    break
            elif position == "C":
                if teamlist[0][0] == "C":
                    teamlist[0][0] = data_array[id][4]
                    break
                elif teamlist[0][8] == "DH":
                    teamlist[0][8] = data_array[id][4]
                    break
            elif position == "2B":
                if teamlist[0][2] == "2B":
                    teamlist[0][2] = data_array[id][4]
                    break
                elif teamlist[0][8] == "DH":
                    teamlist[0][8] = data_array[id][4]
                    break
            elif position == "3B":
                if teamlist[0][3] == "3B":
                    teamlist[0][3] = data_array[id][4]
                    break
                elif teamlist[0][8] == "DH":
                    teamlist[0][8] = data_array[id][4]
                    break
            elif position == "SS":
                if teamlist[0][4] == "SS":
                    teamlist[0][4] = data_array[id][4]
                    break
                elif teamlist[0][8] == "DH":
                    teamlist[0][8] = data_array[id][4]
                    break
            elif position == "1B":
                if teamlist[0][1] == "1B":
                    teamlist[0][1] = data_array[id][4]
                    break
                elif teamlist[0][8] == "DH":
                    teamlist[0][8] = data_array[id][4]
                    break
            elif position == "DH":
                if teamlist[0][8] == "DH":
                    teamlist[0][8] = data_array[id][4]
                    break
            elif position == "SP" or position == "RP":
                if teamlist[0][9] == "P":
                    teamlist[0][9] = data_array[id][4]
                    break
                elif teamlist[0][10] == "P":
                    teamlist[0][10] = data_array[id][4]
                    break
                elif teamlist[0][11] == "P":
                    teamlist[0][11] = data_array[id][4]
                    break
                elif teamlist[0][12] == "P":
                    teamlist[0][12] = data_array[id][4]
                    break
                elif teamlist[0][13] == "P":
                    teamlist[0][13] = data_array[id][4]
                    break
            else:
                result = "Invalid position"
            print(result)
    else:
        position=data_array[id][2]
        if position == "RF" or position == "LF" or position == "CF":
            if teamlist[0][5] == "OF":
                teamlist[0][5]=data_array[id][4]
            elif teamlist[0][6] == "OF":
                teamlist[0][5]=data_array[id][4]
            elif teamlist[0][7] == "OF":
                teamlist[0][6]=data_array[id][4]
            elif teamlist[0][8] == "DH":
                teamlist[0][8]=data_array[id][4]
        elif position == "C":
            if teamlist[0][0] == "C":
                teamlist[0][0]=data_array[id][4]
            elif teamlist[0][8] == "DH":
                teamlist[0][8]=data_array[id][4]
        elif position == "2B":
            if teamlist[0][2] == "2B":
                teamlist[0][2] = data_array[id][4]
            elif teamlist[0][8] == "DH":
                teamlist[0][8] = data_array[id][4]
        elif position == "3B":
            if teamlist[0][3] == "3B":
                teamlist[0][3] = data_array[id][4]
            elif teamlist[0][8] == "DH":
                teamlist[0][8] = data_array[id][4]
        elif position == "SS":
            if teamlist[0][4] == "SS":
                teamlist[0][4] = data_array[id][4]
            elif teamlist[0][8] == "DH":
                teamlist[0][8] = data_array[id][4]
        elif position == "1B":
            if teamlist[0][1] == "1B":
                teamlist[0][1] = data_array[id][4]
            elif teamlist[0][8] == "DH":
                teamlist[0][8] = data_array[id][4]
        elif position == "DH":
            if teamlist[0][8] == "DH":
                teamlist[0][8] = data_array[id][4]
        elif position == "SP" or position == "RP":
            if teamlist[0][9] == "P":
                teamlist[0][9]=data_array[id][4]
            elif teamlist[0][10] == "P":
                teamlist[0][10]=data_array[id][4]
            elif teamlist[0][11] == "P":
                teamlist[0][11]=data_array[id][4]
            elif teamlist[0][12] == "P":
                teamlist[0][12]=data_array[id][4]
            elif teamlist[0][13] == "P":
                teamlist[0][13]=data_array[id][4]
        else:
            print('error')

print(team1)
