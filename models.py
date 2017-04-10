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

from pony.orm import *
from datetime import datetime

db = Database("sqlite", "Dairy2016.sqlite", create_db=False)


class Student(db.Entity):
    name = Required(str)
    surname = Required(str)
    name = Required(str)
    group = Required('Group')
    scores = Set('Score')
    attendance = Set('Attendance')


class Course(db.Entity):
    name = Required(str)
    score = Set('Score')
    attendance = Set('Attendance')


class Score(db.Entity):
    date = Required(datetime)
    value = Required(int)
    student = Required(Student)
    course = Required(Course)


class Attendance(db.Entity):
    date = Required(datetime)
    value = Required(bool)
    student = Required(Student)
    course = Required(Course)


class Group(db.Entity):
    name = Required(str)
    student = Set('Student')

db.generate_mapping(create_tables=False)





