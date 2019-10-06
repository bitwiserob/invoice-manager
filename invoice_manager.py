from invoice import Invoice
# Going to need date, invoice number from contact
# Then update invoice count for object


class Invoice_manager:
    invoice_book = {}
    def __init__(self):
        self.con_mgr = None

    def print(self):
        self.con_mgr.display_contact()
        
    def create_invoice(self):
        self.current_invoice = Invoice(self.selected_contact)

    def select_contact(self, contact):
        self.selected_contact = contact

    def get_selected_contact(self):
        return self.selected_contact

    def get_current_invoice(self):
        return self.current_invoice
    
    def export_current_invoice(self):
        print(self.current_invoice.get_date())
        export_string = "INVOICE{} \n Billing Address: {}\t {}".format(self.current_invoice.get_invoice_number(),
                                                                       self.current_invoice.get_billing_area(),
                                                                       self.current_invoice.get_date())
        
        print(export_string)
        input()
        with open("invoicetest.txt", "w") as file:
            file.write(export_string)

            
        