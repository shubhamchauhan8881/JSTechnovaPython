
# Contact Manager
# -> Take contact details as input
# -> Add them to Array
# -> Print contacts

# [
#     {
#         "name":"",
#         "phone": "",
#         "email":"",
#     },

#     {
#         "name":"",
#         "phone": "",
#         "email":"",
#     }
# ]

# File Handling
# Database


contact_details = [ ]



def add_contact():
    global contact_details

    name = input("Enter you name: ")
    phone = input("Enter you phone: ")
    email = input("Enter you email: ")

    my_dict = {
        "user_name" : name,
        "user_phone": phone,
        "user_email": email
    }
    contact_details.append(my_dict)
    print("User details added.")


def print_contacts():
    index = 0
    for each_user in contact_details:
        print("Sr. No.", index)
        print("Name: ", each_user["user_name"] )
        print("Phone: ", each_user["user_phone"] )
        print("Email: ", each_user["user_email"] )
        index += 1
        print("\n")


def delete_contact():
    global contact_details

    print_contacts()
    index = int( input("Enter Sr. no of contact which you want to delete: ") )
    deleted_contact = contact_details.pop( index ) #{}
    print(f"Contact details of {deleted_contact['user_name'] } was deleted!" )

def mainApp():

    while True:
        print("Contact Manager App: ")
        print("1. Add Contact")
        print("2. Show Contacts")
        print("3. Delete Contact")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == '2':
            print_contacts()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            break
        else:
            print("Invalid input.")

mainApp()