from os import system
import sqlite3
from prettytable import PrettyTable


class Menu:
    def __init__(self, database, table) -> None:
        self.database = database
        self.table = table

    def create_table(self, conn):
        query = f"""CREATE TABLE IF NOT EXISTS {self.table} (
            ContactID INTEGER PRIMARY KEY AUTOINCREMENT,
            Name VARCHAR(255),
            Email VARCHAR(255),
            Phone_number VARCHAR(255),
            Birthday DATE
        );"""
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    
    def show_contacts(self, conn):
        query = f"""SELECT * from {self.table};"""
        cur = conn.cursor()
        cur.execute(query)
        result = cur.fetchall()

        f_table = PrettyTable(
            [
                "ContactID",
                "Name",
                "Email",
                "Phone_number",
                "Birthday"
            ]
        )
        f_table.add_rows(result)
        return f_table

    def add_one(self, conn, *args):
        query = f"""INSERT INTO {self.table} (
            Name,
            Email,
            Phone_number,
            Birthday
        )
            VALUES (?, ?, ?, ?);"""
        cur = conn.cursor()
        cur.execute(query, args)
        conn.commit()
        print()
        print(f"{args[0]} has been sucessfully added to your phonebook.\n{self.search_contact(conn, args[0])}")

    def search_contact(self, conn, name: str):
        query = f"""SELECT ContactID, Name, Email, Phone_number, Birthday FROM {self.table} WHERE name=?;"""
        cur = conn.cursor()
        cur.execute(query, (name,))
        result = cur.fetchone()
        
        f_table = PrettyTable(
            [
                "ContactID",
                "Name",
                "Email",
                "Phone_number",
                "Birthday"
            ]
        )
        try:
            f_table.add_rows([result])
            return f_table
        except:
            return "Contact not found."
    
    def search_id(self, conn, id: int):
        query = f"""SELECT ContactID, Name, Email, Phone_number, Birthday FROM {self.table} WHERE ContactID=?;"""
        cur = conn.cursor()
        cur.execute(query, (id,))
        result = cur.fetchone()
        
        f_table = PrettyTable(
            [
                "ContactID",
                "Name",
                "Email",
                "Phone_number",
                "Birthday"
            ]
        )
        try:
            f_table.add_rows([result])
            return f_table
        except:
            return "Contact not found."

    def update_contact(self, conn, **fields):
        query = f"""UPDATE {self.table} SET
            Name=?,
            Email=?,
            Phone_number=?,
            Birthday=?
            WHERE ContactID=?;"""

        values = (
            fields["name"],
            fields["email"],
            fields["phone_number"],
            fields["birthday"],
            fields["contactid"],
        )

        cur = conn.cursor()
        try:
            cur.execute(query, values)
            conn.commit()
        except:
            print("Error occurred.")

    def delete_contact(self, conn, id: int):
        query = f"""DELETE FROM {self.table} WHERE ContactID=?;"""
        cur = conn.cursor()
        try:
            cur.execute(query, (id,))
            conn.commit()
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
"""
Please choose an option:
[1] - show contacts
[2] - add a contact
[3] - search a contact
[4] - update a contact
[5] - delete a contact
[x] - Exit
""")
            print()

            # [1] - show contacts
            if option == "1":
                print(menu.show_contacts(conn))
                
            # [2] - add a contact
            elif option == "2":
                name = input("Name? ").title()
                email = input("Email? ")
                phone_number = input("Phone number? ")
                birthday = input("Birthday (YYYY-MM-DD)? ")

                menu.add_one(conn, name, email, phone_number, birthday)
            
            # [3] - search a contact
            elif option == "3":
                name=input("Name? ")
                print()
                print(menu.search_contact(conn, name.title()))

            # [4] - update a contact
            elif option == "4":
                try:
                    searched = int(input("ContactID to be updated? "))
                    if menu.search_id(conn, searched) != "Contact not found.":
                        menu.update_contact(
                            conn,
                            name=input("New name? ").title(),
                            email=input("New email? "),
                            phone_number=input("New phone number? "),
                            birthday=input("New birthday (YYYY-MM-DD)? "),
                            contactid=searched,
                        )
                        print()
                        print("Contact successfully updated.")
                        print(menu.show_contacts(conn))
                    else:
                        print("Contact not found.")
                except ValueError:
                        print("Only numbers (0-9) are allowed.")
                
            # [5] - delete a contact
            elif option == "5":
                try:
                    searched = int(input("ContactID to be deleted? "))
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
