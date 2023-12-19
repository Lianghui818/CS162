# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/26/2023
# Description: returns True if the first string is a subsequence of the second string, but returns False otherwise

def is_subsequence(string_1, string_2, i=0, j=0):
    """create a function to find the first string is a subsequence of the second string or not"""

    if i == len(string_1):      #  traversed all characters of string1
        return True
    if j == len(string_2):      #  traversed all characters of string2
        return False

    if string_1[i] == string_2[j]:          # if the characters match 
        return is_subsequence(string_1, string_2, i + 1, j + 1)         # move to the next character in both strings
    
    return is_subsequence(string_1, string_2, i, j + 1)     # If the characters don't match, move to the next character in the string2

"""Example"""
def main():
    string_1 = "aeiuo"
    string_2 = "facetious"
    print(is_subsequence(string_1, string_2))
if __name__ == "__main__":
    main()