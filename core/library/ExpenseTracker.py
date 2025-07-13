from core.utils.commonutils import is_folder, get_files_in_folders
from core.library.invoices.banks.bbva import BBVAInvoice
from core.utils.commonutils import upload_to_spreadsheets
from json import load
import core.utils.settings as settings

class ExpenseTracker(object):
    def __init__(self, file_path, verbose=False):
        if is_folder(file_path):
            files = get_files_in_folders(file_path)
            self.files_path = files
        else:
            self.files_path = [file_path]

        self.settings = settings.load_settings()
        self.settings["verbose"] = verbose

    def run(self):
        if self.settings["verbose"] == True and len(self.files_path)  > 1:
            print(f"Processing {len(self.files_path)} files from {self.files_path}")

        for file in self.files_path:
            if self.settings["verbose"]:
                print(f"Processing expenses from file {file}")
            try:
                invoice = BBVAInvoice(file)
            except Exception as e:
                print(f"Error processing file {file}: {e}")
                continue

            movements = invoice.get_movements()

            # upload_to_spreadsheets(self.settings, movements)
