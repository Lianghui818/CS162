def bubble_count(a_list):
    """function to count the number of comparisons and the number of exchanges in bubble sort"""
    comparisons = 0     # Initialize to 0
    exchanges = 0       # Initialize to 0
    length = len(a_list)
    for pass_num in range(length):
        swapped = False
        for index in range(0, length-pass_num-1):
            comparisons += 1
            if a_list[index] > a_list[index+1]:
                a_list[index], a_list[index+1] = a_list[index+1], a_list[index]
                exchanges += 1
                swapped = True
        if not swapped:
            break
    return comparisons, exchanges       # returns two values (comparisons first, exchanges second)


def insertion_count(a_list):
    """function to count the number of comparisons and the number of exchanges in insertion sort"""
    comparisons = 0     # Initialize to 0
    exchanges = 0       # Initialize to 0
    length = len(a_list)
    for index in range(1, length):
        value = a_list[index]
        pos = index - 1

        while pos >= 0:
            comparisons += 1
            if a_list[pos] > value:
                a_list[pos + 1] = a_list[pos]
                pos -= 1
                exchanges += 1
            else:
                break

        a_list[pos + 1] = value

    return comparisons, exchanges       # returns two values (comparisons first, exchanges second)

def main():

    """Bubble Sort"""
    list_1 = [2, 4, 6, 3]
    comparisons_1, exchanges_1 = bubble_count(list_1)
    print(f"Bubble Sort: Comparisons: {comparisons_1}, Exchanges: {exchanges_1}")

    """Insertion Sort"""
    list_2 = [5, 4, 1, 7, 2, 0, 6, 3]
    comparisons_2, exchanges_2 = insertion_count(list_2)
    print(f"Insertion Sort: Comparisons: {comparisons_2}, Exchanges: {exchanges_2}")

if __name__ == '__main__':
    main()
