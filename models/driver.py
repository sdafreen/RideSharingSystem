from config.db import cursor, conn

def driver_register():
    name = input("Enter Driver Name: ")
    phone = input("Enter Phone: ")
    vehicle = input("Enter Vehicle: ")
    password = input("Enter Password: ")

    cursor.execute(
        """
        INSERT INTO Drivers (Name, Phone, Vehicle, Status, Password)
        VALUES (?, ?, ?, ?, ?)
        """,
        (name, phone, vehicle, "Offline", password)
    )

    conn.commit()

    print("Driver Registered Successfully!")
def driver_login():
    phone = input("Enter Phone: ")
    password = input("Enter Password: ")

    cursor.execute(
        """
        SELECT DriverID, Name
        FROM Drivers
        WHERE Phone=? AND Password=?
        """,
        (phone, password)
    )

    driver = cursor.fetchone()

    if driver:
        print(f"\nWelcome Driver {driver.Name}!")
        return driver.DriverID
    else:
        print("Invalid Phone or Password!")
        return None
    
def view_booked_rides():

    cursor.execute("""
        SELECT RideID, RiderID, Pickup, Destination
        FROM Rides
        WHERE RideStatus='Booked'
    """)

    rides = cursor.fetchall()

    if not rides:
        print("No Booked Rides Available.")
        return

    print("\n===== Pending Rides =====")

    for ride in rides:
        print("--------------------------------")
        print(f"Ride ID      : {ride.RideID}")
        print(f"Rider ID     : {ride.RiderID}")
        print(f"Pickup       : {ride.Pickup}")
        print(f"Destination  : {ride.Destination}")

def accept_ride(driver_id):

    ride_id = input("Enter Ride ID to Accept: ")

    cursor.execute("""
        UPDATE Rides
        SET DriverID=?,
            RideStatus='Accepted'
        WHERE RideID=? AND RideStatus='Booked'
    """, (driver_id, ride_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Ride Accepted Successfully!")
    else:
        print("Ride not found or already accepted.")

def reject_ride():

    ride_id = input("Enter Ride ID to Reject: ")

    cursor.execute("""
        UPDATE Rides
        SET RideStatus='Rejected'
        WHERE RideID=? AND RideStatus='Booked'
    """, (ride_id,))

    conn.commit()

    if cursor.rowcount > 0:
        print("Ride Rejected Successfully!")
    else:
        print("Ride not found.")

def start_ride(driver_id):

    ride_id = input("Enter Ride ID to Start: ")

    cursor.execute("""
        UPDATE Rides
        SET RideStatus='In Progress'
        WHERE RideID=?
        AND DriverID=?
        AND RideStatus='Accepted'
    """,(ride_id,driver_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Ride Started Successfully!")
    else:
        print("Ride cannot be started.")

def end_ride(driver_id):

    ride_id = input("Enter Ride ID to End: ")

    cursor.execute("""
        UPDATE Rides
        SET RideStatus='Completed'
        WHERE RideID=?
        AND DriverID=?
        AND RideStatus='In Progress'
    """,(ride_id,driver_id))

    conn.commit()

    if cursor.rowcount > 0:
        print("Ride Completed Successfully!")
    else:
        print("Ride cannot be completed.")