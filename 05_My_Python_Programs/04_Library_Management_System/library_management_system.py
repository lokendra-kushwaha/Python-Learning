"""
Library Management System
=========================
A comprehensive, terminal-based Library Management System built using Python.

This system manages user/admin accounts, book inventory, borrowing/returning 
records, and fine calculations. It features a custom File I/O database engine 
for persistent data storage and utilizes the 'rich' library to deliver a 
premium, interactive Command Line Interface (CLI).

Author: Lokendra
"""

import random
import datetime 
import time
import os

# Importing UI components from the Rich library for a premium terminal experience
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.rule import Rule

# Initializing the main console object used across the entire application
console = Console()


#==========================================================================================================
#                                       SYSTEM INITIALIZATION & WELCOME
#==========================================================================================================

print("\n")

# TRICKY SYNTAX: UI Centering
# using the native justify="center" in console.print() ensures the panel is always perfectly 
# centered dynamically, regardless of the user's terminal window size.
welcome_panel = Panel(
    "Welcome to Lokendra's Library!", 
    style="#FF69B4 bold", 
    padding=(1, 2)
)
console.print(welcome_panel, justify="center")


#=================================================================================================
#                               UI Notifications, Dividers & Status Spinners
#=================================================================================================


def get_input(prompt_message: str) -> str:
    """
    Prompts the user for styled input using the Rich console.

    Args:
        prompt_message (str): The prompt text to display.

    Returns:
        str: The raw input entered by the user.
    """
    return console.input(f"[bold cyan]{prompt_message}[/bold cyan]")


def get_print(prompt_message: str) -> str:
    """
    Prints a bold cyan styled message to the terminal.

    Args:
        prompt_message (str): The message text to display.
    """
    console.print(prompt_message, style="bold cyan")


def show_success(prompt_message: str) -> str:
    """
    Displays a prominent green success alert message.

    Args:
        prompt_message (str): The success message details to display.
    """
    console.print("☑️  Success!", prompt_message, style="green bold")


def show_error(prompt_message: str) -> str:
    """
    Displays a prominent red error alert message.

    Args:
        prompt_message (str): The error message details to display.
    """
    console.print("❌  Error!", prompt_message, style="red bold")


def show_warning(prompt_message: str) -> str:
    """
    Displays a prominent yellow warning alert message.

    Args:
        prompt_message (str): The warning message details to display.
    """
    console.print("⚠️  !", prompt_message, style="yellow bold")


def show_title(prompt_message: str) -> str:
    """
    Renders a centered cyan title divider across the terminal width using Rich Rule.

    Args:
        prompt_message (str): The title text to render in the horizontal divider.
    """
    # Rich Rule draws a horizontal line across the screen with text centered in the middle
    console.print(Rule(f"[bold cyan] {prompt_message} [/bold cyan]"))


def show_heading(prompt_message: str) -> str:
    """
    Renders a centered red heading divider across the terminal width using Rich Rule.

    Args:
        prompt_message (str): The heading text to render in the horizontal divider.
    """
    console.print(Rule(f"[bold red] {prompt_message} [/bold red]"))


def show_description(prompt_message: str) -> str:
    """
    Displays a secondary description or informational text in magenta.

    Args:
        prompt_message (str): The description message to display.
    """
    console.print(prompt_message, style="bold magenta")


def show_normal(prompt_message: str) -> str:
    """
    Displays a general confirmation or standard status notification in green.

    Args:
        prompt_message (str): The message text to display.
    """
    console.print("🆒  !", prompt_message, style="bold green")


def show_wait(prompt_message: str) -> str:
    """
    Displays an instructional wait notification in white.

    Args:
        prompt_message (str): The message asking the user to wait.
    """
    console.print(prompt_message, style="bold white")


# ------------------------------------------------------------------------------------------------
#                           Dynamic Status Spinners (Animated Feedback)
# ------------------------------------------------------------------------------------------------

def show_search_user():
    """Displays a fast animated spinner simulating user search in progress."""
    # The 'status' context manager automatically starts and stops the animated spinner
    with console.status("[bold magenta]⌛️ Searching Users...[/bold magenta]", spinner="dots"):
        time.sleep(0.2)


def show_loading():
    """Displays an animated spinner simulating general background loading."""
    with console.status("[bold magenta]⌛️ Please wait...[/bold magenta]", spinner="dots"):
        time.sleep(2)


def show_updating():
    """Displays an animated spinner simulating database updates."""
    with console.status("[bold magenta]⌛️ Updating...[/bold magenta]", spinner="dots"):
        time.sleep(3)


def show_adding():
    """Displays an animated spinner simulating record addition."""
    with console.status("[bold magenta]⌛️ Adding...[/bold magenta]", spinner="dots"):
        time.sleep(2)


def show_removing():
    """Displays an animated spinner simulating record deletion."""
    with console.status("[bold magenta]⌛️ Removing...[/bold magenta]", spinner="dots"):
        time.sleep(2)


def show_loading_book():
    """Displays a short animated spinner when iterating through book records."""
    with console.status("[bold magenta]⌛️ Loading....[/bold magenta]", spinner="dots"):
        time.sleep(0.2)


def show_generate():
    """Displays an animated spinner simulating unique ID generation."""
    with console.status("[bold magenta]⌛️ Generating User Id...[/bold magenta]", spinner="dots"):
        time.sleep(2)


def show_logging():
    """Displays an animated spinner simulating user authentication."""
    with console.status("[bold magenta]⌛️ Logging in...[/bold magenta]", spinner="dots"):
        time.sleep(2)


def caculating_fine():
    """Displays an animated spinner simulating fine calculation processing."""
    with console.status("[bold magenta]⌛️ Calculating Fine..[/bold magenta]", spinner="dots"):
        time.sleep(1)


#=================================================================================================
#                               UI Display Functions (Powered by Rich)
#=================================================================================================

def show_menu_style(menu_title, option_dict):
    """
    Renders a styled, interactive menu interface in the terminal using Rich.

    Converts a dictionary of menu options into a neatly formatted, borderless 
    table wrapped inside a custom panel. It specially highlights the exit options.

    Args:
        menu_title (str): The title displayed at the top of the menu panel.
        option_dict (dict): A dictionary where keys are option numbers/commands 
                            and values are their corresponding descriptions.
    """
    # Setting box=None and show_header=False creates a clean, list-like appearance 
    # instead of a rigid grid table.
    menu_table = Table(show_header=False, box=None)
    menu_table.add_column("Option", style="cyan bold", justify="right")
    menu_table.add_column("Description", style="white")

    for key, value in option_dict.items():
        # Separating and highlighting the 'Exit' option in red for better user experience
        
        if key == '0' or key.lower() == 'exit':
            menu_table.add_row("", "")
            menu_table.add_row(f"[{key}]", f"[bold red]{value}[/bold red]")
        else:
            menu_table.add_row(f"[{key}]", value)

    # expand=False ensures the panel wraps tightly around the table content 
    # rather than stretching across the entire width of the terminal.
    menu_panel = Panel(
        menu_table,
        title=f"[bold yellow]{menu_title}[/bold yellow]",
        expand=False,
        border_style="cyan"
    )
    console.print(menu_panel)


def show_profile(user, profile_details):
    """
    Renders a formatted user profile card.

    Displays user-specific details in a clean, padded panel layout.

    Args:
        user (str): The name of the user to display in the panel title.
        profile_details (dict): A dictionary containing the user's profile information.
    """
    profile_table = Table(show_header=False, box=None)
    profile_table.add_column("Option", style="cyan bold", justify="left")
    profile_table.add_column("Description", style="white")

    for key, value in profile_details.items():
        profile_table.add_row(f"{key}", value)

    profile_panel = Panel(
        profile_table,
        title=f"[bold yellow]{user}[/bold yellow]",
        expand=False,
        padding=(1, 3), # Adds vertical and horizontal space inside the border
        border_style="cyan"
    )
    # Centering the entire panel in the terminal window
    console.print(profile_panel, justify="center")


def show_dashboard(user, dashboard_details, warning):
    """
    Renders a comprehensive system dashboard with an alert section.

    Displays library statistics and a prominently styled warning or alert 
    message at the bottom of the dashboard panel.

    Args:
        user (str): The name of the logged-in user (Admin/Guest).
        dashboard_details (dict): A dictionary containing key library statistics.
        warning (str): A notification or warning message to display in red.
    """
    dash_table = Table(show_header=False, box=None)
    dash_table.add_column("Stat", style="cyan bold", justify="left")
    dash_table.add_column("Value", style="white")

    for key, value in dashboard_details.items():
        dash_table.add_row(f"{key}", value)

    dash_table.add_row("", "")
    dash_table.add_row(
        "[bold red]⚠️  ALERT[/bold red]",
        f"[bold red] {warning}[/bold red]"
    )

    dash_panel = Panel(
        dash_table,
        title=f"[bold yellow]🖥️  SYSTEM DASHBOARD [/bold yellow]",
        expand=False,
        padding=(1, 2),
        border_style="cyan"
    )
    # Printing system headers before showing the main dashboard panel
    console.print("[bold green]LOKENDRA'S LIBRARY SYSTEM[/bold green]", justify="center")
    console.print(f"[bold white]Welcome User: {user}[/bold white]", justify="center")
    console.print()
    console.print(dash_panel, justify="center")


#================================================================================================
#                         Helper/Utility Function For Validating User Inputs
#================================================================================================

def get_valid_input(prompt_message):
    """
    Prompts the user for a standard text input and prevents empty submissions.

    Args:
        prompt_message (str): The message displayed to the user.

    Returns:
        str: A validated, non-empty string.
    """
    while True:
        user_input = console.input(f"[bold cyan]👉 {prompt_message} [/bold cyan]").strip()
        if user_input:
            return user_input
        
        show_warning("Input cannot be empty. Please type something.")


def get_valid_number(prompt_message):
    """
    Prompts the user for a 10-digit mobile number and validates the integer type.

    Args:
        prompt_message (str): The message displayed to the user.

    Returns:
        int: A validated 10-digit integer.
    """
    while True:
        user_input = console.input(f"[bold cyan]👉 {prompt_message} [/bold cyan]").strip()

        if not user_input:
            show_warning("Input cannot be empty. Please enter a valid number.")
            continue

        try:
            valid_number = int(user_input)
            
            # TRICKY SYNTAX: Converting int back to str to check its exact length.
            if len(str(valid_number)) != 10:
                show_warning("Mobile no. must be 10 digits.")
                continue
            return valid_number
        
        except ValueError:
            show_warning("Invalid Input! Please enter numbers only (No alphabets/symbols)")


