#
# Copyright (c) 2014 Rafal Bolanowski
# For licensing information please see a LICENSE file.
#

class AbstractSource:
    """
    Abstract class for all data parsers.
    """
    
    def get_grades_table(self):
        """
        Should return data which then will be passed to semester_info(table) method.
        """
        raise NotImplementedError("abstract method")
    
    def semester_info(self, table):
        """
        Accepts semesters' data (probably a table) and parses it. Returns a generator (or is a
        generator expression itself) which in each iteration provides the following data:
            title           - string
            year (of study) - int
            semester        - int
            courses         - list of tuples (course name, ects value, grade); types: (string, int, float)
        Please note that if for any course there is not grade provided it ought to set 0.0 as grade.
        """
        raise NotImplementedError("abstract method")

