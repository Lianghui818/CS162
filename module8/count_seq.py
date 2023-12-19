# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 08/06/2023
# Description: Write a generator function that doesn't require any arguments and generates a sequence

def count_seq():
    yield "2"               # Special case for the first term
    prev_term = "2"         # initializes the variable prev_term with the value "2"

    while True:             # starts an infinite loop that generates the terms of the sequence indefinitel
        count = 1           # keep track of the count of consecutive digits in the previous term
        current_term = ""           # empty string, build the next term of the sequence

        for num in range(1, len(prev_term)):
            if prev_term[num] == prev_term[num - 1]:           # checks if the current digit is the same as the previous digit
                count += 1          # if the current digit is the same as the previous digit, the count is incremented by 1

            else:
                current_term += str(count) + prev_term[num - 1]         # adds the count of the consecutive digits and the previous digit to the current_term
                count = 1           # count is reset to 1

        current_term += str(count) + prev_term[-1]           # Add the last count and digit
        yield current_term
        prev_term = current_term

# Example:
def main():
    my_gen = count_seq()
    for num in range(10):
        print(next(my_gen))

if __name__ == '__main__':
    main()