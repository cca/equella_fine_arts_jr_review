#!/usr/bin/env python
"""
Usage: python fajr-process.py input.csv

Takes Informer CSV export from TEST - EP - Fine Arts Junior Review Students*
report (use column headers & comma-separated multivalue fields) & then prints
an EQUELLA-ready taxonomy CSV to stdout.

* https://vm-informer-01.cca.edu/informer/#action=ReportRun&reportId=79626253
"""

import csv
import sys
from fajr_group import add_to_fajr_group


def map_semester(semester):
    """
    Turn Informer out like "2015SP" into human-friendly season & year
    such as "Spring 2015"
    """
    sem = semester.lower().replace('sp', ' Spring').replace('su', ' Summer').replace('fa', ' Fall')
    semlist = sem.split()
    semlist.reverse()
    return ' '.join(semlist)


def map_major(major):
    """
    Map five-letter.three-letter degree code into human-friendly major
    e.g. ANIMA.BFA => Animation (BFA)

    Commented-out degree codes don't have a correlate in VAULT's Majors taxo
    """
    translations = {
        'ANIMA.BFA': 'Animation (BFA)',
        'ARCHT.BARC': 'Architecture (BArch)',
        'CERAM.BFA': 'Ceramics (BFA)',
        'COMAR.BFA': 'Community Arts (BFA)',
        'CURPR.MA': 'Curatorial Practice (MA)',
        # 'DD2ST': '',
        'DESGN.MFA': 'Design (MFA)',
        'DESST.MBA': 'Design Strategy (MBA)',
        # 'DVCFA': '',
        # 'EXTED': '',
        'FASHN.BFA': 'Fashion Design (BFA)',
        'FCERM.MFA': 'Fine Arts (MFA)',
        'FDRPT.MFA': 'Fine Arts (MFA)',
        'FGLAS.MFA': 'Fine Arts (MFA)',
        'FILMG.MFA': 'Film (MFA)',
        'FILMS.BFA': 'Film (BFA)',
        'FINAR.MFA': 'Fine Arts (MFA)',
        'FPHOT.MFA': 'Fine Arts (MFA)',
        'FPRNT.MFA': 'Fine Arts (MFA)',
        'FRNTR.BFA': 'Furniture (BFA)',
        'FSCUL.MFA': 'Fine Arts (MFA)',
        'FSOCP.MFA': 'Fine Arts (MFA)',
        'FTEXT.MFA': 'Fine Arts (MFA)',
        'GLASS.BFA': 'Glass (BFA)',
        'GRAPH.BFA': 'Graphic Design (BFA)',
        'GRAPH.MFA': 'Fine Arts (MFA)',
        'ILLUS.BFA': 'Illustration (BFA)',
        # 'INACT.MFA': '',
        'INDIV.BFA': 'Individualized (BFA)',
        'INDUS.BFA': 'Industrial Design (BFA)',
        'INDUS.MFA': 'Industrial Design (MFA)',
        'INTER.BFA': 'Interior Design (BFA)',
        'IXDSN.BFA': 'Interaction Design (BFA)',
        'MAAD1.MAAD': 'Master of Advanced Architectural Design (MAAD)',
        # 'MARC2.MARC': '',
        # 'MARC3.MARC': '',
        'METAL.BFA': 'Jewelry / Metal Arts (BFA)',
        'NODEG.UG': 'Undecided',  # shouldn't appear in this context
        'PHOTO.BFA': 'Photography (BFA)',
        'PNTDR.BFA': 'Painting/Drawing (BFA)',
        'PRINT.BFA': 'Printmaking (BFA)',
        'SCULP.BFA': 'Sculpture (BFA)',
        'TEXTL.BFA': 'Textiles (BFA)',
        'UNDEC.BFA': 'Undecided',
        'VISCR.MA': 'Visual & Critical Studies (MA)',
        'VISST.BA': 'Visual Studies (BA)',
        'WRITE.MFA': 'Writing (MFA)',
        'WRLIT.BA': 'Writing & Literature (BA)'
    }

    if major in translations:
        return translations[major]
    else:
        raise Exception('Cannot translate degree code into major! \
        Check the mappings.')


with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile)
    with open('taxo.csv', 'w') as taxofile:
        writer = csv.writer(taxofile, quoting=csv.QUOTE_ALL)
        users = []
        for row in reader:
            writer.writerow([
                row['surname'] + ', ' + row['givenname'],
                'studentID',
                row['studentID'],
                'username',
                row['username'],
                'major',
                map_major(row['major']),
                'semester',
                map_semester(row['semester']),
            ])

            users.append(row['username'])


add_to_fajr_group(users)
