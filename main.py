# from services.booking import book_ride
from admin import (
    view_riders,
    view_drivers,
    view_rides,
    view_payments
)
from services.booking import book_ride, view_history, cancel_ride
# from services.booking import book_ride, view_history
from models.rider import register, login
from models.driver import (
    driver_register,
    driver_login,
    view_booked_rides,
    accept_ride,
    reject_ride,
    start_ride,
    end_ride
)
from services.payment import make_payment
while True:
    print("\n========== Ride Sharing System ==========")
    print("1. Rider Register")
    print("2. Rider Login")
    print("3. Driver Register")
    print("4. Driver Login")
    print("5. Admin View")
    print("6. Exit")

    choice = input("Enter Choice: ")

    if choice == "1":
        register()



    elif choice == "2":
        rider_id = login()

        if rider_id:

         while True:

            print("\n===== Rider Dashboard =====")
            print("1. Book Ride")
            print("2. View Ride History")
            print("3. Cancel Ride")
            print("4. Make Payment")
            print("5. Logout")

            ch = input("Enter Choice: ")

            if ch == "1":
                book_ride(rider_id)

            elif ch == "2":
                view_history(rider_id)

            elif ch == "3":
                cancel_ride(rider_id)

            elif ch == "4":
                make_payment(rider_id)

            elif ch == "5":
                print("Logged out successfully!")
                break

            else:
                print("Invalid Choice")
                
    elif choice == "3":
        driver_register()

    elif choice == "4":
         driver_id = driver_login()

         if driver_id:

          while True:

            print("\n===== Driver Dashboard =====")
            print("1. View Booked Rides")
            print("2. Accept Ride")
            print("3. Reject Ride")
            print("4. Start Ride")
            print("5. End Ride")
            print("6. Logout")

            ch = input("Enter Choice: ")

            if ch == "1":
                view_booked_rides()
            
            elif ch == "2":
                accept_ride(driver_id)

            elif ch == "3":
                reject_ride()

            elif ch == "4":
                start_ride(driver_id)

            elif ch == "5":
                end_ride(driver_id)

            elif ch == "6":
                print(" DriverLogged out successfully!")
                break

            else:
                print("Invalid Choice")
    elif choice == "5":
        username = input("Enter Admin Username: ")
        password = input("Enter Password: ")

        if username == "SD AFREEN" and password == "SYED123":

            while True:
                print("\n========== ADMIN PANEL ==========")
                print("1. View Riders")
                print("2. View Drivers")
                print("3. View Rides")
                print("4. View Payments")
                print("5. Logout")

                ch = input("Enter Choice: ")

                if ch == "1":
                    view_riders()

                elif ch == "2":
                    view_drivers()

                elif ch == "3":
                    view_rides()

                elif ch == "4":
                    view_payments()

                elif ch == "5":
                    break

                else:
                    print("Invalid Choice")

        else:
            print("Invalid Admin Credentials")
            
    elif choice == "6":
        print("Thank You!")
        break   

    else:
        print("Invalid Choice")