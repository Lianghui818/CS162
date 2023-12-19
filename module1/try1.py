import statistics



class Student:


    def __init__(self, name,grade):
        self.__name = name
        self.__grade = grade


    def get_grade(self):
        return self.__grade



    def basic_stats(student):
        total=[]



        for x in student:
            total.append(x.get_grade())

            mean=statistics.mean(total)
            median=statistics.median(total)
            mode=statistics.mode(total)

            stats=(mean,median,mode)
        return stats



s1 = Student("Kyoungmin", 73)

s2 = Student("Mercedes", 74)

s3 = Student("Avanika", 78)

s4 = Student("Marta", 74)



student_list = [s1, s2, s3, s4]
print(Student.basic_stats(student_list))