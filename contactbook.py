import pickle

contacts = {}


def addContact(name, phoneNum, email, address):
    contacts[name] = {"phoneNum": phoneNum, "email": email, "address": address}
    print("Contact added successfully.")
    saveContacts()


def saveContacts():
    file = "contacts.pickle"
    with open(file, "wb") as fileObj:
        pickle.dump(contacts, fileObj)


def loadContacts():
    file = "contacts.pickle"
    try:
        with open(file, "rb") as fileObj:
            loaded_contacts = pickle.load(fileObj)
            return loaded_contacts
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact list.")
        return {}


def updateContact(name, phoneNum=None, email=None, address=None):

    if name in contacts:
        if phoneNum:
            contacts[name]["phoneNum"] = phoneNum
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address
        print("Contact updated successfully.")
        saveContacts()
    else:
        print("Contact not found.")


def deleteContact(name):
    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully.")
        saveContacts()
    else:
        print("Contact not found.")


def searchContact(name):
    found = False
    for contact_name, info in contacts.items():
        if name == contact_name:
            found = True
            print(
                f"\nName: {contact_name}, Phone Number: {info['phoneNum']}, Email: {info['email']}, Address: {info['address']}"
            )
            break
        elif name == info["phoneNum"]:
            found = True
            print(
                f"\nName: {contact_name}, Phone Number: {info['phoneNum']}, Email: {info['email']}, Address: {info['address']}"
            )
            break

    if not found:
        print("Contact not found.")


def showContacts():
    if contacts:
        print("\n\t ===Contacts===")
        print("   Names\t\tNumber\n")

        for i, (name, info) in enumerate(contacts.items(), 1):
            print(f"{i}. {name}\t\t{info['phoneNum']}")
    else:
        print("No contacts found.")


contacts = loadContacts()

while True:
    print("\n====== CONTACT BOOK ======")
    menu = input(
        "1. Add Contact\n2. Show Contacts\n3. Update Contact\n4. Delete Contact\n5. Search Contact\n6. Exit\nEnter your choice: "
    )

    if menu == "1":
        name = input("Enter Name: ").capitalize()
        phoneNum = int(input("Enter Phone Number: "))
        email = input("Enter Email: ")
        address = input("Enter Address: ")
        addContact(name, phoneNum, email, address)
    elif menu == "2":
        showContacts()
    elif menu == "3":
        name = input("Enter Name: ")
        if name in contacts:
            phoneNum = input("Enter New Phone Number (Leave blank to keep current): ")
            email = input("Enter New Email (Leave blank to keep current): ")
            address = input("Enter New Address (Leave blank to keep current): ")
            updateContact(name, phoneNum, email, address)
        else:
            print("\nContact not found")
            saveContacts()
    elif menu == "4":
        name = input("Enter Name: ")
        deleteContact(name)
    elif menu == "5":
        name = input("Enter Name or Phone number: ")
        searchContact(name)
    elif menu == "6":
        print("Exiting...")
        saveContacts()
        break
    else:
        print("Invalid choice.")
