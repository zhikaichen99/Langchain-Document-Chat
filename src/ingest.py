from PyPDF2 import PdfReader

def pdf_to_text(pdf_docs):
    """
    Function to extract text from pdf documents

    Inputs:
        pdf_docs - list of uploaded pdf documents
    Outputs:
        text - extracted text
    """
    text = ""
    for pdf in pdf_docs:
        # initialize pdfreader
        pdf_reader = PdfReader(pdf)
        # loop through the pages of the pdf and extract the text
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text
