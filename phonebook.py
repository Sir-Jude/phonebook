from os import system
import sqlite3
from prettytable import PrettyTable


class Menu:
    def __init__(self, database: str, table: str) -> None:
        """
        Instantiate the Menu object.

        Args:
            database (_type_): _description_
            table (_type_): _description_
        """
        self.database = database
        self.table = table

    def create_table(self, conn: sqlite3.Connection) -> None:
        """
        Create the table in the database if it doesn't exist.

        Args:
            : sqlite3.Connection (sqlite3.Connection): The SQLite connection object.
        """
        query = f"""CREATE TABLE IF NOT EXISTS {self.table} (
            ContactID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(50),
            Phone_number VARCHAR(50),
            Address VARCHAR(100),
            Email VARCHAR(50),
            Birthday DATE
        );"""
        cur = conn.cursor()
        cur.execute(query)

    def show_contacts(self, conn: sqlite3.Connection) -> PrettyTable:
        """
        Retrieve all contacts from the database and display them in a table.

        Args:
            conn (sqlite3.Connection): The SQLite connection object.

        Returns:
            PrettyTable: The table containing all contacts.
        """
        query = f"""SELECT *
                    FROM {self.table}
                    ORDER BY Name;"""
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        f_table = PrettyTable(
            [
                "ContactID",
                "Name",
                "Phone number",
                "Address",
                "Email",
                "Birthday"
            ]
        )
        f_table.add_rows(result)
        return f_table

    def add_one(self, conn: sqlite3.Connection, *args: str) -> None:
        """
        Add a new contact to the database.

        Args:
            conn (sqlite3.Connection): The SQLite connection object.
            args: The contact details (name, phone number, address, email, birthday).
        """
        query = f"""INSERT INTO {self.table} (
            Name,
            Phone_number,
            Address,
            Email,
            Birthday
        )
            VALUES (?, ?, ?, ?, ?);"""
        cur = conn.cursor()
        cur.execute(query, args)
        print()
        print(
            f"{args[0]} has been sucessfully added to your phonebook.\n{self.search_contact(conn, args[0])}"
        )

    def search_contact(self, conn: sqlite3.Connection, name: str) -> PrettyTable:
        """
        Search for a contact in the database by name.

        Args:
            conn (sqlite3.Connection): The SQLite connection object.
            name (str): The name of the contact to search for.

        Returns:
            PrettyTable or str: The table containing the contact details if found, or "Contact not found." if not found.
        """
        query = f"""SELECT ContactID, Name, Phone_number, Address, Email, Birthday 
            FROM {self.table}
            WHERE name LIKE ?
            ORDER BY Name;"""
        cur = conn.cursor()
        cur.execute(query, (f"%{name}%",))
        result = cur.fetchall()

        f_table = PrettyTable(
            [
                "ContactID",
                "Name",
                "Phone number",
                "Address",
                "Email",
                "Birthday"
            ]
        )
        if result:
            f_table.add_rows(result)
            return f_table
        return "Contact not found."

    def search_id(self, conn: sqlite3.Connection, id: int) -> PrettyTable:
        """
        Search for a contact in the database by ContactID.

        Args:
            conn (sqlite3.Connection): The SQLite connection object.
            id (int): The ContactID of the contact to search for.

        Returns:
            PrettyTable or str: The table containing the contact details if found, or "Contact not found." if not found.
        """
        query = f"""SELECT ContactID, Name, Phone_number, Address, Email, Birthday
                    FROM {self.table}
                    WHERE ContactID=?;"""
        cur = conn.cursor()
        cur.execute(query, (id,))
        result = cur.fetchone()

        f_table = PrettyTable(
            [
                "ContactID",
                "Name",
                "Phone number",
                "Address",
                "Email",
                "Birthday"
            ]
        )
        try:
            f_table.add_rows([result])
            return f_table
        except:
            return "Contact not found."

    def update_contact(self, conn: sqlite3.Connection, **kwargs) -> None:
        """
        Update a contact in the database.

        Args:
            conn (sqlite3.Connection): The SQLite connection object.
            fields (dict): The fields to update (name, phone_number, address, email, birthday, contactid).
        """
        query = f"""UPDATE {self.table}
            SET
                Name=CASE WHEN ? = '' THEN Name ELSE ? END,
                Phone_number=CASE WHEN ? = '' THEN Phone_number ELSE ? END,
                Address=CASE WHEN ? = '' THEN Address ELSE ? END,
                Email=CASE WHEN ? = '' THEN Email ELSE ? END,
                Birthday=CASE WHEN ? = '' THEN Birthday ELSE ? END
            WHERE ContactID=?;"""

        values = (
            kwargs.get("name", ""),
            kwargs.get("name", ""),
            kwargs.get("phone_number", ""),
            kwargs.get("phone_number", ""),
            kwargs.get("address", ""),
            kwargs.get("address", ""),
            kwargs.get("email", ""),
            kwargs.get("email", ""),
            kwargs.get("birthday", ""),
            kwargs.get("birthday", ""),
            kwargs.get("contactid", ""),
        )

        cur = conn.cursor()
        try:
            cur.execute(query, values)

        except:
            print("Error occurred.")

    def delete_contact(self, conn: sqlite3.Connection, id: int) -> None:
        """
        Delete a contact from the database.

        Args:
            conn (sqlite3.Connection): The SQLite connection object.
            id (int): The ContactID of the contact to delete.

        Returns:
            str: A message indicating the success of the operation.
        """
        query = f"""DELETE FROM {self.table} WHERE ContactID=?;"""
        cur = conn.cursor()
        try:
            cur.execute(query, (id,))

            return "Contact successfully deleted."
        except:
            print("Error occurred.")