def get_valid_password(prompt_message):
    """
    Prompts the user to create a secure password and validates its strength.
    
    The password must be at least 6 characters long and cannot contain spaces.

    Args:
        prompt_message (str): The message displayed to the user.

    Returns:
        str: A validated, secure password string.
    """
    while True:
        password = console.input(f"[bold cyan]👉 {prompt_message} [/bold cyan]").strip()

        if not password:
            show_warning("Input cannot be empty. Please enter a valid number.")
            continue

        if len(password) < 6:
            show_warning("Password must be 6 characters.")
            continue

        if " " in password:
            show_warning("Password cannot contain spaces.")
            continue
        
        return password
    

def get_valid_email(prompt_message):
    """
    Prompts the user for an email address and performs basic syntax validation.

    Checks for the presence of the '@' symbol, a domain dot ('.'), minimum 
    length requirements, and ensures there are no spaces.

    Args:
        prompt_message (str): The message displayed to the user.

    Returns:
        str: A validated email string.
    """
    while True:
        email = console.input(f"[bold cyan]👉 {prompt_message} [/bold cyan]").strip()

        if not email:
            show_warning("Input cannot be empty. Please enter a valid email.")
            continue

        # Basic email structure validation
        if '.' not in email or '@' not in email or len(email) < 6:
            show_warning("Email address must contain a valid domain (e.g., @gmail.com).")
            continue

        if " " in email:
            show_warning("Email cannot contain spaces.")
            continue
        
        return email

def get_valid_name(prompt_message):
    """
    Prompts the user for a name and ensures it contains only alphabets and spaces.

    Args:
        prompt_message (str): The message displayed to the user.
    
    Returns:
        str: A validated name string containing only alphabets/spaces.
    """
    
    while True:
        name = console.input(f"[bold cyan]👉 {prompt_message} [/bold cyan]").strip()

        if not name:
            show_warning("Input cannot be empty. Please type something.")
            continue

        # TRICKY SYNTAX: name.replace(" ", "").isalpha()
        # A genius logic! Removes all spaces temporarily just for the check, 
        # then isalpha() verifies that everything else is purely alphabetic. 
        # This allows names like "John Doe" while blocking "John123".
        if name.replace(" ", "").isalpha() == False:
            show_warning("Name cannot contain numbers or special characters. ")
            continue
        
        return name
    

def get_valid_payment(prompt_message):
    """
    Prompts the user for a payment amount and validates it as an integer.

    Args:
        prompt_message (str): The message displayed to the user.

    Returns:
        int: A validated payment amount as an integer.
    """
    while True:
        payment = console.input(f"[bold cyan]👉 {prompt_message} [/bold cyan]").strip()

        if not payment:
            show_warning("Input cannot be empty. Please enter a amount.")
            continue

        try:
            valid_payment = int(payment)
            return valid_payment
        
        except ValueError:
            show_warning("Invalid Input! Please enter numbers only (No alphabets/symbols).")


#==========================================================================================================
#                                           CLASS LIBRARY:
#==========================================================================================================

class Library:
    """
    The main controller engine of the Library Management System.

    This class acts as the central hub, initializing the system, 
    handling the main entry point (login/signup), and directing 
    the workflow into either the Admin or User specific environments.
    """

    def __init__(self):
        """
        Initializes the Library system and automatically triggers 
        the main authentication menu.
        """
        self.menu()


    def adminWork(self):
        """
        Manages the interactive session for an authenticated administrator.

        Provides a continuous loop that displays the main admin dashboard 
        and routes the user to sub-menus for managing books, users, 
        and their personal profile. Breaks the loop upon logout.
        """
        while True: 
            # Displays the main admin menu and captures their choice
            choice = self.current_person.showMenu() 
            
            if choice == '1':
                self.current_person.adminDashboard()
            
            if choice == '2':
                manage_book_options = {
                    "1": "Search a book",
                    "2": "View all books",
                    "3": "Add a new book",
                    "4": "Remove a book",
                    "5": "View borrowed books by users",
                    "6": "Go back to Main Menu"
                }
                print("\n")
                show_menu_style("📚  MANAGE BOOKS", manage_book_options)
                manage_book_choice = get_input("Enter your choice: ")

                # Routing to specific book management operations
                if manage_book_choice == '1': 
                    self.current_person.searchBook()
                elif manage_book_choice == '2': 
                    self.current_person.viewBooks()
                elif manage_book_choice == '3':
                    self.current_person.addBook() 
                elif manage_book_choice == '4': 
                    self.current_person.removeBook()
                elif manage_book_choice == '5':
                    self.current_person.viewBorrowed()
                elif manage_book_choice == '6': 
                    pass # Returns to the start of the while loop to show the main menu

            elif choice == '3':
                manage_user_options = {
                    "1": "View all guests",
                    "2": "Add a guest",
                    "3": "Delete a guest",
                    "4": "Go back to main Menu"
                }
                print("\n")
                show_menu_style("👥  MANAGE USERS", manage_user_options)
                manage_user_choice = get_input("Enter your choice: ")

                # Routing to specific user management operation
                if manage_user_choice == '1': 
                    self.current_person.viewUsers()
                elif manage_user_choice == '2':
                    show_title("Please enter guest's details.")
                    self.current_person.userSignUp()
                elif manage_user_choice == '3':
                    self.current_person.deleteUserAccount() 
                elif manage_user_choice == '4':  
                    pass

            elif choice == '4':
                manage_profile_options = {
                                            "1": "View Profile",
                                            "2": "Edit Profile",
                                            "3": "Delete Account",
                                            "4": "Go back to Main Menu"}
                print("\n")
                show_menu_style("🛠️  MANAGE PROFILE", manage_profile_options)
                manage_profile_choice = get_input("Enter your choice: ")

                if manage_profile_choice == '1':  
                    self.current_person.viewAdminProfile()
                elif manage_profile_choice == '2':
                    self.current_person.editAdminProfile()
                elif manage_profile_choice == '3': 
                    is_deleted = self.current_person.deleteAdminAccount()
                    if is_deleted == True:
                        break
                elif manage_profile_choice == '4': 
                    pass

            elif choice in ['5']:
                # Logs the admin out by breaking the session loop
                break


    def userWork(self):
        """
        Manages the interactive session for an authenticated standard user (Guest).

        Provides a continuous loop that displays the main user dashboard 
        and routes the user to sub-menus for exploring books, managing 
        borrowed books, and updating their personal profile. Breaks the 
        loop upon logout or account deletion.
        """
        while True: 
            # Displays the main user menu and captures their choice
            choice = self.current_person.showMenu() 
            
            if choice == '1': 
                self.current_person.Userdashboard()
            
            if choice in ['2']: 
                explore_book_options = {
                    "1": "Search a book",
                    "2": "View all book",
                    "3": "Go back to Main Menu"
                }
                print("\n")
                show_menu_style("📕  EXPLORE BOOKS", explore_book_options)
                explore_book_choice = get_input("Enter your choice: ")

                # Routing to specific book exploration operations
                if explore_book_choice == '1': 
                    self.current_person.searchBook()
                elif explore_book_choice == '2': 
                    self.current_person.viewBooks()
                elif explore_book_choice == '3':
                    pass # Returns to the start of the while loop

            elif choice == '3': 
                borrow_book_options = {
                    "1": "Borrow a book",
                    "2": "Return a book",
                    "3": "View all borrowed books",
                    "4": "Return all borrowed books",
                    "5": "Go back to Main Menu"
                }
                print("\n")
                show_menu_style("📘  BORROW BOOK", borrow_book_options)
                borrow_book_choice = get_input("Enter your choice: ")

                # Routing to specific borrowing and returning operations
                if borrow_book_choice == '1': 
                    self.current_person.borrowBook()
                elif borrow_book_choice == '2':  
                    self.current_person.returnBook()
                elif borrow_book_choice == '3': 
                    self.current_person.viewBorrowedList()
                elif borrow_book_choice == '4': 
                    self.current_person.returnAllBooks()
                elif borrow_book_choice == '5':
                    pass

            elif choice in ['4']: # if choice is 4 then he/she want's to manage his/her profile
                manage_profile_options = {
                    "1": "View Profile",
                    "2": "Edit Profile",
                    "3": "Delete Account",
                    "4": "Go back to Main menu"
                }
                print("\n")
                show_menu_style("🛠️  MANAGE PROFILE", manage_profile_options)
                manage_profile_choice = get_input("Enter your choice: ")

                # Routing to specific profile management operations
                if manage_profile_choice == '1': 
                    self.current_person.viewUserProfile()
                elif manage_profile_choice == '2':
                    self.current_person.editUserProfile()
                elif manage_profile_choice== '3':
                    is_deleted = self.current_person.deleteUserAccount()
                    if is_deleted == True:
                        break # Exits the session if the user deletes their own account
                elif manage_profile_choice == '4':  
                    pass 
            
            elif choice in ['5']: 
                # Logs the user out by breaking the session loop
                break 


    def menu(self): 
        """
        The main authentication portal for the Library Management System.

        Acts as the primary gateway, dynamically assigning the 'current_person' 
        variable to either a User or Admin object based on the user's input. 
        It handles the routing for both the Sign In and Sign Up processes 
        and initiates the respective workspaces upon successful authentication.
        """
        # Initially, no one is logged into the system
        self.current_person = None
        
        while True:
            self.sign_options = {
                "1": "Sign In",
                "2": "Sign Up",
                "3": "Exit"
            }
            print("\n")
            show_menu_style("👥 SIGN IN/UP", self.sign_options)
            sign_choice = get_input("Enter your choice: ")
            
            # ---------------------------------------------------------
            # Phase 1: Sign In Process
            # ---------------------------------------------------------
            if sign_choice == '1': 
                self.user_type_option = {
                    "1": "Guest", 
                    "2": "Administrator"
                }
                print("\n")
                show_menu_style("👤 ACCOUNT", self.user_type_option)
                user_type_choice = get_input("Enter your choice: ")

                if user_type_choice == '1': 
                    print("\n")
                    show_title("Welcome to the Guest Sign In panel.")
                    print("\n")
                    
                    # Dynamically assigning the current person as a User (Guest)
                    self.current_person = User() 
                    is_signed_in = self.current_person.userSignIn()
                    
                    if is_signed_in:
                        self.userWork() # Routing to guest operations

                elif user_type_choice == '2': 
                    print("\n")
                    show_title("Welcome to the Admin Sign In panel.")
                    print("\n")

                    # Dynamically assigning the current person as an Admin
                    self.current_person = Admin()
                    is_signed_in = self.current_person.adminSignIn()
                    
                    if is_signed_in:
                        self.adminWork()

                else: 
                    show_warning("Wrong input! Please select 1 or 2.")

            # ---------------------------------------------------------
            # Phase 2: Sign Up Process
            # ---------------------------------------------------------    
            elif sign_choice == '2': 
                self.user_type_option = {
                    "1": "Guest",
                    "2": "Administrator"
                }
                print("\n")
                show_menu_style("👤 ACCOUNT", self.user_type_option)
                user_type_choice = get_input("Enter your choice: ")
                
                
                if user_type_choice == '1': 
                    print("\n")
                    show_title("Welcome to the Guest Sign Up panel.")
                    print("\n")
                    
                    self.current_person = User()
                    self.current_person.userSignUp() 
                    self.userWork() # Automatically starting session post-registration
                
                elif user_type_choice == '2': 
                    print("\n")
                    show_title("Welcome to the Admin Sign Up panel.")
                    print("\n")
                    
                    self.current_person = Admin()
                    self.current_person.adminSignUp()
                    self.adminWork() # Automatically starting session post-registration
                
                else: 
                    show_warning("Wrong input! Please select 1 or 2.")
                    continue
            
            # ---------------------------------------------------------
            # Phase 3: Exit System
            # ---------------------------------------------------------
            elif sign_choice == '3':
                print("\n")
                show_success("Thank you for using Lokendra's Library System. Goodbye!")
                break

            else: 
                show_warning("Wrong Input! Please select a valid option from the menu.")
                continue


