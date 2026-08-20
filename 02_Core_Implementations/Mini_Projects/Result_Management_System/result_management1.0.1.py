"""
Student Result Management System - Version 2.0

This upgraded command-line application allows students to log in, save their marks, 
and view their personal results. It also features a global tracker that saves all 
students' total marks to find the Maximum and Minimum scores across the system.
"""

from random import randint
import os

def get_valid_integer(prompt):
    """
    Prompts the user repeatedly until a valid integer is entered.
    This acts as error handling to prevent the program from crashing 
    if a user types letters instead of numbers.
    
    Args:
        prompt (str): The message displayed to the user.
        
    Returns:
        int: The valid integer entered by the user.
    """
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")

def main():
    print("Welcome to Result Management System!\n") 
    
    while True:
        # A cleaner menu for the user
        ask_for_user_id = input("""
Choose an option:
1. See Your Result (Enter Unique ID)
2. Login / Register
3. See Maximum/Minimum Score
4. Exit
-----------------> """).strip()
        
        if ask_for_user_id == '1':
            user_id = input("\nEnter your Unique ID: ").strip()
            try:
                 with open(f"{user_id}.txt", "r") as f:
                      print("\n--- YOUR RESULT ---")
                      print(f.read())
                      print("---------------\n")
            except FileNotFoundError:
                print("Unique ID Doesn't Exist. Please Login!\n")

        elif ask_for_user_id == '2':
            # Asking for user details for login
            student_name = input("\nEnter Your name: ").title().strip()
            roll_number = input("Enter Your Roll No.: ").strip()
            fathers_name = input("Enter Your Father's Name: ").title().strip()
            result_class = input("Enter Your Class: ").title().strip()
            
            user_id = f"{student_name.replace(' ', '')}{randint(100, 999)}".lower() 

            print(f"\nYour Unique Id is {user_id}")
            print("-" * 50)
            print("Save Your Result")
            print("-" * 50)
            
            try:
                total_subjects = get_valid_integer("Enter Your total no. of Subjects: ")
                subjects_marks = {} 
                
                for i in range(total_subjects):  
                    subject_name = input(f"{i+1}. Subject: ").strip()
                    total_marks = get_valid_integer("Enter Your Marks: ")
                    subjects_marks[subject_name] = total_marks 
                
                total = sum(subjects_marks.values()) 
                
                # Printing the result to console
                print(f"\nName:     {student_name}          Father's Name: {fathers_name}")
                print(f"Roll No.: {roll_number}           Class:         {result_class}")
                print("Subject Name : Marks") 
                for subject, marks in subjects_marks.items(): 
                    print(f"{subject} | {marks}/100")
                
                print(f"Total Marks : {total}") 
                print(f"Your Percentage: {total/total_subjects:.2f}%\n") 

                # Saving personal result
                with open(f'{user_id}.txt', 'w') as f:
                    f.write(f"Name:     {student_name}          Father's Name: {fathers_name}\n")
                    f.write(f"Roll No.: {roll_number}           Class:         {result_class}\n")
                    f.write("\nSubject Name : Marks\n")
                    for subject, marks in subjects_marks.items():
                         f.write(f"{subject} | {marks}/100\n")
                    f.write(f"Total Marks : {total}\n")
                    f.write(f"Your Percentage: {total/total_subjects:.2f}%\n")

                # Saving total marks to the global tracker for Max/Min logic
                with open('maxMinMarks.txt', 'a') as file:
                    file.write(f"{total}\n")
                    
                print("Result and Global Score Tracker updated successfully!\n")

            except ValueError:
                print("Invalid input! Please enter numbers for subjects and marks.\n")

        elif ask_for_user_id == '3':
            # Checking Maximum and Minimum marks safely
            try:
                with open('maxMinMarks.txt', 'r') as file:
                    marks_txt = file.readlines()
                    
                # Using strip() is safer than removesuffix() for newlines
                marks_int_list = [int(item.strip()) for item in marks_txt if item.strip()]
                
                if marks_int_list:
                    print(f"\nThe Maximum Score: {max(marks_int_list)} Marks")
                    print(f"The Minimum Score: {min(marks_int_list)} Marks\n")
                else:
                    print("\nNo scores have been registered yet!\n")
                    
            except FileNotFoundError:
                print("\nNo data found! Students need to register their results first.\n")

        elif ask_for_user_id == '4': 
            print("Exiting...")
            break
             
        else:
            print("Invalid Input! Please select a valid option.\n")

if __name__ == "__main__":
    main()