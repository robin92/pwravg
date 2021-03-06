#
# Copyright (c) 2014 Rafal Bolanowski
# For licensing information please see a LICENSE file.
#

"""
Implementation of command line interface. Features:
    * reads input from STDIN by default, can specify file with -f or --file
    * specify semesters to include in counting
"""

# standard python library
from argparse import ArgumentParser
from sys import argv, exit, stdin

# this project
from pwravg import average, parse
from pwravg.sources import edukacjacl

def format_course_title(title, maxlength = 32):
    return (title + " " * (maxlength - len(title)))[:maxlength]

def parse_webpage(webpage, width = 80, titlesep = "=", tablesep = "-", semesters = None, semesters_from_oldest=True):
    source = edukacjacl.Source(webpage)
    data = list(sorted(parse(source), key=lambda kv: kv[1]['semester']))
    if not semesters_from_oldest:
        data = list(reversed(data))

    total = {
        "average": 0.0,
        "courses": 0,
        "ects": 0,
        "weightaverage": 0.0,
    }    
    
    for name, tmp in data:
        year, semester, courses = tmp["year"], tmp["semester"], tmp["courses"]
        if semesters is not None and semester not in semesters: continue
        
        print("{}\nrok: {}\tsemestr: {}".format(name, year, semester))
        print("{}".format(width * titlesep))
        if len(courses) > 0:
            print("{}\t\t\t\t{}\t{}".format("NAZWA KURSU", "ECTS", "OCENA"))
            print("{}".format(width * tablesep))
            for course in courses: print("{}\t{}\t{}".format(format_course_title(course[0]), course[1], course[2]))
            
            print("{}".format(width * tablesep))
            print("Punktów ECTS:\t\t{}".format(sum(map(lambda x: x[1], courses))))
            print("Średnia ważona:\t\t{:.3f}".format(average(courses, value = lambda x: x[2], weight = lambda x: x[1])))
            print("Średnia arytmetyczna:\t{:.3f}".format(average(courses, value = lambda x: x[2])))
        
            total["average"] += sum(map(lambda x: x[2], courses))
            total["courses"] += len(courses)
            total["ects"] += sum(map(lambda x: x[1], courses))
            total["weightaverage"] += sum(map(lambda x: x[1] * x[2], courses))
        else: print("Brak danych o kursach!")
        print()

    try:    
        total["average"] /= total["courses"]
        total["weightaverage"] /= total["ects"]
    except ZeroDivisionError: pass
    
    print("Łącznie")
    print("{}".format(width * titlesep))
    print("Odbyto kursów:\t\t{}".format(total["courses"]))
    print("Punktów ECTS:\t\t{}".format(total["ects"]))
    print("Średnia ważona:\t\t{:.3f}".format(total["weightaverage"]))
    print("Średnia arytmetyczna:\t{:.3f}".format(total["average"]))
    
    return True

__desc = """ Aplikacja licząca średnią arytmetyczną i średnią ważoną na podstawie danych z portalu EdukacjaCL """

if __name__ == "__main__":
    parser = ArgumentParser(prog = "pwravg", description = __desc)
    parser.add_argument("-f", "--file", type = str, dest = "file", help = "plik wejściowy, domyślnie STDIN")
    parser.add_argument("-s", "--semesters", type = int, nargs = "+", dest = "semesters", metavar = "N", help = "uwzględniane semestry")
    parser.add_argument("-r", "--reverse", dest="reversed", action="store_true",
                        help="wypisz semestry w kolejności od najmłodszego do najstarszego")
    args = parser.parse_args(argv[1:])

    file = stdin
    if args.file is not None:
        try:
            file = open(args.file, "r")
        except FileNotFoundError:
            print("Error: file '{}' not found!".format(args.file))
            exit(1)

    webpage = file.read()
    if not webpage:
        exit(1)
    if not parse_webpage(webpage, semesters = args.semesters, semesters_from_oldest=not(args.reversed)):
        exit(1)
    exit(0)

