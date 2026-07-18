USE RideSharing;
GO

CREATE TABLE Riders
(
    RiderID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(50),
    Phone VARCHAR(15),
    Password VARCHAR(30)
);
CREATE TABLE Drivers
(
    DriverID INT PRIMARY KEY IDENTITY(1,1),
    Name VARCHAR(50),
    Phone VARCHAR(15),
    Vehicle VARCHAR(30),
    Status VARCHAR(20),
    Password VARCHAR(30)
); 
CREATE TABLE Rides
(
RideID INT PRIMARY KEY IDENTITY(1,1),
RiderID INT,
DriverID INT,
Pickup VARCHAR(100),
Destination VARCHAR(100),
Fare DECIMAL(10,2),
RideStatus VARCHAR(30),

FOREIGN KEY(RiderID) REFERENCES Riders(RiderID),
FOREIGN KEY(DriverID) REFERENCES Drivers(DriverID)
);

CREATE TABLE Payments
(
PaymentID INT PRIMARY KEY IDENTITY(1,1),
RideID INT,
Amount DECIMAL(10,2),
PaymentMode VARCHAR(20),

FOREIGN KEY(RideID) REFERENCES Rides(RideID)
);

UPDATE Drivers
SET Status = 'Online'
WHERE DriverID = 1;

SELECT * FROM Rides;
SELECT * FROM Riders;
SELECT * FROM Drivers;
SELECT * FROM Rides;
SELECT RideID, DriverID, RideStatus
FROM Rides;
SELECT RideID,
       DriverID,
       RideStatus
FROM Rides;
SELECT * FROM Payments;