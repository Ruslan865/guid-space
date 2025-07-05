from fpdf import FPDF

def save_to_pdf(title, lines, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # Unicode font əlavə et (məsələn, DejaVu)
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font("DejaVu", size=12)

    pdf.cell(200, 10, txt=title, ln=True, align='C')
    pdf.ln(10)

    for line in lines:
        pdf.multi_cell(0, 10, txt=line)

    pdf.output(filename)
