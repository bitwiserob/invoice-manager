from invoice_manager import Invoice_manager
from Contact_manager import Contact_manager
import os.path
import os


inv_mgr = Invoice_manager()
con_mgr = Contact_manager()
# Menu

def auto_load():
    if(os.path.isfile(con_mgr.file_name)) == True:
        con_mgr.load_contacts()
        return True
    else:
        open(con_mgr.file_name, 'a').close()


def main_menu():
    os.system('cls||clear')
    if(auto_load() == True):
        print("Contact File Auto Loaded")
    
    print("options should be:")
    print("1:\tCreate contact")
    print("2:\tView contacts")
    print("3:\tSave contacts")
    print("4:\tload contacts")
    print("5:\tmodify contact")
    input_option = input("Enter Option:\n")

    if(int(input_option) == 1):
        con_mgr.create_contact()
        print(con_mgr.contact_book)
        main_menu()

    if(int(input_option) == 2):
        print("launched 2")
        con_mgr.display_contact()

    if(int(input_option) == 3):
        con_mgr.save_contacts()

    if(int(input_option) == 4):
        con_mgr.load_contacts()
        main_menu()

    if(int(input_option) == 5):
        user_input = input("Enter Contact ID\n")
        con_mgr.modify_contact(user_input)
        main_menu()

    else:
        print("invalid selection")
        main_menu()


main_menu()
