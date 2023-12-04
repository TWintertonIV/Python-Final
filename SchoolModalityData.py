
#Given File Name
#Create and return list of data

#list is of following format
#data[Record][Type]

#Type is of following structure
#ID                     0    
#Name                   1
#Week                   2
#learning_modality      3
#operational_schools    4
#student_count          5
#city                   6
#state                  7
#zip_code               8

def exportCSV(file):

    #Initalize Returned List    
    data = []
    #Temp holder for individual line arrays
    record = []

    #Add records to data list
    while(True):
        try:
            with open(file, 'r') as f:
                f.readline()
                for line in f:

                    record = line.rstrip("\n").split(",")
                    data.append(record)
        except:
            print("Error Opening File\n")
        else:
            break
    
    return data


#Gather Valid File Name
def gatherFile():
    while(True):
        try:
            fileName = input("Data file path: ")
            f = open(fileName, 'r')
        except:
            print("Invalid File Path\n")
        else:
            break

        #add whitespace before next print
    print("")


    return fileName


#Print out menu options, Gather input, and return number representing selected option (1,2,3,4)
def Menu():
    #print out options for selection

    print("Data analysis options:\n")

    print("1. List dates")
    print("2. Learning modality by state on date")
    print("3. An analysis you choose")
    print("4. Exit\n")
    

    options = [1,2,3,4]

    while(True):
        try:
            menuInput = int(input("Enter the number of the option (1, 2, 3, or 4): "))
            if(menuInput not in options):
                print("Not a valid option")
                continue
        except:
                print("Invalid Input")
        else:
            break
    print("")
    return menuInput



def dates(data):
    distincts = []

    for modality in data:
        if(modality[2] not in distincts):
            distincts.append(modality[2])
            print(modality[2][:10])
    print("\n")

def generateDates(data):

    distincts = []
    modDates = []
    for modality in data:
        if(modality[2] not in distincts):
            distincts.append(modality[2])
    
    for date in distincts:
        modDates.append(date[:10])
    return modDates

def summary(data):

    #list of valid states + 'all'
    validStates = ['AL', 'AK', 'AZ', 'AR', 'AS','CA','CO','CT','DE','DC','FL','GA','GU','HI','ID','IL','IN','IA','KS','KY','LA','ME','MD','MA','MI','MN','MS','MO','MT','NE','NV','NH','NJ','NM','NY','NC','ND','MP','OH','OK','OR','PA','PR','RI','SC','SD','TN','TX','TT','UT','VT','VA','VI','WA','WV','WI','WY','all' ]
    validDates = generateDates(data)
    validMenu =['y','n']
    repeat = True

    #Initialize all statistic variables
    while(repeat):
        numSchools = 0
        numStudents = 0
        schoolNumIP = 0
        schoolNumHybrid = 0
        schoolNumRemote = 0

        studentNumIP = 0
        studentNumHybrid = 0
        studentNumRemote = 0

        
        print("Enter the two digit code (CA, MO, IL, TX, etc.) for a state or 'all' for all states.")
        while(True):
            state = str(input("State (2 digit code or 'all'): "))
            if(state in validStates):
                break
            else:
                print("Invalid State")
                

        while(True):
            date = str(input("Date (MM/DD/YYYY): "))
            if(date in validDates):
                break
            else:
                print("Invalid Date")

        for school in data:
            if(school[2][:10] == date):
                if(state == 'all' or school[7] == state):
                    numSchools += int(school[4])
                    numStudents += int(school[5])
                    if(school[3] == 'In Person'):
                        schoolNumIP += int(school[4])
                        studentNumIP += int(school[5])
                    elif(school[3] == 'Hybrid'):
                        schoolNumHybrid += int(school[4])
                        studentNumHybrid += int(school[5])
                    elif(school[3] == 'Remote'):
                        schoolNumRemote += int(school[4])
                        studentNumRemote += int(school[5])


        print("-------------------------------")
        print("Date: " + date)
        print("Description: " + state)
        print(f'{numSchools:,}' + " schools")
        print(f'{numStudents:,}' + " students")
        print("Schools per modality:")
        print(f' * {schoolNumIP:,} ({((schoolNumIP/numSchools) * 100):.2f}%) In Person')
        print(f' * {schoolNumHybrid:,} ({((schoolNumHybrid/numSchools) * 100):.2f}%) Hybrid')
        print(f' * {schoolNumRemote:,} ({((schoolNumRemote/numSchools) * 100):.2f}%) Remote')
        print("Students per modality:")
        print(f' * {studentNumIP:,} ({((studentNumIP/numStudents) * 100):.2f}%) In Person')        
        print(f' * {studentNumHybrid:,} ({((studentNumHybrid/numStudents) * 100):.2f}%) Hybrid')
        print(f' * {studentNumRemote:,} ({((studentNumRemote/numStudents) * 100):.2f}%) Remote')
        print("-------------------------------\n")

        while(True):
            choice = input("Enter another state and date: (y/n) ")
            if(choice not in validMenu):
                print("Invalid Choice")
            else:
                break;

        if(choice == 'y'):
            repeat = True
        else:
            repeat = False
            print("\n")

def main():
    print("Learning Modalities Analyzer\n")

    fileName = gatherFile()
    masterDataList = exportCSV(fileName)

    # for record in masterDataList:
    #     print(str(record))


    exitClause = False
    while(not exitClause):
        choice = Menu()
        if(choice == 1):
            dates(masterDataList)
        elif(choice == 2):
            summary(masterDataList)
        # elif(choice == 3):
        #     analysis(masterDataList)
        # elif(choice == 4):
        #     exitClause = uExit()    

main()