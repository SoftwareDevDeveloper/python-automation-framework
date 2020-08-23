import csv

# Method to get data from csv file

def getCSVData(fileName):
    # create an empty list to store row
    rows = []
    # open the CSV file
    dataFile = open(fileName, "r")
    # create a CSV reader from the csv file
    reader = csv.reader(dataFile)
    # skip the header
    next(reader)
    # add rows from the reader to list
    for ch in reader:
        rows.append(ch)
    return rows
