from config.db import cursor, conn

def make_payment(rider_id):

    ride_id = input("Enter Ride ID: ")

    cursor.execute("""
        SELECT Fare, RideStatus
        FROM Rides
        WHERE RideID=? AND RiderID=?
    """, (ride_id, rider_id))

    ride = cursor.fetchone()

    if ride is None:
        print("Ride not found!")
        return

    if ride.RideStatus != "Completed":
        print("Payment can only be made after ride completion.")
        return

    print("\nChoose Payment Method")
    print("1. Cash")
    print("2. UPI")
    print("3. Card")

    choice = input("Enter Choice: ")

    if choice == "1":
        mode = "Cash"
    elif choice == "2":
        mode = "UPI"
    elif choice == "3":
        mode = "Card"
    else:
        print("Invalid Payment Method")
        return

    cursor.execute("""
        INSERT INTO Payments
        (RideID, Amount, PaymentMode)
        VALUES (?, ?, ?)
    """, (ride_id, ride.Fare, mode))

    conn.commit()

    print("\nPayment Successful!")
    print("-------------------------")
    print("Ride ID :", ride_id)
    print("Amount  :", ride.Fare)
    print("Mode    :", mode)