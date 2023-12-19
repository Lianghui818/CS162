# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/20/2023
# Description: reads a JSON file containing data on Nobel Prizes and allows the user to search that data

import json

class NobelData:
    def __init__(self):
        """create a method to reads the file and stores it"""
        with open("nobels.json", 'r') as infile:        # open json file and read it
            self._data = json.load(infile)

    def search_nobel(self, year, category):
        """create a method to search"""
        result = []     # create an empty list

        for prize in self._data["prizes"]:
            if prize["year"] == year and prize["category"] == category:
                laureates = prize.get("laureates", [])
                for laureate in laureates:
                    surname = laureate.get("surname")
                    if surname:
                        result.append(surname)      # append surname to result list

        return sorted(result)

"""Example""" 
def main():
    nd = NobelData()
    print(nd.search_nobel("2001", "economics"))
if __name__ == '__main__':
    main()