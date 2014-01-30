
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

