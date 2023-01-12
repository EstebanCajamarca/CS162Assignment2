# Author: Esteban Cajamarca
# GitHub username: EstebanCajamarca
# Date: 1/11/2023
#
# Write a class called Student that has
# two private data members - the student's name and grade. It should have an init method that takes two values and
# uses them to initialize the data members. It should have a get_grade method.
#
# Write a separate function (not part of the Student class) called basic_stats that takes as a parameter a list of
# Student objects and returns a tuple containing the mean, median, and mode of all the grades. To do this,
# use the mean, median and mode functions in the statistics module. Your basic_stats function should return those
# three values as a tuple, in the exact order given above.

import statistics


class Student:
    """represents students name and grade'"""

    def __init__(self, name, grade):  # initializing private data members
        self._name = name
        self._grade = grade

    def get_grade(self):  # get method to import grade
        return self._grade


def basic_stats(students_list):
    """Create list of students"""
    students_grades_list = []  # for storing list of grades in a list

    for each_student in students_list:  # repeating process for n number of students.
        students_grades_list.append(each_student.get_grade())  # adding all grades to the students_grades_list

    return (statistics.mean(students_grades_list), statistics.median(students_grades_list),
            statistics.mode(students_grades_list))  # getting results by using imported library.


s1 = Student("Kyoungmin", 73)
s2 = Student("Mercedes", 74)
s3 = Student("Avanika", 78)
s4 = Student("Marta", 74)

students_list = [s1, s2, s3, s4]
print(basic_stats(students_list))  # printing results for mean, media and mode.
