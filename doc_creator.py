from fpdf import FPDF

def save_to_pdf(title, contents):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=title, ln=1, align='C')

    for line in contents:
        pdf.multi_cell(0, 10, txt=line)

    pdf.output("output.pdf")
