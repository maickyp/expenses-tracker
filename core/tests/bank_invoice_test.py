from argparse import ArgumentParser
from core.library.invoices.banks.bbva import BBVAInvoice

def validate_bbva_invoice(pdf_file):
    invoice = BBVAInvoice(pdf_file)
    print(f"Date\t\t\tAmount\t\t\tDescription\t\t\t")
    for item in invoice.get_movements():
        print(f"{item[0]}\t\t{item[2]}\t\t\"{item[1]}\"")

    print("Total Charges:",invoice.total_charges)
    print("Total Payments:",invoice.total_payments)

def start_validation(args):

    if args.bank is None:
        raise ValueError("Bank name is required for validation.")
    
    if args.bank.lower() == "bbva":
        validate_bbva_invoice(args.file)