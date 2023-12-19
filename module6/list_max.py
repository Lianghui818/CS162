# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/25/2023
# Description: returns the maximum value in the list

def list_max(a_list):
    """create the function to find the maximum value in the list"""
    if len(a_list) == 0:        # empty list
        return ("There are no numbers in the list. No maximum value can be returned")       # no maximum value

    if len(a_list) == 1:        # list only has one number
        return a_list[0]        # return this number
    
    mid = len(a_list) // 2      # Divide list into two parts
    left_max = list_max(a_list[:mid])       # recursive
    right_max = list_max(a_list[mid:])

    return left_max if left_max >= right_max else right_max     # returns the maximum value


"""Example:"""
def main():
    num_list = [5,7,1,9,58,36,9,57,14,32,8]
    print("The maximum value in the list is", list_max(num_list))

if __name__ == '__main__':
    main()