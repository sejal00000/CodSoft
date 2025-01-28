import os
clear = lambda:os.system('cls')
class Contact:
    
    def __init__(self, name, number , email, address):
        self.name = name
        self.number = number
        self.email = email
        self.address = address
        
    def display(self):
        return f"Name: {self.name}, Number: {self.number}, Email ={self.email}, Address: {self.address}"
    
contacts_list = []

def add_contact():
    clear()
    name = input("Enter name: ")
    
    while True:
        number = input("Enter number: ")
        if len(number) > 10:
            print("Number length Not Possible")
        elif not number.isdigit():
            print("Number Must Contain Only Digit")
        else:
            break
        
    email = input("Enter email: ")
    if not email.endswith('@gmail.com'):
        email += "@gmail.com"
    address = input("Enter address: ")
    new_contact = Contact(name, number, email , address)
    contacts_list.append(new_contact)
    print("Contact Added Successfully !!\n")
    
def view_contact_list():
    if not contacts_list:
        print("Ooops no Contacts Found!\n")
    else:
        print("List of Contacts: ")
        for contact in contacts_list:
            print(contact.display())
            
        print()
        input("\nPress Enter To Continue.")
        
def search_contact():
    clear()
    if not contacts_list:
        print("No contacts available to search!\n")
        return None
    search_term = input("Enter Name or Number to Search: ")
    for contact in contacts_list:
        if search_term.lower() == contact.name.lower() or search_term == str(contact.number):
            print("Contact Found!!")
            print(contact.display(),"\n")
            return contact
           
    print("Contact Not Found!!\n")
    return None
    
def update():
    clear()
    contact_to_update = search_contact()
    if contact_to_update:
        print("Update Contact Details: ")
        contact_to_update.name = input("Enter Name: ") or contact_to_update.name
        contact_to_update.number = input("Enter Number: ") or contact_to_update.number
        contact_to_update.email = input("Enter Email: ") or contact_to_update.email
        contact_to_update.address = input("Enter Address: ") or contact_to_update.address
        print("Contact Updated Successfully!!\n",contact_to_update.display(),"\n")

        
def delete_contact():
    clear()
    if not contacts_list:
        print("No contacts available to delete!\n")
        return
    while True:
        contact_to_delete = search_contact()
        if contact_to_delete :
            contacts_list.remove(contact_to_delete)
            print("Contact Deleted Successfully!!\n ")
            if not contacts_list:
                print("All contacts are deleted!\n")
                break
            
        else:
            print("No Matching Contact")
        while True:
            b = input("Delete Another Contact? (y/n): ")
            if b.lower() == "n":
                return
            elif b.lower() == "y":
                break
            elif b.lower() != "n":
                print("Invalid Input")
def menu():
    while True:
        clear()
        print("\n ---- Contact Book ----\n")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        
        try:
            choice = int(input("\nEnter an option: "))
        except ValueError:
            print("Invalid Input! Please enter a number between 1 to 6\n")
            continue 
        
        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact_list()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update()
        elif choice == 5:
            delete_contact()
        elif choice == 6:
            print("Exiting...")  
            break
        else:
            print("Invalid Choice!!\n ")
            
menu()