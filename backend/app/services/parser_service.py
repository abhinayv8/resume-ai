import pdfplumber
from docx import Document
from fastapi import UploadFile

def extract_text(file: UploadFile) -> str:
    if file.filename.endswith(".pdf"):
        return extract_pdf_text(file)
    elif file.filename.endswith(".docx"):
        return extract_docx_text(file)
    else:
        return ""

def extract_pdf_text(file: UploadFile) -> str:
    text = ""
    with pdfplumber.open(file.file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def extract_docx_text(file: UploadFile) -> str:
    doc = Document(file.file)
    return "\n".join([para.text for para in doc.paragraphs])
