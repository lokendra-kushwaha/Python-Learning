"""
Contact Management System

A beginner-phase CRUD (Create, Read, Update, Delete) application built using 
Python's core File I/O and OS modules. It allows users to register, save 
contact details, and manage their address book via individual text files.

Created By: Lokendra Kushwaha (Legacy Archive)
"""

from random import randint
import os

# Set a dynamic directory for saving files so it works on any computer
DATA_DIR = "Contact_Files"

def setup_environment():
    """Creates the necessary directories if they don't exist."""
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

def save_contact(user_id):
    """
    Prompts the user for contact details and saves them to a text file.
    
    Args:
        user_id (str): The unique ID of the currently logged-in user.
    """
    print("\n--- Enter Contact Details ---")
    person_name = input("Enter Person Name: ").strip().lower()
    
    try:
        person_mobile = int(input("Enter Person's Mobile No.: "))
    except ValueError:
        print("Invalid Mobile Number! Saving as 0000000000.")
        person_mobile = 0000000000
        
    person_email = input("Enter Person's Email: ").strip()
    person_address = input("Enter Person's Address: ").strip()
    person_rel = input("Enter his/her relation with you: ").strip()

    # Saving individual contact file
    file_path = os.path.join(DATA_DIR, f"{user_id}{person_name}.txt")
    with open(file_path, 'w') as contact:
        contact.write('-' * 40)
        contact.write(f"\nName     : {person_name.title()}\n")
        contact.write(f"Mobile No: {person_mobile}\n")
        contact.write(f"Email    : {person_email.lower()}\n")
        contact.write(f"Address  : {person_address.title()}\n")
        contact.write(f"Relation : {person_rel.capitalize()}\n")
        contact.write('-' * 40 + '\n')
        
    # Appending to user's master contact list
    master_file = os.path.join(DATA_DIR, f"{user_id}.txt")
    with open(master_file, 'a') as contact:
        contact.write('-' * 40)
        contact.write(f"\nName     : {person_name.title()}\n")
        contact.write(f"Mobile No: {person_mobile}\n")
        contact.write(f"Email    : {person_email.lower()}\n")
        contact.write(f"Address  : {person_address.title()}\n")
        contact.write(f"Relation : {person_rel.capitalize()}\n")
        contact.write('-' * 40 + '\n')
        
    print("\n" + "-" * 40)
    print('Your Contact Saved Successfully!')
    print("-" * 40 + "\n")


def main():
    """Main loop driving the Contact Management System."""
    setup_environment()
    print("Welcome to the Contact Management System!\n")
    
    user_id = ""
    
    while True: 
        user_input = input("1: Login/Register | 2: Manage Contacts | 3: Exit \nChoose an option: ").strip()
        print("\n")
        
        if user_input == '1': 
            user_fname = input('Enter Your First Name: ').strip().lower()
            user_lname = input('Enter Your Last Name: ').strip()
            user_mobile = input('Enter Your Mobile No.: ').strip()
            user_email = input('Enter Your Email ID: ').strip()
            user_dob = input('Enter Your Date Of Birth: ').strip()
            
            user_id = f"{user_fname}{randint(100, 999)}"
            print("-" * 50)
            print(f"Login Successful! Your User ID is: {user_id}")
            print("-" * 50, "\n")

            while True:
                ask_user_for_save = input("Do you want to save a contact? (Yes/No): ").strip().title()
                if ask_user_for_save == 'Yes': 
                    save_contact(user_id)
                elif ask_user_for_save in ['No', 'Exit']: 
                    break
        
        elif user_input == '2': 
            print("1: View Contact(s) | 2: Update Contact | 3: Delete Contact | 4: Add New Contact")
            user_input_for_manage = input("Choose an option: ").strip()
            
            if user_input_for_manage == '1':  
                ask_for_user_id = input("Enter your User ID: ").strip().lower() 
                ask_for_person_name = input("Enter person's name (or leave blank for full list): ").strip().lower() 
                
                search_file = os.path.join(DATA_DIR, f"{ask_for_user_id}{ask_for_person_name}.txt")
                try:
                    with open(search_file, "r") as contact_details:
                        print(f"\n{contact_details.read()}") 
                except FileNotFoundError:
                    print("\nError: User ID or Contact Doesn't Exist.\n")
            
            elif user_input_for_manage == '2': 
                ask_for_user_id = input("Enter your User ID: ").strip().lower() 
                ask_for_person_name = input("Enter the name of the contact to update: ").strip().lower() 
                
                old_file_path = os.path.join(DATA_DIR, f"{ask_for_user_id}{ask_for_person_name}.txt")
                
                if os.path.exists(old_file_path):
                    print("\n--- Enter Updated Details ---")
                    updated_name = input("Updated Name: ").strip().lower()
                    updated_mobile = input("Updated Mobile No.: ").strip()
                    updated_email = input("Updated Email: ").strip()
                    updated_address = input("Updated Address: ").strip()
                    updated_rel = input("Updated Relation: ").strip()

                    # Removing old file and creating new one
                    os.remove(old_file_path) 
                    new_file_path = os.path.join(DATA_DIR, f"{ask_for_user_id}{updated_name}.txt")
                    
                    with open(new_file_path, 'w') as contact: 
                        contact.write('-' * 40)
                        contact.write(f"\nName     : {updated_name.title()}\n")
                        contact.write(f"Mobile No: {updated_mobile}\n")
                        contact.write(f"Email    : {updated_email.lower()}\n")
                        contact.write(f"Address  : {updated_address.title()}\n")
                        contact.write(f"Relation : {updated_rel.capitalize()}\n")
                        contact.write('-' * 40 + '\n')
                        
                    print("-" * 50)
                    print("Contact Updated Successfully!")
                    print("-" * 50, "\n")
                else:
                    print("\nError: Contact Doesn't Exist.\n")
            
            elif user_input_for_manage == '3': 
                ask_for_user_id = input("Enter your User ID: ").strip().lower() 
                ask_for_person_name = input("Enter the name of the contact to delete: ").strip().lower() 
                
                file_to_delete = os.path.join(DATA_DIR, f"{ask_for_user_id}{ask_for_person_name}.txt")
                
                try:
                    os.remove(file_to_delete) 
                    print("-" * 50)
                    print("Contact Deleted Successfully!")
                    print("-" * 50, "\n")
                except FileNotFoundError: 
                    print("\nError: User ID or Contact Doesn't Exist.\n")
                
            elif user_input_for_manage == '4':
                if not user_id:
                    user_id = input("Please enter your User ID first: ").strip().lower()
                save_contact(user_id)

        elif user_input == '3': 
            print("Exiting system. Have a great day!")
            break
        else: 
            print("Invalid Input! Please Choose 1, 2, or 3.\n") 

if __name__ == "__main__":
    main()