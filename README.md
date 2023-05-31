# Phonebook Application

The Phonebook Application is a simple command-line program that allows users to manage their contacts. Users can add new contacts, search for existing contacts, update contact information, and delete contacts. The application uses a SQLite database to store contact information.

## Installation
1. Clone the repository to your local machine.
2. Make sure you have Python installed (version 3.6 or higher).
3. Install the required dependencies by running the following command:  
    ```
    pip install prettytable
    ```

## Usage
To run the Phonebook Application, follow these steps:
1. Open a terminal or command prompt.
2. Navigate to the directory where you cloned the repository.
3. Run the following command to start the application:
    ```
    python phonebook.py
    ```
4. Once the application starts, you will see a menu with different options.
5. Choose an option by entering the corresponding number and pressing Enter.
6. Follow the prompts to perform various operations such as adding a contact, searching for a contact, updating contact information, or deleting a contact.
7. To exit the application, choose the "x" option from the menu.

## Features
- **Show Contacts**: View all contacts stored in the phonebook.  
- **Add a Contact**: Add a new contact to the phonebook by providing the name, email, phone number, and birthday.  
- **Search a Contact**: Search for a contact by name and display their information.
- **Update a Contact**: Update the information of an existing contact by providing the contact ID and the new details.
- **Delete a Contact**: Delete a contact from the phonebook by providing the contact ID.

## Database
The application uses a SQLite database to store contact information. The database file is named '**phone.db**' and is automatically created if it does not exist. The '**phonebook**' table is used to store the contact records, including fields such as '**ContactID**', '**Name**', '**Phone_number**', '**Address**', '**Email**', and '**Birthday**'. The table is created automatically if it does not exist.  

---
Feel free to modify this README file as per your requirements. You can provide additional instructions, documentation, or screenshots to make it more comprehensive and user-friendly.