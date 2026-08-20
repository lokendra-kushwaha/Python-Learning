"""
Student Result Management System

A simple command-line Python application that generates a unique ID for new users,
saves their academic marks in a text file, and calculates their percentage. 
Returning users can log in using their Unique ID to view their saved results.
"""

from random import randint

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

def display_result(student_name, fathers_name, roll_number, result_class, subjects_marks):
    """
    Formats and prints the student's result to the console.
    
    Args:
        student_name (str): The name of the student.
        fathers_name (str): The father's name.
        roll_number (str): The student's roll number.
        result_class (str): The class/grade of the student.
        subjects_marks (dict): A dictionary containing subject names as keys and marks as values.
    """
    print(f"\nName:     {student_name}          Father's Name: {fathers_name}")
    print(f"Roll No.: {roll_number}           Class:         {result_class}")
    print("\nSubject Name : Marks") 
    print("-" * 30)
    
    for subject, marks in subjects_marks.items():
        print(f"{subject} | {marks}/100")
        
    total = sum(subjects_marks.values())
    total_subjects = len(subjects_marks)
    
    print("-" * 30)
    print(f"Total Marks : {total}")
    if total_subjects > 0:
        print(f"Your Percentage: {total/total_subjects:.2f}%\n")
    else:
        print("Your Percentage: 0.00%\n")


def main():
    """Main loop that drives the entire application logic."""
    print("Welcome! If you have a Unique ID, please enter it to see your result, or Login to create one.") 
    
    while True:
        ask_for_user_id = input("""
1. See Result
2. Login / Register
3. Exit
-----------------> """).strip() 
        
        if ask_for_user_id == '1':
            user_id = input("\nEnter your Login ID: ").strip()
            try:
                 # Reading user data from their respective unique_id.txt file
                 with open(f"{user_id}.txt", "r") as f:
                      print("\n" + "="*20 + " YOUR RESULT " + "="*20)
                      print(f.read())
                      print("="*53 + "\n")

            except FileNotFoundError:
                print("This Unique ID does not exist. Please Login (Option 2) first!\n")
            except Exception as e:
                print(f"An unexpected error occurred: {e}\n")

        elif ask_for_user_id == '2':
            # Asking for user details to create a profile
            student_name = input("\nEnter Your Name: ").title().strip()
            roll_number = input("Enter Your Roll No.: ").strip()
            fathers_name = input("Enter Your Father's Name: ").title().strip()
            result_class = input("Enter Your Class: ").title().strip()
            
            # Generating a Unique ID (removing spaces to keep the ID clean)
            user_id = f"{student_name.replace(' ', '')}{randint(100, 999)}".lower() 

            print(f"\nYour Unique Id is {user_id}")
            print("-" * 50)
            print("Save Your Result")
            print("-" * 50)
            
            # Prompting for total subjects with error handling
            total_subjects = get_valid_integer("Enter Your total no. of Subjects: ")
            subjects_marks = {}

            for i in range(total_subjects): 
                subject_name = input(f"{i+1}. Subject: ").title().strip()
                # Prompting for marks with error handling
                total_marks = get_valid_integer("Enter Your Marks: ")
                subjects_marks[subject_name] = total_marks 

            # Calling the function to display the formatted result
            display_result(student_name, fathers_name, roll_number, result_class, subjects_marks) 

            # Saving user data into unique_id.txt
            try:
                with open(f'{user_id}.txt', 'w') as f:
                    f.write(f"Name:     {student_name}          Father's Name: {fathers_name}\n")
                    f.write(f"Roll No.: {roll_number}           Class:         {result_class}\n")
                    f.write("\nSubject Name : Marks\n")
                    f.write("-" * 30 + "\n")
                    
                    for subject, marks in subjects_marks.items():
                        f.write(f"{subject} | {marks}/100\n")

                    total = sum(subjects_marks.values())
                    f.write("-" * 30 + "\n")
                    f.write(f"Total Marks : {total}\n")
                    if total_subjects > 0:
                        f.write(f"Your Percentage: {total/total_subjects:.2f}%\n")
                print("Your result has been successfully saved!\n")
            except Exception as e:
                print(f"An error occurred while saving the file: {e}")

        elif ask_for_user_id == '3': 
            print("Exiting the system. Have a great day!")
            break
            
        else:
            print("Invalid Option! Please select 1, 2, or 3.")

# Standard Python convention to execute the main function
if __name__ == "__main__":
    main()