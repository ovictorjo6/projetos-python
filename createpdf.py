from fpdf import FPDF

pdf = FPDF()

pdf.add_page()

pdf.set_font('Arial',size=25)

#create a cell 

pdf.cell(200,10,txt='Dynamic Coding', ln=1, align='C')

pdf.cell(200,10,txt='A Place For Python Programming',ln=2,align='C')

pdf.output('PrimeiroPdf.pdf')
