#femaleNames.py
#take out female last names and ages from AllMarriages.gz

#open the data
import gzip
data = gzip.open("/home/dabrahim/semesterProject/AllMarriages.gz", "rt", encoding='latin-1')

#read the data 
if data:
    #initialize the lists
    nameList = []
    ageList = []
    line = data.readline()
    #while there is a line
    while line:
        #split on pipe
        fields = line.split('|')
        #check for comma in fields[3]-the bride's name
        if "," in fields[3]:
            #if there is a comma, split on comma
            lastName = fields[3].split(',')
            #try to take out the last name
            try: fields[3] = lastName[0]
            #if unable to take out last name,
            #set fields[3] to an empty string 
            except: fields[3] = ""
        #if there is no comma in fields[3]
        else:
            #split on space 
            lastName = fields[3].split()
            #try to take out the last name
            try: fields[3] = lastName[0]
            #if unable to take out last name,
            #set fields[3] to an empty string 
            except: fields[3] = ""
        #try to make fields[4] into an int
        try: int(fields[4])
        #if unable, set fields[4] to zero 
        except: fields[4] = 0
        #check that fields[3] is not an empty string
        #and that fields[4] is not zero 
        if fields[3] != "" and fields[4] != 0:
            #if conditions are filled,
            #add fields[3] and fields[4] to right lists
            nameList += [fields[3]]
            ageList += [fields[4]]
        #read the next line 
        line = data.readline()

#loop though the list
#print out the last names and ages of brides 
for i in range(len(nameList)):
    print(nameList[i], ageList[i])

#close the data
data.close()
