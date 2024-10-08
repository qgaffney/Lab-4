#Import OS module
import os

#Import module to read CSV
import csv

#Set path for source file
CSV_PATH = os.path.join ('Resources', 'budget_data.csv')

#Open and read CSV
os.chdir(os.path.dirname(os.path.realpath(__file__)))
with open(CSV_PATH) as csvfile:

#Specify delimiter and CSV reader
    csvreader = csv.reader(csvfile, delimiter=",")

#Read header row, store it
    csv_header = next(csvreader)

#Declare variables
    months = 0
    change = 0

#Declare and initiate lists and dictionaries
    date_list = []
    changes_list = []

#Loop though data
    for row in csvreader:

#Create lists to store individually
        date_list.append(row[0])
        changes_list.append(row[1])

        print(date_list, changes_list)

        def selectionSort(date_list):
            n = len(date_list)
            for i in range(n-1):
                minValueIndex = 1

                for j in range(i+1, n):
                    if date_list[j] < date_list[minValueIndex]:
                        minValueIndex = j

                if minValueIndex != i:
                    temp = date_list[i]
                    date_list[i] = date_list[minValueIndex]
                    date_list[minValueIndex] = temp

                return date_list
            
            for j in range(n):
                if changes_list[j] < changes_list[minValueIndex]:
                    minValueIndex = j

                if minValueIndex != i:
                    temp = changes_list[i]
                    changes_list[i] = changes_list[minValueIndex]
                    changes_list[minValueIndex] = temp

                return changes_list
        
        SelSort = [date_list]
        SelSort2 = [changes_list]

        print(selectionSort(SelSort))