#imports statistics module
import statistics

#definition of class being named Student
class Student:
#init() used to intialize the values associated with class objects
    def __init__(self, name, grade):
        self.__name = name

        self.__grade = grade
#method used to get grade
    def get_grade(self):
        return self.__grade

#function which calculates mean, median as well as mode
def basic_stats(student):
    #list storing grades of each student
    total = []
    #for loop created in order to iterate list of students, and gets their grade
    # using get_grade() and stores the grades in total list
    for x in student:
        #using append to append grade in total
        total.append(x.get_grade())
#using mean, median and mode methods from the statistics module
# in order to calculate mean, median and mode
    mean = statistics.mean(total)

    median = statistics.median(total)

    mode = statistics.mode(total)
#storing mean median and mode within stats
    stats = (mean, median, mode)
#returns stats
    return stats

#creating students by listing them under different variables using s1,s2, etc
s1 = Student("Kyoungmin", 73)

s2 = Student("Mercedes", 74)

s3 = Student("Avanika", 78)

s4 = Student("Marta", 74)
#list of students being created with the name "student_list"
student_list = [s1, s2, s3, s4]
#prints statistics using basic_stats()
print(basic_stats(student_list))