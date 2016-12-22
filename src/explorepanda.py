'''
Created on 24-Nov-2016

@author: venkatesh
'''

import urllib
import math
import pandas as pd
import read_excel as re

def explore_panda():
    print "explore panda: "
    dfs, sheetnames = re.read_full_excel("google.xlsx")
    
    existing_df = dfs["Existing"]
    print existing_df.columns
    print existing_df.index
    
#     print existing_df.ix[:, 0].values
#     print existing_df
    
#     print existing_df.ix[[1990, 1991], ["Afganistan", "Albania"]]
#     print existing_df.loc[1990, "Anguilla"]

#     print existing_df.ix[:,'Afghanistan']
    df = existing_df[existing_df['Afghanistan'] > 420]
    print df
    print df.loc[:,"Afghanistan"]

def main():
    print "Calling main"
    explore_panda()

if __name__ == '__main__': main()