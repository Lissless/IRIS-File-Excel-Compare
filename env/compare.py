'''
Read Excel File
Read File of Folders
Compare to see if there are any names that are not in the folder and vice versa
'''
import pandas as pd
from os import listdir, remove
from os.path import isfile, join
import re

def getExcelNames():
    excelSheet = pd.read_excel("Test-Excel-Names.xlsx")
    data = pd.DataFrame(excelSheet, columns=["File Name"])
    names = data["File Name"].to_list()
    return names

def getFolderNames():
    rawFileNames = listdir("Phase 1 Data")
    return rawFileNames

def deleteRepeats(fileNames):
    count = []
    original = []
    for name in fileNames:
        res = name[len(name) - 7 : len(name) - 4]
        if re.match("\(\d*\)", res) != None:
            remove("Phase 1/" + name)
            count.append(name)
            print(name)
        else:
            original.append(name[0: len(name) - 4])
    print("duplicate amount: " + str(len(count)))
    return original

def createDataSheet(originalNames):
    frame = pd.DataFrame(originalNames, columns=["File Names"])
    frame.to_excel("Phase_1_Names.xlsx")

def main():
    excelNames = getExcelNames()
    excelNames.sort()
    fileNames = getFolderNames()
    fileNames.sort()
    original = deleteRepeats(fileNames)
    createDataSheet(original)
    print("done")


if __name__ == "__main__":
    main()
