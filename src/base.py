
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

def average(courses, weight = lambda x: 1, value = lambda x: x):
    """
    Counts average of a given iterable.
    
    By default uses weight-function that for any input returns 1 thus making this function a classic
    arithmetic average. This can be changed by providing a optional `weight` argument.
    
    This function calls a value-function on each object from iterable. By default this function
    returns the object itself but this can easily be changed by providing a optional `value` argument.
    """
    sum, totalWeight = 0, 0
    for course in courses:
        wght = weight(course)
        sum, totalWeight = sum + wght * value(course), totalWeight + wght
    return sum/totalWeight

