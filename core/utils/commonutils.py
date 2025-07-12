from core.library.tools.google_spreadsheets import GoogleSheet
from gspread_formatting import CellFormat, NumberFormat

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