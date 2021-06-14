import os
from fpdf import FPDF
import pdftotext
import io
import re

path = os.getcwd()
folder = os.listdir(path+"/input")

def nlp():
    for file in folder:
        print()
        
        f = open(os.path.join(path+"/input", file), 'rb')
        print('now reading.... {0}'.format(os.path.join(path+"/input", file)))
        storage = io.BytesIO(f.read())
        f.close()
        txt = pdftotext.PDF(storage)

        
        arr = []

        
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size = 12)

        txt_r_strip = txt[0].rstrip()
        txt_strip = txt_r_strip.strip()
        lines = txt_strip.split('\n')

        
        
        for i in range(len(lines)):
            
            data = lines[i]
            data = re.sub(r'[\w\.-]+@[\w\.-]+', '', data, re.IGNORECASE)

            
            gather = re.search(r'From:\s+', data)
            if isinstance(gather, re.Match):
                data = gather.group(0)

            
            gather = re.search(r'^Visa[\w\s]+\|[\w\s]+:\s+', data)
            if isinstance(gather, re.Match):
                data = gather.group(0)

            
            data = re.sub(r'Visa[\w\s]+ending[\w\s]+in\s\d{4}', 'Visa ending in', data, re.IGNORECASE)

            
            gather = re.search(r'(Billing\s+address)|(Shipping\s+Address)', data)
            if isinstance(gather, re.Match):
                pdf.cell(200, 5, txt = data, ln = 1, align = 'L')
                i += 1
                data = lines[i] 

                blank = re.search(r'^\s{0,2}(\w{1,50})[:#.\s\w,]{0,50}\s{0,5}', data) 
                wildcard = re.search(r'([$-]+)|(^\s+$)', data) 
                marker = re.search(r'^(\s*)Credit', data) 

                while (isinstance(blank, re.Match) or isinstance(wildcard, re.Match)) and not isinstance(marker, re.Match):
                    if isinstance(blank, re.Match):
                        data = re.sub(r'^\s{0,2}(\w{1,50})[:#.\s\w,]{0,50}\s{0,5}', " ", data, re.IGNORECASE)
                    pdf.cell(200, 5, txt = data, ln = 1, align = 'L')
                    arr.append(i)
                    i += 1
                    data = lines[i]
                    blank = re.search(r'^\s{0,2}(\w{1,50})[:#.\s\w,]{0,50}\s{0,5}', data)
                    wildcard = re.search(r'([$-]+)|(^\s*$)', data)
                    marker = re.search(r'^(\s*)Credit', data)
            elif i in arr:
                
                continue
            else:
                
                pdf.cell(200, 5, txt = data, ln = 1, align = 'L')

        print("checking")
        output_fname = os.path.basename(os.path.join(path+"/input", file)).split('.')[0] + ".pdf"
        output_path = os.path.join(path+"/output/") + output_fname
        print('writing pdf.... {0}'.format(output_path))
        pdf.output(output_path, 'F')
