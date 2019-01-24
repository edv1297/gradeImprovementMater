import csv

with open('StudentData 7160 1 23 19 - Sheet3.csv') as file:
    reader = csv.reader(file)

    count = 1
    points = 0

    for row in reader:
        firstNineWeeks = row[5]
        secondNineWeeks = row[6]
        IDNumber = row[4]

        if(firstNineWeeks>secondNineWeeks):
            if(firstNineWeeks == "F"):
                firstNineWeeks = "E"
            if(secondNineWeeks == "F" ):
                secondNineWeeks ="E"
            points+=(ord(firstNineWeeks) - ord(secondNineWeeks))
        

        if( firstNineWeeks < secondNineWeeks):
            if(firstNineWeeks == "F"):
                firstNineWeeks = "E"
            if(secondNineWeeks == "F" ):
                secondNineWeeks = "E"
            
            points-=( ord(secondNineWeeks) - ord(firstNineWeeks))

           

        if count == 6:
            print(""+ IDNumber + " has " + str(points) + " points")
            points = 0
            count = 0

            
        count+=1

        # ID LAST, FIRST, GRADE
        # Color coded : 1 point, 2points, 3points+