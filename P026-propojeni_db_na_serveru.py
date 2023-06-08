import mysql.connector

try:
    connection = mysql.connector.connect(
        host="remote_host_address",
        port="remote_port",
        database="your_database_name",
        user="your_username",
        password="your_password"
    )

    # Zde pište kod
    
    connection.close()  #Zavrit spojeni
except mysql.connector.Error as error:
    print("Error connecting to MySQL database:", error)
