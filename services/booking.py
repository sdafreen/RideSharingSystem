from config.db import cursor, conn

def book_ride(rider_id):
    pickup = input("Enter Pickup Location: ")
    destination = input("Enter Destination: ")

    # Find the first online driver
    cursor.execute("""
        SELECT TOP 1 DriverID
        FROM Drivers
        WHERE Status = 'Online'
    """)

    driver = cursor.fetchone()

    if driver is None:
        print("No Online Driver Available!")
        return

    fare = 250.00   # Fixed fare for now

    cursor.execute("""
        INSERT INTO Rides
        (RiderID, DriverID, Pickup, Destination, Fare, RideStatus)
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    (rider_id, driver.DriverID, pickup, destination, fare, "Booked"))

    conn.commit()

def view_history(rider_id):

    cursor.execute("""
        SELECT RideID,
               Pickup,
               Destination,
               Fare,
               RideStatus
        FROM Rides
        WHERE RiderID=?
    """, (rider_id,))

    rides = cursor.fetchall()

    if not rides:
        print("No Ride History Found.")
        return

    print("\n========== Ride History ==========")

    for ride in rides:
        print("-----------------------------------")
        print(f"Ride ID     : {ride.RideID}")
        print(f"Pickup      : {ride.Pickup}")
        print(f"Destination : {ride.Destination}")
        print(f"Fare        : ₹{ride.Fare}")
        print(f"Status      : {ride.RideStatus}")

    print("Ride Booked Successfully!")

def cancel_ride(rider_id):

    ride_id = input("Enter Ride ID to Cancel: ")

    cursor.execute("""
        SELECT RideStatus
        FROM Rides
        WHERE RideID=? AND RiderID=?
    """, (ride_id, rider_id))

    ride = cursor.fetchone()

    if ride is None:
        print("Ride not found!")
        return

    if ride.RideStatus == "Cancelled":
        print("Ride is already cancelled!")
        return

    if ride.RideStatus == "Completed":
        print("Completed rides cannot be cancelled!")
        return

    cursor.execute("""
        UPDATE Rides
        SET RideStatus='Cancelled'
        WHERE RideID=? AND RiderID=?
    """, (ride_id, rider_id))

    conn.commit()

    print("Ride Cancelled Successfully!")