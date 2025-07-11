from argparse import ArgumentParser
import core.tests.bank_invoice_test as tests
from core.library.ExpenseTracker import ExpenseTracker

def parse_args():
    parser = ArgumentParser(description="Test bank invoices.")
    parser.add_argument("-m", "--mode",     choices=["test","normal"], default="normal",  help="Select the test mode to run." )
    parser.add_argument("-v", "--verbose",  action="store_true",                            help="Enable verbose output")
    parser.add_argument("-f", "--file",     required=True,                                  help="Path to the invoice file to validate")
    parser.add_argument("-b", "--bank",                                                     help="Bank name to validate invoices for")
    return parser.parse_known_args()

def main():
    args, remaining = parse_args()

    if remaining:
        print(f"Warning: Unrecognized arguments: {remaining}")

    if args.mode == "test":
        print("Running in test mode...")
        tests.start_validation(args)
        return
    
    print("Running in normal mode...")
    tracker = ExpenseTracker(args.file)
    tracker.run()