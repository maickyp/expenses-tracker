import core.library.tools.pdf_utils as PDF
from core.library.invoices.banks.bbva import BBVAInvoice
from core.utils.commonutils import upload_to_spreadsheets
from json import load
import core.utils.settings as settings

class ExpenseTracker(object):
    def __init__(self, file_path):
        if not PDF.validate_pdf(file_path):
            raise ValueError(f"The file at {file_path} is not a valid PDF or file does not exists.")
        self.file_path = file_path

        self.settings = settings.load_settings()


    def run(self):
        # Logic to process the expense tracking
        print(f"Processing expenses from {self.file_path}")
        invoice = BBVAInvoice(self.file_path)
        movements = invoice.get_movements()

        upload_to_spreadsheets(self.settings, movements)

        # Add more functionality as needed
