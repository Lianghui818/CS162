# Author: Lianghui Wang
# GitHub username: Lianghui818
# Date: 06/27/2023
# Description: Write a class called Student that has two private data members - the student's name and grade. 
# Description: It should have an init method that takes two values and uses them to initialize the data members. It should have a get_grade method.


import statistics   # Import statistics module

class Student:
    """ Represent a student with name and grade """

    def __init__(self, name, grade):
        """" Create two private variables. Initialize name and grade """
        self.__name = name    # name of the student (private)
        self.__grade = grade  # grade of the student (private)

    def get_grade(self):
        """using get_grade method to get student's grade"""
        return self.__grade   # return the grade of the student


def basic_stats(student):
    """Create tuple to store student's grade"""
    total_student_list=[]    # create a empty list to store

    for x in student:  # using for loop to iterate students
        total_student_list.append(x.get_grade())     # using get_grade() to get student's grade

        mean = statistics.mean(total_student_list)       # computing mean of the grade
        median = statistics.median(total_student_list)   # computing median of the grade 
        mode = statistics.mode(total_student_list)       # computing mode of the grade

        tuple_stats = (mean, median, mode)  # tuple of mean,median and mode
    return tuple_stats


"""
s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

student_list = [s1, s2, s3, s4]

print(basic_stats(student_list))  # should print a tuple of three values

"""


