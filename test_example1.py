import pytest
import os
import pdfquery
from PII_removal import nlp

nlp()
pdf = pdfquery.PDFQuery(os.path.join(os.getcwd()+"/output", "example1.pdf"))
pdf.load()

def credit_card():
    expected = 'Visa | Last digits:'

    label = pdf.pq('LTTextLineHorizontal:contains("digits:")')
    assert label.text() == expected



def credit_card_pattern():
    expected = ''

    label = pdf.pq('LTTextLineHorizontal:contains("1234")')
    assert label.text() == expected

def email():
    expected = ''

    label = pdf.pq('LTTextLineHorizontal:contains("@")')
    assert label.text() == expected


