import re
import core.library.tools.pdf_utils as PDF
from core.library.invoices.invoice import Invoice
from core.library.invoices.banks.conts import BBVA_CHARGES, BBVA_PAYMENTS

class BBVAInvoice(Invoice):
    def __init__(self, invoice):
        super().__init__()
        pdf_text= PDF.extract_text_pdf(invoice)
        self._get_charges(pdf_text)
        self._get_payments(pdf_text)

    def _get_charges(self, pdf_text):
        pattern = BBVA_CHARGES
        match_list = re.findall(pattern, pdf_text)
        output = []
        for charge in match_list:
            output.append(list(charge))
        self.charges = output
        self.total_charges = self._get_sum(self.charges)

    def _get_payments(self, pdf_text):
        pattern = BBVA_PAYMENTS
        match_list = re.findall(pattern, pdf_text)
        output = []
        for payment in match_list:
            if "PAGO TDC" in payment[1]:
                continue
            payment = list(payment)
            payment[2] = f'-{payment[2]}'
            output.append(payment)
        self.payments = output
        self.total_payments = self._get_sum(self.payments)


    def _get_sum(self, charges: list) -> float:
        total = 0
        for charge in charges:
            charge[2] = charge[2].replace(",","")
            total = total + float(charge[2])

        return total
