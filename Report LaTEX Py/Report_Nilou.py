import os
import numpy as np
from pylatex import Document, Section, Subsection, Command, Figure, Tabular, MultiRow, MultiColumn
import pdflatex
from pylatex import Document, PageStyle, Head, Foot, MiniPage, \
    StandAloneGraphic, MultiColumn, Tabu, LongTabu, LargeText, MediumText, \
    LineBreak, NewPage, Tabularx, TextColor, simple_page_number
from pylatex.utils import bold, NoEscape

from pylatex import Document, Section, Subsection, Command
from pylatex.utils import italic, NoEscape
import matplotlib.pyplot as plt

num = 5


def fill_document(doc):
    """Add a section, a subsection and some text to the document.
    :param doc: the document
    :type doc: :class:`pylatex.document.Document` instance
    """
    with doc.create(Section('Scope')):
        doc.append('Tasks Update includes ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('Progress Overview:')):
            doc.append('\n')
            doc.append('\n')
            with doc.create(Tabular('|c|c|c|c|')) as table:
                table.add_hline()
                table.add_row((bold('Task:'), bold('Goal/Desired outcome:'),
                               bold('Progress:'), bold('GitHub:')))
                table.add_hline()
                table.add_row('Task1', '', '', MultiRow(3, data='Multicolumn not on left'))
                table.add_hline(start=3)
                table.add_empty_row()
                table.add_hline(start=3)
                table.add_empty_row()
                table.add_hline()
                table.add_row('Task2', '', '', MultiRow(3, data='Multicolumn not on left'))
                table.add_hline(start=3)
                table.add_empty_row()
                table.add_hline(start=3)
                table.add_empty_row()
                table.add_hline()

                # table.add_row((4, 5, 6, 7))

        a = np.array([[100, 10, 20]]).T
        M = np.matrix([[2, 3, 4],
                       [0, 0, 1],
                       [0, 0, 2]])

    with doc.create(Section('Task 2 (GS-Call data flow):')):
        doc.append('updates tasks ')
        doc.append(italic('italic text. '))

        with doc.create(Subsection('GSL_Experiment_setup:')):
            doc.append(italic('What the algorithm does: \n'))
            doc.append('algorithm text')
            doc.append('\n\n\n')
            doc.append(italic('Features: '))
            doc.append('features text')
            doc.append('\n')
            doc.append(italic('Web app: '))
            doc.append('user instructions text')
            doc.append('\n')
            with doc.create(Figure(position='h!')) as kitten_pic:
                kitten_pic.add_image('C:/Users/Niloufar Jamshidy/OneDrive - Genetic Signatures Ltd/Nilou '
                                     'works/Ninouf-Py/Task_2_webbapp/GSL-Experiment_setup.png', width='120px')
                kitten_pic.add_caption('GSL-Experiment_setup web app with interactive platemap feature')
            doc.append('\n')
            doc.append(italic('Challenges: '))
            doc.append('limitation text')
            doc.append('\n')


#
if __name__ == '__main__':
    # Basic document
    doc = Document('Report_Nilou')
    doc.preamble.append(Command('title', 'Report %d' % num))
    doc.preamble.append(Command('author', 'by Nilou'))
    doc.preamble.append(Command('date', NoEscape(r'\today')))
    doc.append(NoEscape(r'\maketitle'))
    fill_document(doc)
    doc.generate_pdf('Report_Nilou', clean_tex=False, compiler='pdflatex')
    tex = doc.dumps()  # The document as string in LaTeX syntax

