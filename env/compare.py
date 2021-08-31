'''
Read Excel File
Read File of Folders
Compare to see if there are any names that are not in the folder and vice versa
'''
import pandas as pd
from os import listdir
from os.path import isfile, join
import re

def getExcelNames():
    excelSheet = pd.read_excel("Test-Excel-Names.xlsx")
    data = pd.DataFrame(excelSheet, columns=["File Name"])
    names = data["File Name"].to_list()
    return names

def getFolderNames():
    rawFileNames = listdir("Phase 1")
    return rawFileNames

def createComparisonSheet(excelNames, fileNames):
    count = []
    for name in fileNames:
        res = name[len(name) - 7 : len(name) - 4]
        if re.match("\(\d*\)", res) != None:
            count.append(name)
            print(name)
    print("duplicate amount: " + str(len(count)))

def main():
    excelNames = getExcelNames()
    excelNames.sort()
    fileNames = getFolderNames()
    fileNames.sort()
    createComparisonSheet(excelNames, fileNames)
    print("done")


if __name__ == "__main__":
    main()