#==========================================================================================================
#                                           CLASS ACCOUNT:
#==========================================================================================================

class Account:
    """
    Manages user (Guest/Admin) accounts in the Library Management System.
    
    This class handles the core state of a user and provides functionalities for 
    signing up and signing in. Data is persistently managed using custom File I/O.
    
    Attributes:
        fname (str): User's first name.
        lname (str): User's last name.
        mobile (str): User's mobile number.
        email (str): User's email address.
        password (str): User's account password.
        loginId (str): Auto-generated unique login ID for the user.
        userpath (str): File path for the users database.
        borrowedbook (str): File path for the borrowed books database.
    """
    def __init__(self):
        """Initializes the Account object with empty attributes and database paths."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_folder = os.path.join(base_dir, 'database')
        os.makedirs(db_folder, exist_ok=True)

        self.userpath = os.path.join(db_folder, 'users.txt')
        self.borrowedbook = os.path.join(db_folder, 'borrowedbooks.txt')
        self.bookpath = os.path.join(db_folder, 'books.txt') 
        
        for file_path in [self.userpath, self.borrowedbook, self.bookpath]:
            if not os.path.exists(file_path):
                with open(file_path, 'a') as f:
                    pass
        
        self.fname = ''
        self.lname = ''
        self.mobile = ''
        self.email = ''
        self.password = '' 
        self.loginId = '' 


    def signUp(self):
        """
        Handles the registration process for a new user/admin.
        
        Prompts the user for their details, formats the inputs, and 
        auto-generates a unique login ID.
        """
        self.fname = get_valid_name('Enter your first name: ').title()
        self.lname = get_valid_name('Enter your last name: ').title()
        self.mobile = get_valid_number('Enter your mobile no.: ')    
        self.email = get_valid_email('Enter your email: ').lower()
        self.password = get_valid_password('Make a strong password: ')
        print("\n")

        # TRICKY SYNTAX: Using f-strings to seamlessly concatenate the string (first name) 
        # with a dynamically generated random integer to create a unique ID.
        self.loginId = f"{self.fname}{random.randint(100, 999)}".lower()
        
        show_generate()
        show_success(f"Your login ID '{self.loginId}' is generated.")


    def signIn(self):
        """
        Handles the prompt process for an existing user/admin to log in.
        
        Collects the user's Login ID and password to be verified against 
        the database in a subsequent step.
        """
        self.loginId = get_valid_input('Please enter your Login ID: ') 
        self.loginpassword = console.input('[bold cyan]👉 Please enter your password: [/bold cyan]')


    def deleteAccount(self):
        """
        Authenticates the user and deletes their account from the database.

        The method prompts for credentials to verify the user's identity. 
        Before deletion, it strictly checks the borrowed books database. 
        If the user has unreturned books, the deletion request is denied.
        If cleared, it removes the user's record from the text file by 
        rewriting the file without their specific data row.

        Returns:
            bool: True if the account was successfully deleted, False if 
                  the operation was cancelled, denied, or failed.
        """
        show_description("\nEnter your login ID and password to delete your account.")
        self.varifyId = get_valid_input('Login ID: ') 
        self.varifypassword = console.input('[bold cyan]👉 Password: [/bold cyan]')
        
        if hasattr(self, 'loginpassword'):
            current_user_password = self.loginpassword
        else:
            current_user_password = self.password

        if self.varifyId == self.loginId and self.varifypassword == current_user_password:
            while True:
                print("\n")
                confirm = get_input("Please confirm if you want to proceed (type 'yes' or 'no'): ").upper() 
                if confirm == "YES":
                    try:
                        with open(self.borrowedbook, "r") as books:
                            totalbooklist = books.readlines()
                            booklist = []
                            for book in totalbooklist:
                                if book.strip(): # .strip() safely removes empty lines and newline (\n) characters.
                                    
                                    # TRICKY SYNTAX: eval()
                                    # This is a powerful built-in function that parses a string expression 
                                    # and runs it as Python code. Here, it beautifully converts a string 
                                    # that looks like a dictionary back into a real Python dictionary object.
                                    bookdict = eval(book)
                                    booklist.append(bookdict)

                            # TRICKY SYNTAX: List Comprehension
                            # A highly optimized, one-line loop that extracts only those books 
                            # where the user's loginId exists in the book dictionary.
                            borrowed_booksByUser = [borrowbook for borrowbook in booklist if self.loginId in borrowbook] # a list that stores all borrowed books by user
                            
                            if len(borrowed_booksByUser) == 0:
                                # CORE DATABASE ENGINE LOGIC: Read -> Filter -> Overwrite
                                with open(self.userpath, "r") as users: 
                                    userlist = users.readlines()
                                    updated_userlist = [] 
                                    for user in userlist: 
                                        # TRICKY SYNTAX: .split(',')
                                        # Parses the CSV-style string row into a Python list based on commas.
                                        userdetails = user.split(',')
                            
                                        if userdetails[1] == self.loginId and userdetails[2] == current_user_password:
                                            pass # Skip appending this user (effectively deleting them)

                                        else:
                                            updated_userlist.append(user)

                                    # Opening file in "w" (write) mode completely erases old content 
                                    # and replaces it with our new, filtered list.
                                    with open(self.userpath, "w") as updated_userlistfile: # writing all updated user's into database
                                        for updated_users in updated_userlist: # a loop that extract all users one by one and write to txt file
                                            updated_userlistfile.write(updated_users)
                                    
                                    show_loading()
                                    show_success("Account deleted. We will miss you!")
                                    return True
                                                                    
                            else:
                                show_loading()
                                show_error(f"Action Denied! You still have {len(borrowed_booksByUser)} borrowed books.")
                                show_warning("Please return all borrowed books and clear your dues before deleting you account.")
                                return False
        
                    except FileNotFoundError:
                        print("\n")
                        show_error("Database file not found! Please check the file path.")
                        return False
                            
                elif confirm == 'NO':
                    show_loading()
                    show_success("Account deletion request cancelled !")
                    return False

                else:
                    show_warning("Wrong Input! Please type exactly 'yes' or 'no'.")
                    continue

        else:
            show_loading()
            show_error("Login ID or password doesn't match.")
            return False


    def viewProfile(self):
        """
        Retrieves and displays the user's profile information.

        Reads the user database, finds the record matching the current 
        session's Login ID and password, formats the extracted data into 
        a dictionary, and passes it to the UI display function.

        Raises:
            FileNotFoundError: Caught internally if the user database file is missing.
        """
        try:
            with open(self.userpath, "r") as users: 
                userslist = users.readlines()

                user_details = []
                for details in userslist:
                    # .strip() removes the invisible newline character (\n) at the end of the line.
                    # .split(',') breaks the comma-separated string into a clean Python list.
                    user_details_list = details.strip().split(',')
                    
                    if hasattr(self, 'loginpassword'):
                        current_user_password = self.loginpassword
                    else:
                        current_user_password = self.password
                    
                    # Validating if the current row belongs to the logged-in user
                    if user_details_list[1] == self.loginId and user_details_list[2] == current_user_password:
                        user_details.append(user_details_list)

                for info in user_details:
                    # Mapping the raw list indices to meaningful dictionary keys for the UI.
                    # Index mapping assumption based on code: 1=ID, 3=First Name, 4=Last Name, etc.
                    profile_details = {
                                        "Login Id": f"{info[1]}",
                                        "Name": f"{info[3]} {info[4]}",
                                        "Mobile No.": f"{info[5]}",
                                        "Email Id": f"{info[6]}"
                                        }
                    show_loading()
                    print("\n")
                    show_profile(f"👤 {info[3]} {info[4]}", profile_details)
        
        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")


    def editProfile(self): 
        """
        Updates the user's profile information in the database.

        Prompts the user for their updated first name, last name, mobile number, 
        and email address. It then reads the user database, separates the current 
        user's record from the rest, modifies the target fields in memory, 
        and rewrites the entire database file to save the changes.

        Raises:
            FileNotFoundError: Caught internally if the user database file is missing.
        """
        print("\n")
        show_heading("To edit your details, please enter your updated first name, last name, mobile number, and email address.")
        self.updatedFname = get_valid_name("First name: ").title() 
        self.updatedLname = get_valid_name("Last name: ").title()
        self.updatedMobile = get_valid_number("Mobile No.: ")
        self.updatedEmail = get_valid_email("Email address: ").lower()

        try:
            with open(self.userpath, "r") as users: 
                userslist = users.readlines() 

                other_users_details = []
                user_details = [] 
                for details in userslist: 
                    user_details_list = details.strip().split(',')

                    if hasattr(self, 'loginpassword'):
                        current_user_password = self.loginpassword
                    else:
                        current_user_password = self.password
                    
                    if user_details_list[1] == self.loginId and user_details_list[2] == current_user_password: 
                        user_details.append(user_details_list)
                    
                    else:
                        other_users_details.append(user_details_list)

                # Opening the file in "w" mode to overwrite it with the updated lists
                with open(self.userpath, "w") as updatedusers: 
                    for info in user_details:
                        info[3] = self.updatedFname
                        info[4] = self.updatedLname
                        info[5] = str(self.updatedMobile) # Ensuring mobile is a string before joining
                        info[6] = self.updatedEmail
                        
                        # Reconstructing the comma-separated string from the list
                        updatedDetails = ",".join(info)
                        updatedusers.write(f"{updatedDetails}\n")

                    for info in other_users_details:
                        # Writing the remaining users back without changes
                        other_users_in_library = ",".join(info)
                        updatedusers.write(f"{other_users_in_library}\n")
                
                show_updating()
                show_success("Your details updated.")
        
        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")


    def showMenu(self):
        """
        Displays the role-specific menu interface.

        Checks the current session's user role (Admin or Guest) and routes 
        them to the appropriate interactive menu.
        """
        pass

#==========================================================================================================
#                                           CLASS COMMONWORK:
#==========================================================================================================

class CommonWork:
    """
    Manages common library operations shared between Guest and Admin users.
    
    This class handles functionalities that are universally accessible, 
    such as searching for specific books or viewing the library's catalog.
    
    Attributes:
        bookpath (str): File path for the books database.
    """
    def __init__(self):
        """Initializes the CommonWork object with the database path for books."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_folder = os.path.join(base_dir, 'database')
        
        self.bookpath = os.path.join(db_folder, 'books.txt')

        if not os.path.exists(self.bookpath):
            with open(self.bookpath, 'a') as f:
                pass

    def searchBook(self):
        """
        Searches for a specific book in the library database.
        
        Continuously prompts the user for a book name and author. Formats 
        these inputs and checks for an exact string match line-by-line 
        in the books text file. Provides a menu to continue or exit after 
        each search.

        Raises:
            FileNotFoundError: Caught internally if the books database is missing.
        """
        while True:
            get_print("\nPlease enter book name and its author name for search in library.")
            
            # .capitalize() converts only the very first letter of the string to uppercase.
            # Useful for standardizing book titles before formatting them into the search query.
            self.book = get_valid_input('Book Name: ').capitalize()
           
            # .title() converts the first letter of every word to uppercase.
            # Highly effective for standardizing author names (e.g., "john doe" becomes "John Doe").
            self.author = get_valid_input("Author Name: ").title()
            
            # Constructing the exact sentence format expected to exist in the text file database
            # to enable a direct, high-speed string equality check.
            search = f"Book name is '{self.book}' and written by '{self.author}'.\n" 
            
            try:
                match_book = False
                with open(self.bookpath, 'r') as file:
                    booklist = file.readlines()
                    for book in booklist:
                        # Direct string matching against the database row
                        if book == search:
                            show_loading()
                            show_success(f"1 book found.")
                            print("\n")
                            show_description(book)
                            match_book = True # if book details is mathed
                            break
                            
                if match_book == False: # id book details doesn't match
                    show_loading()
                    show_error('Book not found into the library.')

                # Interactive prompt loop to control whether the user wants to search again or leave
                while True:
                    asking_option = {"1": "Continue", "2": "Exit"}
                    print("\n")
                    show_menu_style("CHOICE", asking_option)
                    asking = get_input("Enter your choice: ")
                    if asking == '1':
                        break # Breaks the inner interaction loop, restarting the main search loop
                    elif asking == '2':
                        return # Exits the entire method gracefully
                    else:
                        show_warning("Wrong Input! Please choose exactly 1 or 2.")
                        continue

            except FileNotFoundError:
                show_error('Database file not found! Please check the file path.')
                return # Safe exit if the file is completely missing


    def viewBooks(self):
        """
        Displays all the books currently available in the library database.
        
        Reads the entire book text file, calculates the total number of books, 
        and iterates through the list to display each book's details sequentially 
        with its corresponding index number.

        Raises:
            FileNotFoundError: Caught internally if the books database is missing.
        """
        try:
            with open(self.bookpath, 'r') as file: # reading books.txt data
                booklist = file.readlines() # a variable that stores all books in a list
                
                show_success(f"{len(booklist)} books found.")
                print("\n")
                
                # TRICKY SYNTAX: enumerate()
                # A highly Pythonic built-in function that automatically adds a counter to an iterable.
                # Instead of manually maintaining a counter variable (e.g., i = 0, i += 1), 
                # enumerate dynamically yields both the index ('total') and the value ('book') at the same time.
                for total, book in enumerate(booklist): # extracting all book from the list
                    show_loading_book()
                    
                    # Using .strip() ensures we don't get double newlines if the text file already contains '\n'
                    show_description(f"{total+1}. {book.strip()}")
        
        except FileNotFoundError:
            print("\n")
            show_error('Database file not found! Please check the file path.')


