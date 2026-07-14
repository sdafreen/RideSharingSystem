import pyodbc

conn = pyodbc.connect(
    "DRIVER={SQL Server};"
    "SERVER=DESKTOP-4TB6OEF\\SQLEXPRESS;"
    "DATABASE=RideSharing;"
    "Trusted_Connection=yes;"
)

cursor = conn.cursor()

print("Database Connected Successfully!")