# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/21/2023
# Description: reads a JSON file containing data on 2010 SAT results for New York City and writes the data to a text file in CSV format

import json
import pandas as pd

class SatData:
    """create SAT date class"""
    def __init__(self):
        self._data = self._read_json_file()

    def _read_json_file(self):
        """create read json file method"""
        with open('sat.json','r', encoding='utf-8') as infile:      # open .json file and read it
            data = json.load(infile)        # use .load()
        return data['data']         # return data

    def save_as_csv(self, dbns):
        """create save as cav method"""
        dbn_data = [entry for entry in self._data if entry[8] in dbns]      # DBNs begin at column 8
        sorted_data = sorted(dbn_data, key=lambda x: (int(x[8][0:2]), int(x[8][3:])))       # sort DBNs
        sorted_data = [x[8:] for x in sorted_data]          # Extract the DBNs and columns after it
        
        name = ["DBN" , "School Name", "Number of Test Takers", "Critical Reading Mean", "Mathematics Mean", "Writing Mean"]    # name of columns
        pd.DataFrame(columns=name , data=sorted_data).to_csv("output.csv")       # save as csv file

  
def main(): 
    sd = SatData()
    dbns = ["02M303", "02M294", "01M450", "02M418"]
    sd.save_as_csv(dbns)
if __name__ == '__main_':
    main()