#==========================================================================================================
#                                           CLASS FINECALCULATION:
#==========================================================================================================

class FineCalculation(): 
    """
    Calculates and manages library fines for users based on overdue books.
    and also calculates the total library fine.
    
    This class reads the borrowed books database, parses the stored due dates, 
    compares them with the current real-time date, and calculates the total 
    accumulated fine for a specific user.
    
    Attributes:
        borrowedbook (str): File path for the borrowed books database.
    """

    def __init__(self):
        """Initializes the FineCalculation object with the database path."""
        base_dir = os.path.dirname(os.path.abspath(__file__))
        db_folder = os.path.join(base_dir, 'database')
        
        self.borrowedbook = os.path.join(db_folder, 'borrowedbooks.txt')

        if not os.path.exists(self.borrowedbook):
            with open(self.borrowedbook, 'a') as f:
                pass


    def totalUserFine(self, loginId):  
        """
        Calculates the total pending fine for a specific user's borrowed books.

        Reads the database, filters records belonging to the provided login ID, 
        extracts the due date from the string format, and compares it to today's 
        date. A fine of 20 rupees per day is applied for overdue books.

        Args:
            loginId (str): The unique login ID of the user to check fines for.

        Returns:
            str: A formatted message indicating the total fine amount, 
                 or a status message if there are no dues or borrowed books.

        Raises:
            FileNotFoundError: Caught internally if the database file is missing.
        """
        self.loginId = loginId 
        try:
            with open(self.borrowedbook, "r") as books:
                totalbooklist = books.readlines() 
                booklist = []
                for book in totalbooklist:
                    if book.strip():
                        # TRICKY SYNTAX: eval()
                        # Converting the string representation of a dictionary back into a real dictionary.
                        bookdict = eval(book)
                        booklist.append(bookdict)

                # TRICKY SYNTAX: List Comprehension with Dictionary Key check
                # 'if self.loginId in borrowbook' checks if the user's ID exists as a key in the dictionary.
                borrowed_booksByUser = [borrowbook for borrowbook in booklist if self.loginId in borrowbook] 
                if not borrowed_booksByUser:
                    return "You have not borrowed any book yet."
                    
                total_fine = []
                for book in borrowed_booksByUser: 
                    # TRICKY SYNTAX: Multi-level String Splitting
                    # First split isolates the date part after ' Due Date: '.
                    # Example: "Harry Potter Due Date: 2026-08-10" -> ["Harry Potter", "2026-08-10"]
                    bookdetailsAndDate = book[self.loginId].split(' Due Date: ')
                    
                    # Second split breaks "YYYY-MM-DD" into ["YYYY", "MM", "DD"]
                    extracted_date = bookdetailsAndDate[1].split("-")
                    
                    # Converting extracted string pieces into integers to create a datetime.date object.
                    duedate = datetime.date(int(extracted_date[0]), int(extracted_date[1]), int(extracted_date[2]))
                    currentdate = datetime.date.today()
                    
                    # TRICKY SYNTAX: Date Math (Timedelta)
                    # Subtracting two datetime.date objects returns a 'timedelta' object.
                    # We use .days to get the exact integer difference in days.
                    
                    daysleft = duedate - currentdate
                    
                    if daysleft.days < 0:
                        # TRICKY SYNTAX: Negative Math Conversion
                        # Since 'daysleft' is negative for overdue books (e.g., -5 days),
                        # multiplying by -20 makes the fine a positive number (e.g., -5 * -20 = 100).
                        total_fine.append(-20*daysleft.days)
                
                totalfine = sum(total_fine)
                if totalfine > 0:
                    return f"Your total pending fine is {totalfine} rupees. Please pay to clear your dues."
                else:
                    return "Status: No Dues"
                
        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")
            

    def totalLibraryFine(self):
        """
        Calculates the total pending fine across all users in the library system.

        Reads the entire borrowed books database, extracts all active book records 
        regardless of the user, parses their due dates, and compares them against 
        the current date. Aggregates a 20-rupee per day penalty for all overdue books.

        Returns:
            str: A formatted string displaying the total accumulated fine for the 
                 entire library, or a status message if no fines/books exist.

        Raises:
            FileNotFoundError: Caught internally if the database file is missing.
        """
        try:
            with open(self.borrowedbook, "r") as books:
                totalbooklist = books.readlines()
                booklist = []
                for book in totalbooklist:
                    if book.strip():
                        # TRICKY SYNTAX: eval() to dynamically parse the dictionary
                        bookdict = eval(book)
                        booklist.append(bookdict)

                total_books = []
                if not booklist:
                    return "No book was borrowed from the library."
                
                # TRICKY SYNTAX: .items() dictionary method
                # Since the dictionary structure is { 'loginId': 'book details...' },
                # using .items() allows us to bypass the keys (user IDs) and just 
                # extract all the values (book details) into a flat list.
                for book in booklist:
                    for key, value in book.items():
                        total_books.append(value)

                
                total_fine = []
                for book in total_books:
                    # TRICKY SYNTAX: Multi-level String Splitting
                    bookdetailsAndDate = book.split(' Due Date: ')
                    extracted_date = bookdetailsAndDate[1].split("-")
                    
                    # Converting extracted strings into a real datetime object
                    duedate = datetime.date(int(extracted_date[0]), int(extracted_date[1]), int(extracted_date[2]))
                    currentdate = datetime.date.today()
                    
                    # TRICKY SYNTAX: Date Math (Timedelta)
                    daysleft = duedate - currentdate
                    
                    if daysleft.days < 0:
                        # Multiplying negative overdue days by -20 to get a positive fine amount
                        total_fine.append(-20*daysleft.days)
                
                # Calculating total fine across all users
                totalfine = sum(total_fine)
                if totalfine > 0:
                    return f"Total Fine💰 Pending across all users is {totalfine} rupees."
                else:
                    return "No fine pending."
                
        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")
            return show_error("Error: Database missing.")


