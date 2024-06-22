import re
import os 

contacts = {}

def display_menu():
    print("Welcome to the Contact Management System!") 
    print("Menu:")
    print("1. Add a new contact")
    print("2. Edit an existing contact")
    print("3. Delete a contact")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Export contacts to a text file")
    print("7. Import contacts from a text file *BONUS*")
    print("8. Quit")

def input_contact_info():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    additional_info = input(" Enter")
    
    if not re.match(r'^\+?\d{10,15}$', phone):
        print("Invalid phone number format. Plese use 10 to 15 digits.")
        return None
    
    if not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', email):
        print("Inavlid email address format.")
        return None
    
    return {
        'Name': name,
        'Phone': phone,
        'Email': email,
        'Additional Info': additional_info  
      }

def add_contact():
    contact = input_contact_info()
    if contact:
        contacts[contact['Phone']] = contact
        print("Contact added successfully.")

def edit_contact():
    phone = input("Enter the phone number of the contact to edit: ")
    if phone in contacts:
        print("Editing contact: ", contacts[phone])
        contact = input_contact_info()
        if contact:
            contacts[phone] = contact
            print("Contact updated successfully.")
    else:
        print("Contact not found.")

def delete_contact():
    phone = input("Enter the phone number of the contact to delete: ")
    if phone in contacts:
        del contacts[phone]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    phone = input("Enther the phone number of the contact to search: ")
    if phone in contacts:
        print("Contact details: ", contacts[phone])
    else:
        print("Contact not found")

def display_all_contacts():
    if contacts:
        for phone, info in contacts.items():
            print(f"Phone: {phone}, Details: {info}")
    else:
        print("No contacts available.")

def export_contacts(filename):
    try:
        with open(filename, 'w') as file:
            for contact in contacts.values():
                file.write(f"{contact['Name']}, {contact['Phone']}, {contact['Email']}, {contact['Additional Info']}\n")
        print(f"Contacts exported to {filename} successfully.")
    except Exception as e:
        print(f"Error exporting contacts: {e}")

def immport_contacts(filename):
    try:
        with open(filename, 'r') as file:
            for line in file:
                name, phone, email, additional_info = line.strip().split(',')
                contacts[phone] = {
                    'Name': name,
                    'Phone': phone,
                    'Email': email,
                    'Additional Info': additional_info
                }
        print(f"Contacts imported from {filename} successfully.")
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except Exception as e:
        print(f"Error importing contacts: {e}")

def main():
    while True:
        display_menu()
        choice = input("Select an option: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            filename = input("Enter the filename to export contacts: ")
            export_contacts(filename)
        elif choice == '7':
            filename = input("Enter the filename to import contacts: ")
            import_contacts(filename)
        elif choice == '8':
            print("Exiting the Contact Management System. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()


    