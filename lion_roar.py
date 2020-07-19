# Dependencies
import csv
import pandas as pd
 

# Convert Excel File to Csv
def data_to_csv(data_file):
    print("found excel file, changing to CSV")
    path = data_file[0:len(data_file)-4] + "csv"
    data = pd.read_excel(data_file)
    data.to_csv(path, index = False)
    return path

# Calculate the points in calculate improvement method
def calc_difference(first,second):
    difference = 0
    if first == "" and second == "":
        return difference
    elif first == " ":
        first = second
        return difference

    elif second == " ":
        second = first
        return difference
    else:
        
        if(first == "F"):
            first = "E"
        if(second == "F" ):
            second ="E"
        difference = (ord(first) - ord(second))

    return difference


# Used to start off algorithm in calculate improvement
def get_firstID(filepath):
    with open(filepath) as file:
        reader = csv.reader(file)
        reader.__next__()
        num = reader.__next__()[1] # represents id column
    return num

# Making csv out of analyzed data from calculate improvement
def make_excel(data_list,output):
    with open(str(output), 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, dialect='excel')

        for i in data_list:
            writer.writerow(i)

# PRE: Given a filepath, and an output filename
# POST: Return the list of students with their improvement scores.
# ALGO SKETCH: For each row, compare first and second quarter scores
# if the first quarter letter is earlier in the alphabet then the second quarter, return a negative score
# conversely, if the first quarter letter is later in the alphabet then the second, return a positive score
# if there's no change then return 0.
def calculate_improvement(filepath):
    analysis = []
#     filepath = data_to_csv(filepath)
    
    
    if (".xlsx" in filepath):
        data = data_to_csv(filepath)
    else:
        data = filepath
    
    first_nine_weeks = 5
    second_nine_weeks = first_nine_weeks+1
    
    first_name_col = 3
    last_name_col = 2
    grade_col = 0
    
    id_col = 1
    
    with open(data) as file:
        reader = csv.reader(file)
        reader.__next__() #Skip first row
        points = 0
        IDnum = 0
        pre= []
        IDnum = get_firstID(data) # get the first ID to start off the algo

        for row in reader:
            
            firstNineWeeks = row[first_nine_weeks] 
            secondNineWeeks = row[second_nine_weeks]
            checkID = row[id_col]
            name = row[first_name_col] + " "+ row[last_name_col] # indices of first and last name
            grade = row[grade_col]

            if (IDnum != checkID): # when we reach a new ID Num, add current information to the output file and reset info
                analysis.append([pre[id_col],pre[grade_col], pre[first_name_col]+ " " +pre[last_name_col] , points])
                points = 0
                IDnum = checkID
            
            points += calc_difference(firstNineWeeks, secondNineWeeks)
            pre = row
            
    modifier_index = data.rfind('.csv')
    make_excel(analysis,data[0:modifier_index] + "-analyzed.csv")


def continuous_improvement(q1_csv, q2_csv, output):
    calculate_improvement(q1_csv, output)
    calculate_improvement(q2_csv, output+"2")
    clean_files(q1_csv, q2_csv, "./"+output+".csv")
    
    
def clean_files(f1, f2, out):
    df_1 = pd.read_csv(f1, names = ["ID", "Grade", "Name", "Points"])
    df_2 = pd.read_csv(f2, names = ["ID", "Grade", "Name", "Points"])
    
    df_1 = df_1.merge(df_2, left_on = "ID", right_on="ID")
    df_1 = df_1.drop(df_1.columns[4:6], axis=1)

    print(df_1)
    
    r_df = pd.DataFrame()
    for ind in df_1.index:
        if (df_1["Points_x"][ind]>0 and df_1["Points_y"][ind]>0):
            r_df = r_df.append(df_1.iloc[ind])
    
    
    r_df.set_index("ID").to_csv(out)

# data_to_csv('./data/7160.xlsx')

calculate_improvement('./data/7160.csv')
calculate_improvement('./data/7014.csv')
calculate_improvement('./data/6012.csv')
# clean_files(output)

# calculate_improvement
# continuous_improvement('./data/7160.csv','./data/6012_q2-q3.csv', "6012_improve")
# continuous_improvement('./7014_q1.csv','./7014_q2-q3.csv', "7014_improve")

# continuous_improvement('./data/7014_1.csv', './data/7014.csv', "7014_continuous_improvement")
# continuous_improvement('./data/6012_1.csv', './data/6012.csv', "6012_continuous_improvement")