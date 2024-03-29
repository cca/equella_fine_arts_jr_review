#!/usr/bin/env python
"""
Usage: python fajr-process.py input.csv 2019FA

Takes CSV of Fine Arts juniors with their ID, names, majors, plus usernames &
then creates an EQUELLA-ready taxonomy CSV named "taxo.csv" and uploads it.
"""

import csv
import os
import sys

from fajr_group import add_to_fajr_group


def map_major(major):
    """
    Map five-letter.three-letter degree code into human-friendly major
    e.g. ANIMA.BFA => Animation (BFA)
    We should really only need the Fine Arts majors here but including the
    full list costs us nothing.

    Commented-out degree codes don't have a correlate in VAULT's Majors taxo
    """
    translations = {
        'ANIMA.BFA': 'Animation (BFA)',
        'ARCHT.BARC': 'Architecture (BArch)',
        'CERAM.BFA': 'Ceramics (BFA)',
        'COMAR.BFA': 'Community Arts (BFA)',
        'CURPR.MA': 'Curatorial Practice (MA)',
        'DESGN.MFA': 'Design (MFA)',
        'DESST.MBA': 'Design Strategy (MBA)',
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
        'INDIV.BFA': 'Individualized (BFA)',
        'Individualized Studies': 'Individualized (BFA)',
        'INDUS.BFA': 'Industrial Design (BFA)',
        'INDUS.MFA': 'Industrial Design (MFA)',
        'INTER.BFA': 'Interior Design (BFA)',
        'IXDSN.BFA': 'Interaction Design (BFA)',
        'MAAD1.MAAD': 'Master of Advanced Architectural Design (MAAD)',
        'METAL.BFA': 'Jewelry / Metal Arts (BFA)',
        'Jewelry and Metal Arts': 'Jewelry / Metal Arts (BFA)',
        'NODEG.UG': 'Undecided',  # shouldn't appear in this context
        'PHOTO.BFA': 'Photography (BFA)',
        'PNTDR.BFA': 'Painting/Drawing (BFA)',
        'Painting and Drawing': 'Painting/Drawing (BFA)',
        'PRINT.BFA': 'Printmedia (BFA)',
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
    # handle if Fine Arts sends us non-code versions of majors
    elif "{} (BFA)".format(major) in translations.values():
        return "{} (BFA)".format(major)
    else:
        raise Exception('Cannot translate degree code "{}" into major! Check the mappings.'.format(major))

filename = sys.argv[1]
semester = sys.argv[2]
with open(filename) as csvfile:
    reader = csv.DictReader(csvfile)
    with open('taxo.csv', 'w') as taxofile:
        writer = csv.writer(taxofile, quoting=csv.QUOTE_ALL)
        users = []
        anima_users = []
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
                semester,
            ])

            users.append(row['username'])
            if map_major(row['major']) in ['Animation (BFA)', 'Film (BFA)']:
                anima_users.append(row['username'])

print('Wrote EQUELLA taxonomy file to taxo.csv.')
add_to_fajr_group(users)
add_to_fajr_group(anima_users, anima=True)
os.system('./upload.sh')
