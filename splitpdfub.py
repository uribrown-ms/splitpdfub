import os
from PyPDF2 import PdfReader, PdfWriter

# Define the PDF file name as a variable
pdf_file = 'file name.pdf'

# Get the base name of the original file (without the extension)
base_name = os.path.splitext(pdf_file)[0]

# Create a new directory with the base name of the original file
os.makedirs(base_name, exist_ok=True)

with open(pdf_file, 'rb') as file:
    infile = PdfReader(file)

    for i in range(len(infile.pages)):
        page = infile.pages[i]
        outfile = PdfWriter()
        outfile.add_page(page)
        
        # Save the new files in the new directory
        with open(os.path.join(base_name, f'{base_name}-page-{i}.pdf'), 'wb') as f:
            outfile.write(f)