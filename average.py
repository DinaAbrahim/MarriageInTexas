#average.py
#this program finds the average age of women of each race at marriage

#open the data 
data = open("/home/dabrahim/semesterProject/compare.txt")

#read the data
if data:
    line = data.readline()
    #initialize sums and totals for each race 
    whiteSum = 0
    whiteTotal = 0
    blackSum = 0
    blackTotal = 0
    asianSum = 0
    asianTotal = 0
    indianSum = 0
    indianTotal = 0
    multiSum = 0
    multiTotal = 0
    hispanicSum = 0
    hispanicTotal = 0
    while line:
        #split on space 
        fields = line.split() #(race,age)
        #set fields[1] to an int
        fields[1] = int(fields[1])
        #for each race, check if fields[0] is that race
        #if it is, add 1 to the total and add fields[1] to the sum 
        if fields[0] == "White":
            whiteTotal += 1
            whiteSum += fields[1]
        if fields[0] == "Black":
            blackTotal += 1
            blackSum += fields[1]
        if fields[0] == "Asian":
            asianTotal += 1
            asianSum += fields[1]
        if fields[0] == "Indian":
            indianTotal += 1
            indianSum += fields[1]
        if fields[0] == "Multi":
            multiTotal += 1
            multiSum += fields[1]
        if fields[0] == "Hispanic":
            hispanicTotal += 1
            hispanicSum += fields[1]
        #read the next line 
        line = data.readline()
    #find the average for each race by dividing the sum by the total 
    whiteAverage = whiteSum // whiteTotal
    blackAverage = blackSum // blackTotal
    asianAverage = asianSum // asianTotal
    indianAverage = indianSum // indianTotal
    multiAverage = multiSum // multiTotal
    hispanicAverage = hispanicSum // hispanicTotal

#print the averages 
print("White", whiteAverage)
print("Black", blackAverage)
print("Asian", asianAverage)
print("Indian", indianAverage)
print("Multi", multiAverage)
print("Hispanic", hispanicAverage)

#close the data 
data.close()
