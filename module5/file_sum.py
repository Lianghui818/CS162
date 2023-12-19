# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 07/20/2023
# Description: sum the values in the file and write the sum (just that number) to a text file named sum.txt 

def file_sum(input_file):
    """create a method to calculate the sum"""
    try:
        with open(input_file, 'r') as infile:          # open the file to read
            numbers = [float(line.strip()) for line in infile]      # read float number line by line

        sum_of_numbers = sum(numbers)       # calculate the sum

        with open('sum.txt', 'w') as outfile:       # create a file named sum.txt and write
            outfile.write(str(sum_of_numbers))      # write the sum into file
        
        print(f"Sum of numbers is: {sum_of_numbers}")      # print the sum

    except FileNotFoundError:       # except the file not found error
        print("Input file not found.")


"""Example"""
def main():
    file_sum("input_numbers.txt")

if __name__ == '__main__':
    main()
