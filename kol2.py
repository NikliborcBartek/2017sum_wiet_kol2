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

class student:
    def __init__(self, name, surname,student_id, attendances=None, scores = None):
        self.name = name
        self.surname = surname
        self.attendances = attendances
        self.scores = scores
        self.student_id = student_id

        def get_avarage_score(self):
            if scores is None:
                return None
            else:
                return numpy.avarage(self.scores)
        def get_avarage_attendance(self):
            if attendances is None:
                return None
            else:
                return numpy.avarage(attendance)

class class_dictionary:
    def _init(self, class_id, student_list):
        self.class_id = class_id
        students = {}

    def get_avarege_student_score(self, student_id):
        student = students[student_id];
        return numpy.avarage(student.avarage_score)




