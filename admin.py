from config.db import cursor

def view_riders():

    cursor.execute("SELECT * FROM Riders")

    riders = cursor.fetchall()

    print("\n========== Riders ==========")

    for rider in riders:
        print("--------------------------------")
        print("ID      :", rider.RiderID)
        print("Name    :", rider.Name)
        print("Phone   :", rider.Phone)
    
def view_drivers():

    cursor.execute("SELECT * FROM Drivers")

    drivers = cursor.fetchall()

    print("\n========== Drivers ==========")

    for driver in drivers:
        print("--------------------------------")
        print("ID      :", driver.DriverID)
        print("Name    :", driver.Name)
        print("Vehicle :", driver.Vehicle)
        print("Status  :", driver.Status)

def view_rides():

    cursor.execute("SELECT * FROM Rides")

    rides = cursor.fetchall()

    print("\n========== Rides ==========")

    for ride in rides:
        print("--------------------------------")
        print("Ride ID     :", ride.RideID)
        print("Rider ID    :", ride.RiderID)
        print("Driver ID   :", ride.DriverID)
        print("Pickup      :", ride.Pickup)
        print("Destination :", ride.Destination)
        print("Fare        :", ride.Fare)
        print("Status      :", ride.RideStatus)

def view_payments():

    cursor.execute("SELECT * FROM Payments")

    payments = cursor.fetchall()

    print("\n========== Payments ==========")

    for payment in payments:
        print("--------------------------------")
        print("Payment ID :", payment.PaymentID)
        print("Ride ID    :", payment.RideID)
        print("Amount     :", payment.Amount)
        print("Mode       :", payment.PaymentMode)