from fpdf import FPDF

def save_to_pdf(query, answers, filename="output.pdf"):
    pdf = FPDF()
    pdf.add_page()

    # Unicode fontu əlavə edirik
    pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
    pdf.set_font("DejaVu", size=14)

    pdf.cell(200, 10, txt=f"Sual: {query}", ln=True, align="L")
    pdf.ln(10)

    pdf.set_font("DejaVu", size=12)
    for answer in answers:
        pdf.multi_cell(0, 10, txt=answer)
        pdf.ln(5)

    pdf.output(filename)