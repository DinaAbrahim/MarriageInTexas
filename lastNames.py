#lastNames.py
#Assign race to each last name in 2010Census

#open the data
data = open("/home/dabrahim/semesterProject/Names_2010Census.csv")

#read the data
if data:
    #initialize lists for each race 
    whiteList = []
    blackList = []
    asianList = []
    indianList = []
    multiList = []
    hispanicList = []
    #read the first line
    line = data.readline()
    #while there is a line
    while line:
        #split on comma
        fields = line.split(",")
        #try to make the fields into ints
        try:
            int(fields[5])
            int(fields[6])
            int(fields[7])
            int(fields[8])
            int(fields[9])
            int(fields[10])
        #if they cannot be turned to ints make them zero
        except:
            fields[5] = 0
            fields[6] = 0
            fields[7] = 0
            fields[8] = 0
            fields[9] = 0
            fields[10] = 0
        
        #whiteList
        #if this surname is most common with white people, add it to the white list
        if fields[5] > max(fields[6],fields[7],fields[8],fields[9],fields[10]):
            whiteList += [fields[0]]

        #blackList
        #if this surname is most common with black people, add it to the black list
        if fields[6] > max(fields[5],fields[7],fields[8],fields[9],fields[10]):
            blackList += [fields[0]]
            
        #asianList
        #if this surname is most common with asian people, add it to the asian list
        if fields[7] > max(fields[5],fields[6],fields[8],fields[9],fields[10]):
            asianList += [fields[0]]
            
        #indianList
        #if this surname is most common with indian people, add it to the indian list
        if fields[8] > max(fields[5],fields[6],fields[7],fields[9],fields[10]):
            indianList += [fields[0]]
            
        #multiList
        #if this surname is most common with multi people, add it to the multi list
        if fields[9] > max(fields[5],fields[6],fields[7],fields[8],fields[10]):
            multiList += [fields[0]]

        #hispanicList
        #if this surname is most common with hispanic people, add it to the hispanic list
        if fields[10] > max(fields[5],fields[6],fields[7],fields[8],fields[9]):
            hispanicList += [fields[0]]

        #read the next line
        line = data.readline()

    #loop through each list
    #print out the last name and corresponding race
    for i in range(len(whiteList)):
        print(whiteList[i], "White")
    for i in range(len(blackList)):
        print(blackList[i], "Black")
    for i in range(len(asianList)):
        print(asianList[i], "Asian")
    for i in range(len(indianList)):
        print(indianList[i], "Indian")
    for i in range(len(multiList)):
        print(multiList[i], "Multi")
    for i in range(len(hispanicList)):
        print(hispanicList[i], "Hispanic")

#close the data 
data.close()
        