#==========================================================================================================
#                                           CLASS ADMIN:
#==========================================================================================================

class Admin(Account, CommonWork): 
    """
    Represents a system administrator in the library system.

    This class inherits from Account and CommonWork, providing admin-specific 
    privileges such as overseeing users, managing the entire book inventory, 
    and accessing system-wide dashboards.
    """
    def __init__(self):
        """
        Initializes the Admin object, inheriting properties from parent classes, 
        and setting up specific file paths for database operations.
        """
        super().__init__()
        self.book = ''
        self.author = ''

    def showMenu(self):
        """
        Displays the interactive menu for the logged-in administrator.

        Returns:
            str: The admin's selected menu option as a string number.
        """
        menuItemOptions = {
                        "1": "View Dashboard",
                        "2": "Manage Books",
                        "3": "Manage Users",
                        "4": "Manage Profile",
                        "5": "Logout"} 
        print("\n")
        show_menu_style("👤  ADMIN MENU", menuItemOptions)
        self.menuItem = get_input("Enter your choice: ")
        return self.menuItem
        

    def adminSignUp(self):
        """
        Registers a new administrator account in the system.

        Calls the parent class signUp method to gather details, then safely 
        appends the new admin's record to the database file with the 'Admin' role tag.
        """
        super().signUp()
        
        try:
            # Safely appending the new admin to the universal user database
            with open(self.userpath, "a") as users:
                users.write(f"Admin,")
                users.write(f"{self.loginId},")
                users.write(f"{self.password},")
                users.write(f"{self.fname},")
                users.write(f"{self.lname},")
                users.write(f"{self.mobile},")
                users.write(f"{self.email}\n")

        except Exception as e:
            show_error(f"An unexpected error occurred during admin registration: {e}")


    def adminSignIn(self) -> bool:
        """
        Authenticates an administrator for system access.

        Verifies credentials against the database and strictly checks the role 
        (must be 'Admin') to prevent unauthorized access by standard users attempting 
        to use the admin portal.

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        super().signIn()
        is_match = False 

        try:
            with open(self.userpath, "r") as users:
                user_details = users.readlines() 
                
                for userid in user_details: 
                    # TRICKY SYNTAX: .strip().split(',')
                    # .strip() is crucial here to remove any hidden newline characters (\n)
                    # before splitting, ensuring accurate string comparison for passwords.
                    details = userid.strip().split(',')
                    
                    # Security Check: Strictly verifying the 'Admin' role
                    if details[0] == "Admin" and details[1] == self.loginId and details[2] == self.loginpassword:
                        self.password = details[2]
                        self.fname = details[2]
                        self.lname = details[4]
                        self.mobile = details[6]
                        self.email = details[6].strip()
                        
                        show_logging()
                        show_success('You Logged in.')
                        is_match = True
                        return True 
            
            if is_match == False:
                show_error('Login id or password incorrect.')
                return False

        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")
            return False
        
        except Exception as e:
            show_error(f"An unexpected error occurred: {e}")
            return False


    def adminDashboard(self):
        """
        Gathers and displays the system-wide dashboard statistics for the admin.

        Calculates the total number of registered users, total books (available + borrowed), 
        available books, and total borrowed books. Integrates the FineCalculation module 
        to display the total pending fine across the entire library system.
        """
        show_loading()
        calc = FineCalculation()
        
        # Block 1: Counting total registered users (Guests only)
        try:
            with open(self.userpath, "r") as users: 
                userslist = users.readlines()

                guest_list = []
                for user_details in userslist:
                    user_details_list = user_details.strip().split(',')

                    # Filtering only standard users, excluding admins from the count
                    if user_details_list[0] == "User":
                        guest_list.append(user_details_list)

                allguestids = []
                for guestid in guest_list:
                    allguestids.append(guestid[1])
        except FileNotFoundError:
            show_error("Users database file not found! Please check the file path.")

        # Block 2: Counting total available books in the library
        try:
            with open(self.bookpath, "r") as availbleBooks:
                booklist = availbleBooks.readlines()

                totalAvailbleBooks = []
                for availbleBook in booklist:
                    # .strip() safely ignores blank lines or trailing newlines
                    if availbleBook.strip():
                        totalAvailbleBooks.append(availbleBook)
        
        except FileNotFoundError:
            show_error("Books database file not found! Please check the file path.")

        # Block 3: Counting total borrowed books
        try:
            with open(self.borrowedbook, "r") as borrowedbooks:
                borrowedbooklist = borrowedbooks.readlines()

                totalborrowedbooks = []
                for borrowedbook in borrowedbooklist:
                    if borrowedbook.strip():
                        totalborrowedbooks.append(borrowedbook)
        
        except FileNotFoundError:
            show_error("Borrowed books database file not found! Please check the file path.")

        # Assembling data for the UI panel
        admin_details = {
            "[+] Total Users": f"{len(allguestids)}",
            "[+] Total Books" : f"{len(totalAvailbleBooks) + len(totalborrowedbooks)}",
            "[+] Available Books": f"{len(totalAvailbleBooks)}",
            "[+] Borrowed Books": f"{len(totalborrowedbooks)}"
        }
        
        print("\n")
        # Displaying the dashboard along with the total library fine across all users
        show_dashboard(self.loginId, admin_details, calc.totalLibraryFine())
        

    def deleteAdminAccount(self):
        """Wrapper method to permanently delete the current admin's account."""
        return super().deleteAccount()
    

    def searchBook(self):
        """Wrapper method to search for a specific book in the library inventory."""
        return super().searchBook()
    

    def viewBooks(self):
        """Wrapper method to display all available books in the library."""
        return super().viewBooks()


    def addBook(self):
        """
        Adds a new book record to the library inventory.

        Prompts the admin for the book's name and author, capitalizes them for 
        consistency, and asks for confirmation. If confirmed, it safely appends 
        the correctly formatted book string to the database. Includes options 
        to continuously add multiple books or exit.

        Raises:
            IOError: Caught internally if there is an issue writing to the file.
        """
        while True:
            print("\n")
            get_print("Please enter book name and its author name for add it in the library.")
            self.book = get_valid_input('Book Name: ').capitalize() 
            self.author = get_valid_input("Author Name: ").title() 
            
            print("\n")
            show_description("Please check the book details before adding it to the library.")
            confirm = get_input("If you want to proceed with these details. type 'Yes' or 'No': ").upper()
            
            if confirm == 'YES':
                try:
                    # Opening the file in append mode ('a') ensures we don't overwrite existing books
                    with open(self.bookpath, 'a') as book:
                        # Combining the string into a single write operation for cleaner File I/O
                        exact_book_string = f"Book name is '{self.book}' and written by '{self.author}'.\n"
                        book.write(exact_book_string)
                        
                        show_adding()
                        show_success("Book added into the library.") 
                        
                        # Interactive prompt to control whether the admin wants to add more books
                        while True:
                            asking_option = {"1": "Continue", "2": "Exit"}
                            print("\n")
                            show_menu_style("CHOICE", asking_option)
                            asking = get_input("Enter your choice: ")
                            
                            if asking == '1':
                                break # Breaks this inner menu loop, restarting the main 'add book' loop at the top
                            elif asking == '2':
                                return # Exits the entire function safely
                            else:
                                show_warning("Wrong Input! Please choose exactly 1 or 2.")
                                continue

                except FileNotFoundError:
                    show_error("Error: Database file not found! Please check the file path.")
                    return
            
            elif confirm == 'NO':
                print("\n")
                while True:
                    ask_for_edit = get_input("Please edit the details if they are incorrect. Type 'Yes' or 'Exit': ").upper()
                    
                    if ask_for_edit == "YES":
                        # Breaking this inner loop automatically sends the flow back to the start of the outer while loop.
                        # This safely replaces the need for a recursive self.addBook() call.
                        break 
                    elif ask_for_edit == "EXIT":
                        return # Exits the function entirely
                    else:
                        show_warning("Wrong Input! Please choose exactly 'Yes' or 'Exit'.")
                        continue

            else:
                show_warning("Wrong Input! Please choose exactly 'Yes' or 'No'.")
                continue


    def removeBook(self):
        """
        Removes a specific book record from the library inventory.

        Prompts the admin for the book's name and author, constructs the exact 
        string format expected in the database, and attempts to remove it from 
        the active list of books. If successful, it overwrites the database file 
        with the updated inventory.

        Raises:
            ValueError: Caught internally if the requested book is not found in the database.
            FileNotFoundError: Caught internally if the database file is missing.
        """
        while True:
            get_print("\nPlease enter book name and its author name to remove it from library.")
            self.book = get_valid_input('Book Name: ').capitalize()
            self.author = get_valid_input("Author Name: ").title()
            
            # Formulating the exact string to match against the text file records
            exact_book_string = f"Book name is '{self.book}' and written by '{self.author}'.\n"
            
            try:
                # Reading the current inventory from the database
                with open(self.bookpath, 'r') as book:
                    allbooks = book.readlines() 
                    
                    # The .remove() method acts as both a deleter and a validator.
                    # If the book is not in the list, Python automatically raises a ValueError.
                    allbooks.remove(exact_book_string) 
                    
                    updated_data = allbooks 

                    # Overwriting the database file with the updated book list
                    with open(self.bookpath, 'w') as book:
                        for book_entry in updated_data:
                            book.write(book_entry) 
                    
                    show_removing()
                    show_success("Book removed from library.") 
                    
                    while True:
                        asking_option = {"1": "Continue", "2": "Exit"}
                        print("\n")
                        show_menu_style("CHOICE", asking_option)
                        asking = get_input("Enter your choice: ")
                        
                        if asking == '1':
                            break # Restarts the main remove process
                        elif asking == '2':
                            return # Safely exits the function entirely
                        else:
                            show_warning("Wrong Input! Please choose exactly 1 or 2.")
                            continue

            except ValueError:
                # Triggered when .remove() fails to find the book in the list
                show_removing()
                show_error("Book details doesn't match.")
                
                while True:
                    asking_option = {"1": "Continue", "2": "Exit"}
                    print("\n")
                    show_menu_style("CHOICE", asking_option)
                    asking = get_input("Enter your choice: ")
                    
                    if asking == '1':
                        break # Allows the admin to try entering the details again
                    elif asking == '2':
                        return
                    else:
                        show_warning("Wrong Input! Please choose exactly 1 or 2.")
                        continue

            except FileNotFoundError:
                show_error("Database file not found! Please check the file path.")
                return

    def viewBorrowed(self):
        """
        Displays a list of all books currently borrowed by any user in the system.

        Reads the borrowed books database, parses the dictionary structures, 
        and extracts the book details (ignoring the user IDs) to show the admin 
        a complete overview of out-of-stock inventory.

        Raises:
            FileNotFoundError: Caught internally if the database file is missing.
        """
        
        try:
            with open(self.borrowedbook, "r") as borrowedbooks:
                books = borrowedbooks.readlines()
                booklist = []
                
                for book in books:
                    if book.strip():
                        bookdict = eval(book)
                        booklist.append(bookdict)

                show_loading()

                if not booklist:
                    show_error("There are no borrowed books in the system.")
                    return
                
                show_success(f"{len(booklist)} books found.\n")
                
                for borrowedbook in booklist:
                    # Extracting just the book details from the dictionary
                    for loginid, bookdetails in borrowedbook.items():
                        show_loading_book()
                        show_description(f"{bookdetails}")
                        
        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")


    def viewUsers(self): 
        """
        Displays a formatted list of all registered standard users (Guests).

        Reads the universal users database and filters out Admin accounts. 
        Crucially, it implements Data Masking by removing the password field 
        before displaying user details, ensuring privacy and security.

        Raises:
            FileNotFoundError: Caught internally if the database file is missing.
        """
        try:
            with open(self.userpath, "r") as users: 
                userslist = users.readlines()
                all_guest = []
                
                for user_details in userslist:
                    filtered_details = user_details.strip().split(',')
                    
                    # Data Masking: Popping index 2 (Password) so the admin cannot see user passwords
                    filtered_details.pop(2)

                    if filtered_details[0] == 'Admin':
                        pass # Skipping admin records

                    else:
                        # Popping index 0 (The 'User' tag) as it is redundant for this list
                        filtered_details.pop(0)
                        all_guest.append(filtered_details)
                
                show_loading()
                if not all_guest:
                    show_description("There are no users registered in the library.")
                    return
                
                show_success(f"{len(all_guest)} guests found.\n")
                
                for guest in all_guest:
                    # Joining the remaining details (ID, Name, Mobile, Email) with a pipe separator
                    show_search_user()
                    show_description(" | ".join(guest))

        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")


    def userSignUp(self):
        """
        Allows the admin to manually register a new standard user.

        Calls the parent class signUp method to gather details, then appends 
        the new user's record to the database with the 'User' role tag.
        Useful for offline registrations or helping users who cannot sign up themselves.
        """
        super().signUp()
        
        try:
            # Opening file in append mode ('a') to safely add the new user
            with open(self.userpath, "a") as users:
                users.write(f"User,")
                users.write(f"{self.loginId},")
                users.write(f"{self.password},")
                users.write(f"{self.fname},")
                users.write(f"{self.lname},")
                users.write(f"{self.mobile},")
                users.write(f"{self.email}\n")
        
        
        except IOError as e:
            # IOError is more appropriate here than FileNotFoundError because 
            # 'a' mode automatically creates the file if it doesn't exist.
            show_error(f"Database error! Unable to save user. (Details: {e})")


    def viewAdminProfile(self):
        """Wrapper method to view the current administrator's profile."""
        return super().viewProfile()
    

    def editAdminProfile(self):
        """Wrapper method to edit the current administrator's profile details."""
        return super().editProfile()


    def deleteUserAccount(self): 
        """
        Allows the admin to permanently delete a standard user's account.

        Prompts for the target user's Login ID and asks for confirmation. 
        It reads the entire universal user database, searches for the exact 
        match with the 'User' role, and excludes them from the updated list. 
        It also provides realistic feedback if the requested ID does not exist.

        Raises:
            FileNotFoundError: Caught internally if the database file is missing.
            Exception: Catches any other unexpected execution errors.
        """
        get_print("\nEnter guest's login ID for delete his/her account.")
        self.guestId = get_valid_input('Login ID: ')
        print("\n")
        
        confirm = get_input("Please confirm if you want to proceed (type 'yes' or 'no): ").upper()
        
        if confirm == "YES":
            try:
                with open(self.userpath, "r") as users: 
                    userslist = users.readlines()

                updated_users_list = []
                user_found = False

                # Single Loop Optimization: Filtering the user in one pass
                for user_details in userslist:
                    if not user_details.strip():
                        continue # Skips any empty lines in the text file
                        
                    user_details_list = user_details.strip().split(',')
                    
                    # If it's a User and the ID matches, we skip appending them (Effectively deleting)
                    if user_details_list[0] == "User" and user_details_list[1] == self.guestId:
                        user_found = True
                    else:
                        # Everyone else (Admins and other Users) gets added to the safe list
                        updated_users_list.append(user_details)

                
                # Writing back to the database only if the user was actually found and removed
                if user_found:
                    with open(self.userpath, "w") as updated_users:
                        for safe_user in updated_users_list:
                            updated_users.write(safe_user) 
                            
                    show_loading()
                    show_success(f"User '{self.guestId}' has been successfully deleted.") 
                else:
                    show_loading()
                    show_error(f"Action Denied! User ID '{self.guestId}' not found in the database.")
                    
            except FileNotFoundError:
                show_error("Database file not found! Please check the file path.") 

            except Exception as e:
                show_error(f"An unexpected error occurred: {e}") 
        
        elif confirm == 'NO':
            show_loading()
            show_success("User deletion cancelled by admin.")
        
        else:
            show_warning("Invalid Input! Please type exactly 'yes' or 'no'.")


