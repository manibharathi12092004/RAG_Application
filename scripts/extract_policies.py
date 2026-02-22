import fitz
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

POLICY_FOLDER = os.path.abspath(
    os.path.join(BASE_DIR, "..", "policies_data")
)

# PDF EXTRACTION

def extract_pdf(path):

    doc = fitz.open(path)

    text = ""

    for page in doc:

        page_text = page.get_text()

        if page_text:
            text += page_text + "\n"

    doc.close()

    return text

# READ ALL PDFs

def read_all_policies():

    policies = {}

    for file in os.listdir(POLICY_FOLDER):

        if file.lower().endswith(".pdf"):

            file_path = os.path.join(POLICY_FOLDER, file)

            print("Reading:", file)

            policies[file] = extract_pdf(file_path)

    return policies