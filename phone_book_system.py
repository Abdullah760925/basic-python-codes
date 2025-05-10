# phone_book_system.py

contacts = []

def add_contact():
    name = input("Enter contact name: ")
    number = input("Enter phone number: ")
    
    contact = {"name": name, "phone": number}
    contacts.append(contact)
    print("📇 Contact saved!\n")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.\n")
        return

    print("\nYour Contacts:")
    for contact in contacts:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    found = False

    for contact in contacts:
        if contact['name'].lower() == name.lower():
            print(f"🔍 Found: {contact['name']} - {contact['phone']}\n")
            found = True
            break

    if not found:
        print("❌ Contact not found.\n")

def main():
    while True:
        print("==== Phone Book ====")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("Goodbye 👋")
            break
        else:
            print("❌ Invalid option.\n")

main()
