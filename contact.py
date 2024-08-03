def add_contact(contacts):
    name = input("Name: ")
    contact_number = input("Contact Number: ")
    email = input("Email: ")
    address = input("Address: ")

    contact = {
        "name": name,
        "contact_number": contact_number,
        "email": email,
        "address": address
    }

    contacts.append(contact)
    print("Contact added successfully!")

def view_contacts(contacts):
    print("\nName\t\tContact Number\t\tEmail\t\t\tAddress")
    print("-" * 80)
    for contact in contacts:
        print(f"{contact['name']}\t\t{contact['contact_number']}\t\t{contact['email']}\t\t{contact['address']}")

def search_contact(contacts):
    search_term = input("\nEnter search term (name or email): ")
    print("Search results:")
    found = False
    for contact in contacts:
        if search_term.lower() in contact['name'].lower() or search_term.lower() in contact['email'].lower():
            print(f"Name: {contact['name']}, Phone Number: {contact['contact_number']}, Email: {contact['email']}, Address: {contact['address']}")
            found = True
    if not found:
        print("No records found.")

def delete_contact(contacts):
    name = input("\nEnter the name of the contact to delete: ")
    for i, contact in enumerate(contacts):
        if name.lower() == contact['name'].lower():
            del contacts[i]
            print(f"Contact '{name}' deleted successfully.")
            return
    print("Contact not found.")

def main():
    contacts = []

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
