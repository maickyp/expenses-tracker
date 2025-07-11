import pypdf
import os


def validate_pdf(file_path: str) -> bool:
    """Check if the file is a valid PDF."""

    if not file_exists(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    return file_path.endswith('.pdf')
    
def file_exists(file_path: str) -> bool:
    """Check if the file exists at the given path."""
    if not file_path or file_path.isspace() or len(file_path) == 0:
        raise ValueError("The provided file path is empty.")

    if not os.path.isfile(file_path):
        raise FileNotFoundError(f"The file at {file_path} does not exist.")

    return os.path.exists(file_path)

def extract_text_pdf(file_path: str):
    if not validate_pdf(file_path):
        raise ValueError(f"The file at {file_path} is not a valid PDF.")

    pdf_text = ""
    with open(file_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_text += page.extract_text()

    return pdf_text