#==========================================================================================================
#                                           CLASS USER:
#==========================================================================================================

class User(Account, CommonWork): 
    """
    Represents a standard library guest/user.

    This class inherits from both Account (handling authentication/profile) 
    and CommonWork (handling general library queries). It manages user-specific 
    actions like viewing the dashboard, borrowing/returning books, and managing 
    their profile.
    """
    def __init__(self):
        """
        Initializes the User object, inheriting properties from parent classes, 
        and sets up specific file paths for user operations.
        """
        # TRICKY SYNTAX: super().init()
        # This calls the constructor of the parent class. In Multiple Inheritance, 
        # it follows the Method Resolution Order (MRO) to initialize attributes.
        super().__init__()
        self.book = ''
        self.author = ''


    def showMenu(self): 
        """
        Displays the interactive menu for the logged-in user.

        Returns:
            str: The user's selected menu option as a string number.
        """
        self.menuItem_options = {
                        "1": "View Dashboard",
                        "2": "Explore Books",
                        "3": "My Borrowed Books",
                        "4": "Manage Profile",                      
                        "5": "Logout"}
        print("\n")
        show_menu_style("👤 USER MENU", self.menuItem_options)
        self.menuItem = get_input("Enter your choice: ")
        return self.menuItem
        

    def userSignUp(self):
        """
        Registers a new user in the library system.

        Calls the parent class signUp method to gather details, then safely 
        appends the new user's record to the database file in CSV format. 
        Includes robust error handling for file access issues.
        """
        # Inherited from the Account class to handle inputs and ID generation
        super().signUp()
        
        try:
            # TRICKY SYNTAX: "a" (Append Mode)
            # Unlike "w" which erases the whole file, "a" safely adds new data 
            # to the very end of the file without deleting existing users.
            with open(self.userpath, "a") as users:
                users.write(f"User,")
                users.write(f"{self.loginId},")
                users.write(f"{self.password},")
                users.write(f"{self.fname},")
                users.write(f"{self.lname},")
                users.write(f"{self.mobile},")
                users.write(f"{self.email}\n")

        except PermissionError:
            show_error("Permission denied. Please check if the file is read- only or currently open in another program.")
        except IOError as e:
            show_error(f"IO Error: Unable to write to file. Please verify the file path and disk. (Details: {e})")
        except Exception as e:
            show_error(f"An unexpected error occured: {e}")


    def userSignIn(self) -> bool:
        """
        Authenticates a guest user for system access.

        Calls the parent class signIn method to collect credentials, then 
        verifies them against the database. It strictly checks the role 
        (must be 'User') to prevent cross-role login attempts (e.g., an 
        Admin trying to log in through the User portal).

        Returns:
            bool: True if authentication is successful, False otherwise.
        """
        # Gathers login ID and password inputs via the parent class
        super().signIn()
        
        is_match = False 
        try:
            with open(self.userpath, "r") as users:
                user_details = users.readlines()
                
                for userid in user_details:
                    details = userid.split(',')
                    
                    # Security Check: Ensuring the account type is exactly "User"
                    # before matching the ID and password.
                    if details[0] == "User" and details[1] == self.loginId and details[2] == self.loginpassword:
                        self.password = details[2]
                        self.fname = details[2]
                        self.lname = details[4]
                        self.mobile = details[6]
                        self.email = details[6].strip()
                        
                        show_logging() 
                        show_success('You Logged in.')
                        is_match = True
                        return True 
            
            if is_match == False:
                show_error('Login id or password incorrect.') # Optional: Add a slight delay before showing the error
                return False
            
        except PermissionError:
            show_error("Permission denied. Please check if the file is read- only or currently open in another program.")
            return False
        except IOError as e:
            show_error(f"IO Error: Unable to write to file. Please verify the file path and disk. (Details: {e})")
            return False
        except Exception as e:
            show_error(f"An unexpected error occured: {e}")
            return False


    def Userdashboard(self):
        """
        Gathers and displays the user's personal dashboard statistics.

        Calculates the total number of books currently available in the library 
        and the total number of books borrowed by the current user. It also 
        integrates the FineCalculation module to display any pending dues.

        Returns:
            bool: False only if a critical file operation fails.
        """
        show_loading()
        calc = FineCalculation()
        
        # Block 1: Counting total available books in the library
        try:
            with open(self.bookpath, "r") as availableBooks:
                booklist = availableBooks.readlines()

                totalAvailableBooks = []
                for availableBook in booklist:
                    # .strip() is safer as it handles spaces, tabs, and newlines efficiently
                    if availableBook.strip():
                        totalAvailableBooks.append(availableBook)
        
        except PermissionError:
            show_error("Permission denied. Please check if the file is read- only or currently open in another program.")
            return False
        except IOError as e:
            show_error(f"IO Error: Unable to write to file. Please verify the file path and disk. (Details: {e})")
            return False
        except Exception as e:
            show_error(f"An unexpected error occured: {e}")
            return False

        # Block 2: Counting books borrowed by the specific user
        try:
            with open(self.borrowedbook, "r") as borrowedbooks:
                borrowedbooklist = borrowedbooks.readlines()

                booklist = []
                for book in borrowedbooklist:
                    if book.strip():
                        bookdict = eval(book)
                        booklist.append(bookdict)

                # Filtering only the books that have the current user's login ID as a key
                guestsBorrowedBooks = [books for books in booklist if self.loginId in books]
        
        except PermissionError:
            show_error("Permission denied. Please check if the file is read- only or currently open in another program.")
            return False
        except IOError as e:
            show_error(f"IO Error: Unable to write to file. Please verify the file path and disk. (Details: {e})")
            return False
        except Exception as e:
            show_error(f"An unexpected error occured: {e}")
            return False

        # Assembling data for the UI panel
        user_details = {
                        "[+] Total Available Books in Library": f"{len(totalAvailableBooks)}",
                        "[+] Books Borrowed By You": f"{len(guestsBorrowedBooks)}/5 (Max Limit)"
                        }
        
        print("\n")
        # Passing user details and dynamic fine calculation to the dashboard UI
        show_dashboard(self.loginId, user_details, calc.totalUserFine(self.loginId))


    def viewUserProfile(self):
        """Wrapper method to view the current user's profile."""
        return super().viewProfile()
    

    def editUserProfile(self):
        """Wrapper method to edit the current user's profile details."""
        return super().editProfile()


    def deleteUserAccount(self):
        """Wrapper method to permanently delete the current user's account."""
        return super().deleteAccount()
    

    def searchBook(self):
        """Wrapper method to search for a specific book in the library."""
        return super().searchBook()
    

    def viewBooks(self):
        """Wrapper method to display all available books in the library."""
        return super().viewBooks()
    

    def borrowBook(self):
        """
        Handles the complete book borrowing process for a user.

        Displays borrowing rules, calculates if the user has reached their 
        monthly limit (max 5 books) by reverse-engineering the issue dates 
        from existing borrowed records. If eligible, it prompts for book details, 
        removes the requested book from the available 'books.txt' inventory, 
        and appends the transaction to 'borrowedbooks.txt' with a new 15-day due date.

        Raises:
            ValueError: Caught internally if the requested book is not in the library.
            FileNotFoundError: Caught internally if database files are missing.
            Exception: Catches any other unexpected execution errors.
        """
        print("\n")
        show_heading("--- Important Borrowing Rules ---")
        get_print("1. You can borrow a maximum of 5 books per month. Once you reach this limit, you will be able to borrow again when your limit renews next month.")
        get_print("2. You must return the book within 15 days.")
        get_print("3. A fine of 20 rupees per day will be charged after the due date.\n")
        
        while True:
            try:
                # ---------------------------------------------------------
                # Phase 1: Checking User's Monthly Borrowing Limit
                # ---------------------------------------------------------
                # Reading the user's borrowed books data from the file and storing in a variable
                # then calculating the month and year when he want to borrow a book.
                with open(self.borrowedbook, "r") as books:
                    totalbooklist = books.readlines()
                    booklist = [] 
                    for book in totalbooklist:
                        if book.strip():
                            bookdict = eval(book)
                            booklist.append(bookdict)

                    current_month = datetime.datetime.now().month
                    current_year = datetime.datetime.now().year
                    books_borrowed_this_month = 0

                    for borrowbook in booklist:
                        if self.loginId in borrowbook: 
                            bookdetailsAndDate = borrowbook[self.loginId].split(' Due Date: ')
                            extracted_date = bookdetailsAndDate[1].split("-")
                            
                            duedate = datetime.date(int(extracted_date[0]), int(extracted_date[1]), int(extracted_date[2]))
                            
                            # TRICKY SYNTAX: Reverse-Engineering Dates
                            # Since only the due date is saved, we subtract 15 days using 
                            # timedelta to figure out the exact date the book was issued.
                            issue_date_obj = duedate - datetime.timedelta(days = 15)
                            
                            if issue_date_obj.month == current_month and issue_date_obj.year == current_year:
                                books_borrowed_this_month += 1

                    # ---------------------------------------------------------
                    # Phase 2: Borrowing Process & Database Updates
                    # ---------------------------------------------------------
                    # Giving permission to user for borrow a book
                    # Reading library's books.txt file and checking for book details that is provided
                    # by user. and then updating the borrowed books data also updating books.txt file's data
                    if books_borrowed_this_month < 5:
                        while True:
                            confirm = get_input("For proceed please type ('Yes' or 'No'): ").upper()
                            get_print("\nEnter the name of the book and its author that you want to borrow.")
                            
                            if confirm == 'YES':
                                self.bookname = get_valid_input("Book name: ").capitalize()
                                self.authorname = get_valid_input("Author name: ").title()
                                
                                # Generating a new due date (Today + 15 days)
                                self.dueDate = datetime.date.today() + datetime.timedelta(days = 15)

                                try:
                                    # CORE DATABASE LOGIC: Move from 'Available' to 'Borrowed'
                                    with open(self.bookpath, 'r') as book:
                                        allbooks = book.readlines()
                                        
                                        # TRICKY SYNTAX: .remove() as a Validator
                                        # This directly tries to find and remove the exact string. 
                                        # If the book doesn't exist, Python instantly throws a ValueError!
                                        exact_book_string = f"Book name is '{self.bookname}' and written by '{self.authorname}'.\n"
                                        allbooks.remove(exact_book_string)
                                        
                                        updated_books = allbooks
                                    
                                        # Overwriting books.txt to deduct the inventory
                                        with open(self.bookpath, 'w') as upadted_booklist: 
                                            for book in updated_books:
                                                upadted_booklist.write(book)

                                        # TRICKY SYNTAX: String escaping for JSON-like format
                                        # Using {{ and }} to safely inject literal curly braces for the dictionary string format.
                                        with open(self.borrowedbook, 'a') as borrowed_booklist:
                                            borrowed_booklist.write(f"{{\"{self.loginId}\":\"Book name is '{self.bookname}' and written by '{self.authorname}'. Due Date: {self.dueDate}\"}}\n")
                                        
                                        show_loading()
                                        show_success(f"You have borrowed '{self.bookname}'.")
                                        show_description(f"📌Please note your Due Date: {self.dueDate}")
                                        return # Successfully borrowed, exit function


                                except ValueError:
                                    # Caught if .remove() fails (Book not found)
                                    show_error("Book details don't match or the book is currently unavailable.")
                                    
                                    while True:
                                        asking_option = {"1": "Continue", "2": "Exit"}
                                        print("\n")
                                        show_menu_style("CHOICE", asking_option)
                                        asking = get_input("Enter your choice: ")
                                        if asking == '1':
                                            break  # Breaks inner loop to ask for book details again
                                        elif asking == '2':
                                            return # Exits entirely
                                        else:
                                            show_warning("Wrong Input! Please choose exactly 1 or 2.")
                                            continue

                            elif confirm == 'NO':
                                show_loading()
                                show_success("Book borrowed cancelled by user.")
                                return
                            break
                    else:
                        show_warning(f"Limit Reached! You have already borrowed {books_borrowed_this_month} books this month.")
                        show_warning("Please borrow again next month.")
                        return # Exit if limit reached
            
            except FileNotFoundError:
                show_error("Database file not found! Please check the file path.")
                return

            except Exception as e:
                show_error(f"An unexpected error occured: {e}")
                return
    

    def returnBook(self):
        """
        Handles the return process for a borrowed book and manages fine collection.

        Prompts the user for book details, searches their borrowed records, 
        and calculates if the book is overdue. If overdue, it enforces fine 
        payment before accepting the return. Once validated, it removes the 
        book from the user's borrowed list and adds it back to the main library inventory.

        Raises:
            FileNotFoundError: Caught internally if database files are missing.
            Exception: Catches any other unexpected execution errors.
        """
        while True:
            get_print("\nEnter the name of the book and its author that you want to return.")
            self.bookname = get_valid_input("Book name: ").capitalize()
            self.authorname = get_valid_input("Author name: ").title()
            
            try:
                # Reading the borrowed books database to find the user's records
                # then calculating the month and year when he want to borrow a book.
                with open(self.borrowedbook, "r") as books:
                    totalbooklist = books.readlines()
                    booklist = [] 
                    for book in totalbooklist:
                        if book.strip():
                            bookdict = eval(book) 
                            booklist.append(bookdict)

                    match_book = False
                    for borrowbook in booklist:
                        if self.loginId in borrowbook: 
                            bookdetailsAndDate = borrowbook[self.loginId].split(' Due Date: ')
                            
                            # Formatting the exact string to match database records consistently
                            exact_book_string = f"Book name is '{self.bookname}' and written by '{self.authorname}'."
                            
                            if self.loginId in borrowbook and bookdetailsAndDate[0] == exact_book_string:
                                show_description(f"\n{bookdetailsAndDate[0]}")
                                
                                # Extracting and converting the date to a datetime.date object
                                extracted_date = bookdetailsAndDate[1].split("-")
                                duedate = datetime.date(int(extracted_date[0]), int(extracted_date[1]), int(extracted_date[2]))
                                currentdate = datetime.date.today()
                                daysleft = duedate - currentdate
                            
                                if duedate >= currentdate:
                                    # Book is being returned on or before the due date (Safe period)
                                    show_description(f"{daysleft.days} Days Left.")
                                    show_description('No Fine Till Now.\n')
                                    
                                    while True:
                                        confirm = get_input("If you want to return this books please type 'yes'): ").upper()
                                        if confirm == "YES":
                                            # Removing the specific dictionary record from the memory list
                                            booklist.remove(borrowbook)
                                            
                                            # Overwriting the borrowed books database with the updated list
                                            with open(self.borrowedbook, "w") as updatedBorrowedbooks:
                                                for allborrowbook in booklist:
                                                    updatedBorrowedbooks.write(f"{str(allborrowbook)}\n")

                                            # Adding the book back to the main library inventory (Append mode)
                                            with open(self.bookpath, 'a') as booklist: 
                                                booklist.write(f"Book name is '{self.bookname}' and written by '{self.authorname}'.\n")
                                            
                                            show_loading()
                                            show_success("Book returned to library.\n")
                                            return

                                        elif confirm == 'NO':
                                            show_loading()
                                            show_success("Book return cancelled by user.\n")
                                            break

                                        else:
                                            show_warning("Invalid Input! Please type exactly 'yes' or 'no'.\n")

                                # Book is overdue, fine calculation and payment process initiated
                                else:
                                    df = currentdate - duedate
                                    total_fine = 20 * df.days
                                    show_warning(f"{df.days} Days Overdue !")
                                    show_warning(f"Fine till now : {total_fine} Rupees.\n")
                                    
                                    while True:
                                        try:
                                            payment = get_valid_payment("If you want to return this books please make payment(Enter Amount): ")
                                            if payment == total_fine:
                                                # Payment successful, process the return logic
                                                booklist.remove(borrowbook)
                                                
                                                with open(self.borrowedbook, "w") as updatedBorrowedbooks:
                                                    for allborrowbook in booklist:
                                                        updatedBorrowedbooks.write(f"{str(allborrowbook)}\n")

                                                with open(self.bookpath, 'a') as booklist:
                                                    booklist.write(f"Book name is '{self.bookname}' and written by '{self.authorname}'.\n")
                                                
                                                show_loading() 
                                                show_success("Book returned to library.")
                                                match_book = True
                                                return
                                            
                                            else:
                                                # Added a check if the user pays the wrong amount
                                                show_error(f"Incorrect amount! Please pay exactly {total_fine} rupees.")

                                        except ValueError:
                                            show_error("Invalid Input! Please enter numbers only.")

                                match_book = True
                                break # Exits the main for-loop once the specific book is found and processed

                    # If the loop finishes and the book was never found
                    if match_book == False:
                        show_error("You haven't borrowed this book, or the book details are incorrect")
                        while True:
                            asking_option = {"1": "Continue", "2": "Exit"}
                            print("\n")
                            show_menu_style("CHOICE", asking_option)
                            asking = get_input("Enter your choice: ")
                            if asking == '1':
                                break # Restarts the main book return process
                            elif asking == '2':
                                return
                            else:
                                show_warning("Invalid Input! Please choose exactly 1 or 2.")
                                continue

            except FileNotFoundError:
                show_error('Database file not found! Please check the file path.')

            except Exception as e:
                show_error(f"An unexpected error occured: {e}")


    def returnAllBooks(self):
        """
        Handles the bulk return process for all books borrowed by the user.

        Requires re-authentication for security. It calculates the total fine 
        across all overdue books. If fines exist, it forces payment before 
        processing. Once cleared, it removes all associated records from the 
        borrowed database and efficiently appends them back to the library inventory.

        Raises:
            FileNotFoundError: Caught internally if database files are missing.
            Exception: Catches any other unexpected execution errors.
        """
        get_print("\nPlease enter your login ID and password to return all your borrowed books.")
        
        self.varifiedId = get_valid_input("Login ID: ")
        self.varifiedPassword = console.input("[bold cyan]👉 Password: [/bold cyan]")
        print("\n")
        
        if hasattr(self, 'loginpassword'):
            current_user_password = self.loginpassword
        else:
            current_user_password = self.password
        
        if self.varifiedId == self.loginId and self.varifiedPassword == current_user_password:
            while True:
                ask = get_input("Please confirm if you want to proceed (type 'yes' or 'no'): ").upper()
                
                if ask == 'YES':
                    try:
                        with open(self.borrowedbook, "r") as books:
                            totalbooklist = books.readlines()
                            booklist = []
                            for book in totalbooklist:
                                if book.strip():
                                    bookdict = eval(book)
                                    booklist.append(bookdict)

                            # TRICKY SYNTAX: Advanced List Comprehensions
                            # Separating the entire database into two distinct lists in just 2 lines:
                            # 1. Books belonging to other users (to be saved back).
                            # 2. Books belonging to the current user (to be processed for return).
                            updated_borrowed_booklist = [borrowbook for borrowbook in booklist if self.loginId not in borrowbook]
                            borrowed_booksByUser = [borrowbook for borrowbook in booklist if self.loginId in borrowbook]
                            
                            if not borrowed_booksByUser:
                                show_error("You do not have any books to return.")
                                return

                            total_fine = []
                            for book in borrowed_booksByUser:
                                bookdetailsAndDate = book[self.loginId].split(' Due Date: ')
                                extracted_date = bookdetailsAndDate[1].split("-")
                                duedate = datetime.date(int(extracted_date[0]), int(extracted_date[1]), int(extracted_date[2]))
                                currentdate = datetime.date.today()
                                daysleft = duedate - currentdate
                                
                                if daysleft.days < 0:
                                    total_fine.append(-20*daysleft.days)
                            
                            totalfine = sum(total_fine)
                            caculating_fine()
                            show_warning(f"Your total fine: {totalfine} Rupees.")

                            if totalfine > 0:
                                while True:
                                    try:
                                        print("\n")
                                        payment = get_valid_payment("If you want to return all books, please pay your total fine: ")
                                        if payment == totalfine:
                                            # Rewriting borrowed books file excluding this user's books
                                            with open(self.borrowedbook, "w") as updatedBorrowedbooks:
                                                for allborrowbook in updated_borrowed_booklist:
                                                    updatedBorrowedbooks.write(f"{(allborrowbook)}\n")

                                            returned_booklist = [returnbook for returnbook in booklist if f"{self.loginId}" in returnbook]
                                            
                                            # Appending user's books back to the main library inventory
                                            with open(self.bookpath, 'a') as returned_books:
                                                for book in returned_booklist:
                                                    bookdetailsAndDate = book[self.loginId].split(' Due Date: ')  
                                                    returned_books.write(f"{bookdetailsAndDate[0]}\n")

                                            show_loading()      
                                            show_success("All Books returned to library.")
                                            
                                            return
                                        
                                        else:
                                            show_error(f"Incorrect amount! Please pay exactly {totalfine} rupees.")

                                    except ValueError:
                                        show_error("Invalid Input! Please enter numbers only.")

                            else:
                                while True:
                                    print("\n")
                                    confirm = get_input("If you want to return these books please type 'Yes' or 'No'): ").upper()
                                    
                                    if confirm == "YES":
                                        with open(self.borrowedbook, "w") as updatedBorrowedbooks:
                                            for allborrowbook in updated_borrowed_booklist:
                                                updatedBorrowedbooks.write(f"{(allborrowbook)}\n")

                                        returned_booklist = [returnbook for returnbook in booklist if f"{self.loginId}" in returnbook]
                                        with open(self.bookpath, 'a') as returned_books:
                                            for book in returned_booklist:
                                                bookdetailsAndDate = book[self.loginId].split(' Due Date: ')
                                                returned_books.write(f"{bookdetailsAndDate[0]}\n")

                                        show_loading() 
                                        show_success("All Books returned to library.")
                                        return

                                    elif confirm == 'NO':
                                        show_loading()
                                        show_success("Book return cancelled by user.")
                                        return

                                    else:
                                        show_warning("Invalid Input! Please type exactly 'yes' or 'no'.")

                    except FileNotFoundError:
                        show_error('Database file not found! Please check the file path.')
                        return

                    except Exception as e:
                        show_error(f"An unexpected error occured: {e}")
                        return

                elif ask == 'NO':
                    show_loading()
                    show_success("Book return cancelled by user.")
                    return

                else:
                    show_warning("Invalid Input! Please type exactly 'yes' or 'no'.")
                    
        else:
            show_loading()
            show_error("Login ID or Password doesn't match.")


    def viewBorrowedList(self):
        """
        Displays a detailed list of all books currently borrowed by the user.

        Reads the borrowed books database and filters records matching the 
        user's login ID. For each borrowed book, it parses the due date, 
        calculates the remaining days, and displays either the days left 
        or the overdue fine (20 rupees/day) if the due date has passed.

        Raises:
            FileNotFoundError: Caught internally if the database file is missing.
            Exception: Catches any other unexpected errors during execution.
        """
        show_loading()
        
        try:
            with open(self.borrowedbook, "r") as books:
                borrowBooklist = books.readlines() 
                has_borrowed = False
                print("\n")

                for bBooks in borrowBooklist:
                    # TRICKY SYNTAX: .strip() check before eval()
                    # This prevents the program from crashing if there is an empty 
                    # newline ('\n') at the end of the text file.
                    if bBooks.strip():
                        # Converting the string dictionary back to a real Python dictionary
                        userBorrowedBooks = eval(bBooks) 
                        
                        if self.loginId in userBorrowedBooks:
                            has_borrowed = True
                            
                            # Printing the book details
                            get_print(f"📕 {userBorrowedBooks[self.loginId]}") 
                            
                            # TRICKY SYNTAX: Multi-level Splitting for Dates
                            # Splitting to isolate the date string: "2026-08-10"
                            booksdetailsAndDate = userBorrowedBooks[self.loginId].split(' Due Date: ')
                            
                            # Splitting by "-" to get Year, Month, and Day separately
                            extracted_date = booksdetailsAndDate[1].split("-")
                            
                            duedate = datetime.date(int(extracted_date[0]), int(extracted_date[1]), int(extracted_date[2]))
                            current_date = datetime.date.today()
                            
                            # Calculating the difference between dates (returns a timedelta object)
                            daysleft = duedate - current_date

                            if duedate >= current_date:
                                # User is within the safe period
                                show_normal(f"{daysleft.days} Days Left !")
                                show_normal('No Fine till now.\n')

                            # TRICKY SYNTAX: Overdue Math
                            # If overdue, subtracting duedate from current_date gives positive days
                            else:
                                df = current_date - duedate
                                show_warning(f"{df.days} Days Overdue !")
                                show_warning(f"Total Fine till now : {20*df.days} Rupees\n")

                if has_borrowed == False: 
                    show_error("You didn't borrow a book yet.")
        
        except FileNotFoundError:
            show_error("Database file not found! Please check the file path.")

        except Exception as e:
                show_error(f"An unexpected error occured: {e}")


# ==========================================================================================================
#                                    SYSTEM ENTRY POINT (THE IGNITION SWITCH)
# ==========================================================================================================
"""
The block below ensures that the Library Management System only runs when this 
script is executed directly, and not when it is imported as a module in another file. 
It instantiates the main Library object, which in turn triggers the entire application workflow.
"""

if __name__ == "__main__":
    # Starting the Main Engine of Lokendra's Library System
    lx = Library()