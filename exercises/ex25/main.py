import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("animals/*txt")

pdf =  FPDF(orientation="p", unit="mm", format="A4")

for filepath in filepaths:
    pdf.add_page()

    filename = Path(filepath).stem
    title = filename.title()
    
    pdf.set_font(family="Times", style="B", size=16)
    pdf.cell(w=50, h=8, text=f"{title}", ln=1)
    
    with open(filepath, "r") as file:
        content =  file.read()

    pdf.set_font(family="Times", size=10)
    pdf.multi_cell(w=0, h=6, text=content)

pdf.output("output.pdf")