def main():
    menu = Menu("phone.db", "phonebook")
    option = ""
    with sqlite3.connect(menu.database) as conn:
        menu.create_table(conn)

        while option != "x":
            system("clear")
            option = input(
                """Please select an option:
                           
[1] - show all the contacts
[2] - add a contact
[3] - search a contact
[4] - update a contact
[5] - delete a contact
[x] - Exit

Selected option: """
            )
            print()

            # [1] - show contacts
            if option == "1":
                print(menu.show_contacts(conn))

            # [2] - add a contact
            elif option == "2":
                name = input("Name? ").title()
                phone_number = input("Phone number? ")
                address = input("Address? ")
                email = input("Email? ")
                birthday = input("Birthday (YYYY-MM-DD)? ")

                menu.add_one(conn, name, phone_number, address, email, birthday)

            # [3] - search a contact
            elif option == "3":
                name = input("Name of the contact? ")
                print()
                print(menu.search_contact(conn, name.title()))

            # [4] - update a contact
            elif option == "4":
                try:
                    searched = int(input("ID of the contact to be updated? "))
                    if menu.search_id(conn, searched) != "Contact not found.":
                        print(menu.search_id(conn, searched))
                        menu.update_contact(
                            conn,
                            name=input("New name? ").title(),
                            phone_number=input("New phone number? "),
                            address=input("New address? "),
                            email=input("New email? "),
                            birthday=input("New birthday (YYYY-MM-DD)? "),
                            contactid=searched,
                        )
                        print()
                        print("Contact successfully updated.")
                        print(menu.search_id(conn, searched))
                    else:
                        print("Contact not found.")
                except ValueError:
                    print("Only numbers (0-9) are allowed.")

            # [5] - delete a contact
            elif option == "5":
                try:
                    searched = int(input("ID of the contact to be deleted? "))
                    if menu.search_id(conn, searched) != "Contact not found.":
                        print(menu.delete_contact(conn, id=searched))
                    else:
                        print("Contact not found.")
                except ValueError:
                    print("Only numbers (0-9) are allowed.")

            if option != "x":
                print()
                input("Press Enter to continue...")
                continue
            else:
                print("Have a nice day!")


if __name__ == "__main__":
    main()
