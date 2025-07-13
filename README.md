# Expense Tracker

## Description
Brief script to scrap the invoice of your bank's credit card's movements and drop them at spreasheets.
Currently this code supports only Mexican invoice format since all has a default format.
Nevertheless, it is designed to be able to add multiples formats or banks

It scraps PDF files using Regex looking for expenses and payments to such card.
Then, connect to spreadsheets file and selected sheet and writes data in it.

## Installation
It's pretty straightforward, you have a python interpreter? you surely can run this module.
It is needed only a couple of dependencies listed below:

### Dependencies

-gspread
-gspread_formatting
-pypdf

Run `pip install -r requirements.txt` for below dependencies

## Usage
To run this project use:
`python expenses-tracker.py -f <path-to-file>`

This will go to defined path location and scrap for its info and upload it to selected spreadsheets
If <path-to-file> is a folder, it will scan for every pdf file

## Features
- Mexican Bank BBVA support only (currently)
- Upload to spreadsheets capability

## Configuration
There is a few confgurations to be done before use it.
1. It is needed to be able to upload to spreadsheet to have a [service account for Google Cloud Platform](https://cloud.google.com/iam/docs/keys-create-delete) (currently free).
Once you have your credentials, the json file needs to be at core/settings.

2. In order to select the correct sheet, another json file should be at the same folder as credentials
```
"source": "google",
"file": "<sheet_file_name>",
"sheet": "<sheet_name>",
"credential-file":"<path_to_credential_file>"
```
The spreadsheets file must be shared with the Google Service Account you created before (use the email they generated for that service account)


## Contributing
Feel free to colaborate to this project

## License
GNU General Public License v3.0 (GPL-3.0)
