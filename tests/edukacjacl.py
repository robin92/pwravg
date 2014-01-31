#
# Copyright (c) 2014 Rafal Bolanowski
# For licensing information please see a LICENSE file.
#

from unittest import TestCase
from base64 import b64decode

from pwravg import parse
from pwravg.sources.edukacjacl import Source

import tests.edukacjacl_consts as consts

class EdukacjaclSourceTestcase(TestCase):
    """
    Testcase for Source parsing webpage from EdukacjaCL system.
    """
    
    EXPECTED_DATA = [
            ('2013/2014 Letni', {
                    'semester': 6,
                    'year': 3,
                    'courses': []
                }),
            ('2013/2014 Zimowy', {
                    'semester': 5,
                    'year': 3,
                    'courses': [
                            ('Bazy danych i zarządzanie info', 5, 0.0),
                            ('Obliczenia naukowe i metody', 5, 0.0),
                            ('Projekt programistyczny', 3, 0.0),
                            ('Języki i paradygmaty programow', 6, 0.0),
                            ('Systemy rozproszone', 3, 5.0),
                            ('Języki formatowania danych', 3, 0.0),
                            ('Praktyka', 3, 5.0),
                            ('Metody probabilistyczne i stat', 8, 0.0)
                        ]
                }),
            ('2012/2013 Letni', {
                    'semester': 4,
                    'year': 2,
                    'courses': [
                            ('Podstawy elektroniki', 4, 3.0),
                            ('Grafika komputerowa i wizualiz', 3, 4.5),
                            ('Kurs programowania 2', 4, 5.5), 
                            ('Technologie sieciowe', 4, 5.5), 
                            ('Zarządzanie projektami inform.', 3, 5.0), 
                            ('Kodowanie i bezpieczeństwo inf', 6, 5.0), 
                            ('Język rosyjski - A1', 2, 4.5), 
                            ('Teoria grafów', 3, 3.5), ('Taniec', 1, 5.0)
                        ]
                }),
            ('2012/2013 Zimowy', {
                    'semester': 3,
                    'year': 2,
                    'courses': [
                            ('Wstęp do fizyki technologii', 3, 5.0),
                            ('Laboratorium z fizyki', 1, 5.0),
                            ('Kurs programowania 1', 4, 5.5),
                            ('Logika algorytmiczna', 5, 4.5),
                            ('Systemy operacyjne', 3, 5.0),
                            ('Algorytmy i struktury danych', 6, 4.5),
                            ('Język angielski CERTYF. B2E', 3, 5.0),
                            ('Matematyka dyskretna', 6, 5.5)
                        ]
                }),
            ('2011/2012 Letni', {
                    'semester': 2,
                    'year': 1,
                    'courses': [
                            ('Fizyka', 5, 4.0),
                            ('Wstęp do programowania', 4, 5.0),
                            ('Problemy społeczne i zawodowe', 2, 5.0),
                            ('Urządzenia techniki kompu', 3, 4.5),
                            ('Algebra abstrakcyjna i kodowan', 8, 4.5),
                            ('Analiza matematyczna 2', 8, 5.0),
                            ('Narciarstwo', 1, 5.0)
                        ]
                }),
            ('2011/2012 Zimowy', {
                    'semester': 1,
                    'year': 1,
                    'courses': [
                            ('Etyka', 2, 5.0),
                            ('Wstęp do informatyki', 4, 5.0),
                            ('Algebra z geometrią analit.', 8, 5.0),
                            ('Analiza matematyczna 1', 8, 5.0),
                            ('Logika i struktury formalne', 8, 4.0)
                        ]
                })
        ]
            
    def test_parse_data(self):
        src = Source(b64decode(consts.source))
        self.assertListEqual(parse(src), self.EXPECTED_DATA, "Something went wrong when parsing <= data differs")

