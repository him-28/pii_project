import pytest
import os
import pdfquery
from PII_removal import nlp

nlp()
pdf = pdfquery.PDFQuery(os.path.join(os.getcwd()+"/output", "example2.pdf"))
pdf.load()

def credit_card():
    expected = 'Visa | Last digits:'

    label = pdf.pq('LTTextLineHorizontal:contains("digits:")')
    assert label.text() == expected
