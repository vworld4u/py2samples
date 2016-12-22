'''
Created on 25-Nov-2016

@author: venkatesh
'''

import numpy as np
import pandas as pd

months = ["January", "February", "March", "April", 'May', "June", "July", "August", "September", "October", "November", "December"]
days = [31, 28, 21, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def is_leap_year(year):
    return year % 4 == 0 and year % 200 != 0

def main():
    print "generateWorkingHours: "
    names = generate_worker_names()
    print names
    dates, workhours = generate_working_hours(2016, names)
    df = pd.DataFrame(workhours, names, dates)
    writer = pd.ExcelWriter("workhours.xlsx")
    df.to_excel(writer, sheet_name = "WorkingHours")
    writer.save()
    writer.close()
    print "Done."

def generate_worker_names():
    return map(chr, range(65, 91))

def generate_working_hours(year, rows):
    allDates = []
    for i in range(len(months)):
        numDays = days[i]
        if is_leap_year(year) and i == 1: numDays += 1
        dates = [str(i + 1) + "-" + str(j + 1) + "-" + str(year) for j in range(numDays)]
        allDates = allDates + dates
    
    workdata = [ [8 for j in range(len(allDates))] for i in range(len(rows))]
    return allDates, workdata
    

if (__name__ == "__main__"): main()