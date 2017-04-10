#
# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.
import numpy

from pony.orm import *
from models import *
import argparse


class Diary(object):

    def __init__(self, db_name):
        self.db = Database()
        self.db.bind("sqlite", db_name + ".sqlite", create_db=False)
        self.db.generate_mapping(create_tables=False)
        sql_debug(False)

    @db_session
    def show_students_total_average_score(self):
        print 'students total average score (average across classes)'
        score = select((avg(scr.value),scr.course.name, scr.student.name, scr.student.surname) for scr in Score)
        score.show()
        print'\n'

    @db_session
    def show_students_course_average_score(self):
        print 'Students average score in course'
        score = select((avg(scr.value), scr.student.name, scr.student.surname) for scr in Score)
        score.show()
        print'\n'

    @db_session
    def show_students_attendance(self):
        print 'Students attendance'
        score = select((count(atd.value), atd.student.name, atd.student.surname) for atd in Attendance)
        score.show()
        print'\n'

if __name__ == '__main__':
    dairy2017 = Diary('Dairy2016')
    dairy2017.show_students_total_average_score()
    dairy2017.show_students_course_average_score()
    dairy2017.show_students_attendance()









