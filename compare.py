#compare.py
#compare lastNames.txt and femaleNames.txt

#open the data
data = open("/home/dabrahim/semesterProject/lastNames.txt")

#make lastNames.txt into a dictionary
#read the data 
if data: 
    line = data.readline()
    #initialize dictionary
    dict = {}
    while line:
        #split on space
        fields = line.split()
        #add last names and corresponding races to the dictionary
        dict[fields[0]] = fields[1]
        #read the next line
        line = data.readline()

#close the data
data.close()

#open the data
female = open("/home/dabrahim/semesterProject/femaleNames.txt")

#read the data
if female:
    line = female.readline() #(last name,age)
    #initialize the lists
    raceList = []
    ageList = []
    while line:
        #split on space 
        fields = line.split()
        #if the last name is in the dictionary
        if fields[0] in dict:
            #add the race and age to the corresponding lists 
            raceList += [dict[fields[0]]] #(race)
            ageList += [fields[1]] #(age)
        #read the next line 
        line = female.readline()

#loop through the list
#print out the races and ages 
for i in range(len(ageList)):
    print(raceList[i],ageList[i])

#close the data 
female.close()

