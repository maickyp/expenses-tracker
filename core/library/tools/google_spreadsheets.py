import gspread
import gspread_formatting as gs_format
import re

class GoogleSheet:
    def __init__(self,credentials):
        """Open connection with Google"""
        self.gc = gspread.service_account(filename=credentials)
        self.sh = None
        self.worksheet = None

    # Setting the document
    def open_document(self, document):
        self.sh = self.gc.open(document)

    def get_worksheet_list(self):
        worksheets = []
        if self.sh is not None:
            worksheets = self.sh.worksheets()
        return worksheets

    def select_worksheet(self, sheet_name):
        self.worksheet = self.sh.worksheet(sheet_name)

    def get_worksheet(self):
        return self.worksheet

    def format_worksheet(self, range, settings):
        gs_format.format_cell_ranges(self.worksheet, [(range, settings)])

    # Write and read
    def write_cell(self, cell, data):
        self.worksheet.update_acell(cell, data)

    def write_cell_by_coordinates(self, col, row, data):
        self.worksheet.update_cell(row, col, data)

    def write_row(self, range, data):
        self.worksheet.update(range, data)
    
    def write_bulk_data(self, range, values):
        matches = re.search(r'(\w+)(\d+):(\w+)(\d+)', range)
        limit = int(matches.group(4))+len(values)
        range_data = f"{matches.group(1)}{matches.group(2)}:{matches.group(3)}{limit}"
        self.worksheet.update(range_data, values, value_input_option="USER_ENTERED")

    def read_cell(self, cell):
        return self.worksheet.acell(cell).value

    def read_cell_by_coordinates(self, col, row):
        return self.worksheet.cell(row, col).value

    def read_data(self, range): #range = "A1:E1". Data devolvera un array de la fila 1 desde la columna A hasta la E
        data = self.worksheet.get(range)
        return data

    def get_last_row_range(self):
        last_row = len(self.worksheet.get_all_values()) + 1
        deta = self.worksheet.get_values()
        range_start = f"A{last_row}"
        range_end = f"{chr(ord('A') + len(deta[0]) - 1)}{last_row}"
        return f"{range_start}:{range_end}"

    def get_all_values(self):
        #self.sheet.get_all_values () # this return a list of list, so the get all records is easier to get values filtering
        return self.worksheet.get_all_records() # this return a list of dictioraies so the key is the name column and the value is the value for that particular column
