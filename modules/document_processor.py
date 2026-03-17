import PyPDF2

def extract_text(file):

    text=""

    if file.name.endswith(".pdf"):
        reader=PyPDF2.PdfReader(file)

        for page in reader.pages:
            text+=page.extract_text()

    else:
        text=file.read().decode()

    return text