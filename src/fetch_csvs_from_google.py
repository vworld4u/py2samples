'''
Created on 24-Nov-2016

@author: venkatesh
'''

import urllib
import pandas as pd

def main():
    tb_deaths_url_csv = 'https://docs.google.com/spreadsheets/d/12uWVH_IlmzJX_75bJ3IH5E-Gqx6-zfbDKNvZqYjUuso/pub?gid=0&output=CSV'
    tb_existing_url_csv = 'https://docs.google.com/spreadsheets/d/1X5Jp7Q8pTs3KLJ5JBWKhncVACGsg5v4xu6badNs4C7I/pub?gid=0&output=csv'
    tb_new_url_csv = 'https://docs.google.com/spreadsheets/d/1Pl51PcEGlO9Hp4Uh0x2_QM0xVb53p2UDBMPwcnSjFTk/pub?gid=0&output=csv'
    
    local_tb_deaths_file = 'tb_deaths_100.csv'
    local_tb_existing_file = 'tb_existing_100.csv'
    local_tb_new_file = 'tb_new_100.csv'
    
    deaths_f = urllib.urlretrieve(tb_deaths_url_csv, local_tb_deaths_file)
    existing_f = urllib.urlretrieve(tb_existing_url_csv, local_tb_existing_file)
    new_f = urllib.urlretrieve(tb_new_url_csv, local_tb_new_file)
    
    deaths_df = pd.read_csv(local_tb_deaths_file, index_col = 0, thousands  = ',').T
    existing_df = pd.read_csv(local_tb_existing_file, index_col = 0, thousands  = ',').T
    new_df = pd.read_csv(local_tb_new_file, index_col = 0, thousands  = ',').T

    writer = pd.ExcelWriter("google.xlsx")
    deaths_df.to_excel(writer, sheet_name="Deaths")
    existing_df.to_excel(writer, sheet_name="Existing")
    new_df.to_excel(writer, sheet_name="New")
    writer.save()
    writer.close()
    print "Done."


if __name__ == '__main__': main()