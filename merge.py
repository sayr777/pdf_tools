# Последовательно добавляет отдельные документы PDF в единый документ PDF
from PyPDF2 import PdfFileWriter, PdfFileReader

def append_pdf(input,output):
    [output.addPage(input.getPage(page_num)) for page_num in range(input.numPages)]



output = PdfFileWriter()


append_pdf(PdfFileReader("./1.pdf","rb"),output)
append_pdf(PdfFileReader("./2.pdf","rb"),output)
append_pdf(PdfFileReader("./3.pdf","rb"),output)



output.write(open("./result.pdf", "wb"))


