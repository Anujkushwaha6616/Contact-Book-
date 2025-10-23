# Contact Book

file = "contacts.txt"

def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")
    with open(file, "a") as f:
        f.write(f"{name} - {phone}\n")
    print("Contact Saved!")

def view_contacts():
    print("\n--- Contact List ---")
    try:
        with open(file, "r") as f:
            data = f.read()
            print(data if data else "No contacts found.")
    except FileNotFoundError:
        print("No contacts found.")

def search_contact():
    search = input("Enter name to search: ").lower()
    found = False
    try:
        with open(file, "r") as f:
            for line in f:
                if search in line.lower():
                    print("Found:", line.strip())
                    found = True
        if not found:
            print("No contact found.")
    except FileNotFoundError:
        print("No contacts file found.")

while True:
    print("\n1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Exit")
    ch = input("Enter choice: ")
    if ch == "1":
        add_contact()
    elif ch == "2":
        view_contacts()
    elif ch == "3":
        search_contact()
    elif ch == "4":
        print("Exiting Contect Book.!")
        break
    else:
        print("Invalid choice!")
