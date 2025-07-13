BBVA_CHARGES  = r'(\d{2}-\w{3}-\d{4})\s\d{2}-\w{3}-\d{4}\s(.*)(?:\s;\s?Tarjeta Digital\s\*+\d{4})?\s\+\s\$(.*)'
BBVA_PAYMENTS = r'(\d{2}-\w{3}-\d{4})\s\d{2}-\w{3}-\d{4}\s(.*)\s\-\s\$(.*)'
BBVA_MONTHLY_PAYMENTS = r'Pago para No generar\nIntereses\s\$\s(?P<Total>.*\.\d{2})\n\s*Capital\s\$\s(?P<Capital>.*\.\d{2})\n\s*Intereses\s\$\s(?P<Intereses>.*\.\d{2})\n\s*Comisiones\s\$\s(?P<Comisiones>.*\.\d{2})\n\s*IVA\s\$\s(?P<IVA>.*\.\d{2})'

