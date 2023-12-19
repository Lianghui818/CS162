# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/25/2023
# Description: return True if the elements of the list are strictly decreasing but return False otherwise

def  is_decreasing(a_list, pos = 0):
    """create a function to determine whether the list is strictly decreasing"""

    if pos == len(a_list) - 2:          # When pos reaches the second-to-last index of the list
        return a_list[pos] > a_list[pos + 1]

    if a_list[pos] <= a_list[pos + 1]:      # The latter number is larger than the previous one
        return False            # false
    
    return is_decreasing(a_list, pos + 1)           # recursive

"""Example:"""
def main():
    num_list = [765, 75, 51, 28]
    print(is_decreasing(num_list))

if __name__ == '__main__':
    main()