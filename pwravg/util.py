
from pwravg.sources.base import AbstractSource

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

def parse(src):
    """
    Parses data, using an AbstractSource object, into Python object.
    
    Sample data returned by this function:
        ("name", {
            "year": 1
            "semester": 2
            "courses": [("Przykładowy kurs", 3, 5.5),]  # (course title, ects, grade (float))
        })
    """
    if not isinstance(src, AbstractSource): raise ArgumentError("expected AbstractSource")
    table = src.get_grades_table()
    if table is None: return None
    
    data = []    
    for name, year, semester, courses in src.semester_info(table):      
        tmp = {
            "year": year,
            "semester": semester,
            "courses": courses,
        }
        data.append((name, tmp)) 
    
    return data

