'''
Created on 24-Nov-2016

@author: venkatesh
'''

import pandas as pd

def read_full_excel(filename):
    readfile = pd.ExcelFile(filename)
    sheets = [(sheetname, readfile.parse(sheetname)) for sheetname in readfile.sheet_names]
    dfs = dict(sheets)
    return dfs, readfile.sheet_names
        

def main():
    print "Sample XL reader"
    dfs, sheetnames = read_full_excel("google.xlsx")
    print "Sheet Names = " + str(sheetnames)
    print "Data frames"
    print dfs

if __name__ == '__main__': main()
