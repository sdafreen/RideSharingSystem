from config.db import cursor, conn

def register():
    name = input("Enter Name: ")
    phone = input("Enter Phone: ")
    password = input("Enter Password: ")

    cursor.execute(
        "INSERT INTO Riders (Name, Phone, Password) VALUES (?, ?, ?)",
        (name, phone, password)
    )

    conn.commit()

    print("Rider Registered Successfully!")

def login():
    phone = input("Enter Phone: ")
    password = input("Enter Password: ")

    cursor.execute(
        "SELECT RiderID, Name FROM Riders WHERE Phone=? AND Password=?",
        (phone, password)
    )

    user = cursor.fetchone()

    if user:
        print(f"\nWelcome {user.Name}!")
        return user.RiderID
    else:
        print("Invalid Phone or Password!")
        return None