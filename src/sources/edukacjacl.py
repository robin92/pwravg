
# 3rd party
from bs4 import BeautifulSoup

from .base import AbstractSource

class Source(AbstractSource):
    """
    Implementation of parser for data collected from EdukacjaCL system.
    """
    
    __pattern   = "Lista kursów realizowanych w semestrach"
    
    def __init__(self, webpage):
        self.root = BeautifulSoup(webpage)
    
    def grade_to_float(self, grade):
        if grade is None or grade == "": return 0.0
        return float(grade)

    def get_grades_table(self):
        b, table = list(filter(lambda x: Source.__pattern in x, self.root.find_all('b')))[0], None
        
        # looking for first table after specified text
        tmp = b
        while tmp.next_sibling:
            if tmp.name != "table":
                tmp = tmp.next_sibling
                continue
            table = tmp
            break
        return table

    def parse_courses(self, courses):
        trs = courses.find_all("tr")[1:]
        data = []
        for tr in trs:
            tds = tr.find_all("td")
            data.append((tds[1].text.strip(), int(tds[3].text.strip()), self.grade_to_float(tds[4].text.strip())))
        return data

    def split_semester_rows(self, table):
        rows = [table.tr] + table.tr.find_next_siblings("tr")
        for i in range(0, len(rows), 4):
            yield rows[i], rows[i + 1], rows[i + 2], rows[i + 3]

    def semester_info(self, table):
        for nameRow, yearRow, semesterRow, coursesRow in self.split_semester_rows(table):
            name = nameRow.td.find_next_sibling("td").text.strip()
            year = yearRow.td.find_next_sibling("td").text.strip()
            semester = semesterRow.td.find_next_sibling("td").text.strip()
            courses = coursesRow.td.table
            yield name, int(year), int(semester), self.parse_courses(courses)

