# Phonebook Application

The Phonebook Application is a simple command-line program that allows users to manage their contacts. Users can add new contacts, search for existing contacts, update contact information, and delete contacts. The application uses a SQLite database to store contact information.


## Features
- **Show all contacts**: display a detailed list of all contacts stored in the phonebook in alphabetical order.  
- **Add a Contact**: add a new contact to the phonebook by providing the name, phone number, address, email and birthday.  
- **Search for a Contact**: search for a contact by typing its full name (or some of its letters) and display all details.
- **Update a Contact**: update the information of an existing contact.
- **Delete a Contact**: delete a contact from the phonebook.


## Requirements
- **Python** (version 3.6 or higher)
- **SQLite3** (version 3.37.2)
- **Prettytable** (version 3.7.0)


## Installation
1. Clone the repository to your local machine.
    ```
    git clone git@github.com:Sir-Jude/phonebook.git
    ```
2. Make sure you have Python installed.
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
6. Follow the on-screen instructions to navigate through the menu.
7. To exit the application, type "x".


## Database
The application uses a SQLite database to store contact information. The database file is named '**phone.db**' and is automatically created if it does not exist. The '**phonebook**' table is used to store the contact records, including fields such as '**ContactID**', '**Name**', '**Phone_number**', '**Address**', '**Email**', and '**Birthday**'. The table is created automatically if it does not exist.  

## License
This project is licensed under the **MIT License**.

Feel free to modify and use this code according to your needs. Contributions and suggestions are welcome!


## Contact
If you have any questions or suggestions, please feel free to reach out to me.
Happy managing your contacts!