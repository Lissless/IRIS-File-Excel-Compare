'''
Read Excel File
Read File of Folders
Compare to see if there are any names that are not in the folder and vice versa
'''
import pandas as pd
from os import listdir
from os.path import isfile, join

def getExcelNames():
    excelSheet = pd.read_excel("Test-Excel-Names.xlsx")
    data = pd.DataFrame(excelSheet, columns=["File Name"])
    names = data["File Name"].to_list()
    return names

def main():
    excelNames = getExcelNames()


if __name__ == "__main__":
    main()
