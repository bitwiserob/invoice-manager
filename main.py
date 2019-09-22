from invoice_manager import Invoice_manager
from Contact_manager import Contact_manager
inv_mgr = Invoice_manager()
con_mgr = Contact_manager()
#Menu
def main_menu():
    print("options should be:")
    print("1:\tCreate contact")
    print("2:\tView contacts")
    print("3:\tSave contact")
    print("4:\tload contacts")
    input_option = input("Enter Option:")
    print(input_option) 
    if(int(input_option) == 1):
        con_mgr.create_contact()
        print(con_mgr.display_contact())
    if(int(input_option) == 2):
        print(con_mgr.display_contact())
    if(int(input_option) == 3):
        con_mgr.save_contacts()
    if(int(input_option) == 4):
        con_mgr.load_contacts()
        main_menu()
    else:
        print("invalid selection")
        main_menu()

main_menu()