from core.library.tools.google_spreadsheets import GoogleSheet
from gspread_formatting import CellFormat, NumberFormat
import os


def file_exists(file_path: str) -> bool:
    """Check if the file exists at the given path."""
    valid_file_path_str(file_path)

    return os.path.isfile(file_path)

def is_folder(file_path: str) -> bool:
    """Check if the file path is a folder."""
    valid_file_path_str(file_path)

    return os.path.isdir(file_path)

def valid_file_path_str(file_path: str) -> bool:
    """Check if the file path is valid."""
    if not file_path or file_path.isspace() or len(file_path) == 0:
        raise ValueError("The provided file path is empty.")
    
def get_files_in_folders(folder_path):
    files = []
    for root, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            files.append(os.path.join(root, filename))
    return files


def upload_to_spreadsheets(settings, charges):
    spreadsheets_dict = settings["spreadsheets"]["tracker"]
    if spreadsheets_dict["source"] == "google":
        google = GoogleSheet(spreadsheets_dict["credential-file"])
        google.open_document(spreadsheets_dict["file"])
        google.select_worksheet(spreadsheets_dict["sheet"])
        data_pos = google.get_last_row_range()
        print(data_pos)

        fmt=CellFormat(
            numberFormat=NumberFormat(type="CURRENCY", pattern="")
        )
        google.format_worksheet("C", fmt)

        fmt=CellFormat(
            numberFormat=NumberFormat(type="DATE", pattern="dd/mm/yy")
        )
        google.format_worksheet("A", fmt)
        google.write_bulk_data(data_pos, charges)