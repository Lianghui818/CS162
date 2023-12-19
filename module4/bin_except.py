class TargetNotFound(Exception):
    """ Create a TargetNotFound exception class """
    pass

def bin_except(a_list, target):    
    """    
    Searches a_list for an occurrence of target    
    If found, returns the index of its position in the list    
    If not found, returns -1, indicating the target value isn't in the list    
    """    
    first = 0    
    last = len(a_list) - 1    
    
    while first <= last:        
        middle = (first + last) // 2        
        if a_list[middle] == target:            
            return middle        
        if a_list[middle] > target:            
            last = middle - 1        
        else:            
            first = middle + 1

    raise TargetNotFound("Target value not found in the list.")     # Raise the error we defined


def main():
    a_list = [2, 5, 8, 12, 16, 21, 25, 28, 32, 34, 36, 41]      # A in sorted order list
    target = 15

    try:
        index = bin_except(a_list, target)
        print(f"At index {index} we found target value {target}.")
    except TargetNotFound as tnf:
        print("TargetNotFound Error:", tnf)

if __name__ == "__main__":
    main()