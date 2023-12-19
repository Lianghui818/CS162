def insertionsort(string_list):
    """ Create a insertion sort function to sort a list of strings instead of numbers"""
    for index in range(1, len(string_list)):
        value = string_list[index]
        pos = index - 1

        while pos >= 0 and string_list[pos].lower() > value.lower():      # ignore case
            string_list[pos + 1] = string_list[pos]
            pos -= 1

        string_list[pos + 1] = value

    return string_list

def main():
    example_list = ["Zebra", "apple", "maRker", "marble"]     # example
    sorted_list = insertionsort(example_list)
    print(sorted_list)

if __name__ == '__main__':
    main()
