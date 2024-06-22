import mysql.connector

if __name__ == "__main__":
    mydb = mysql.connector.connect(
        host = "localhost",
        user="user",
        password="password123",
        database="nodepeopledb"
    )
    mycursor = mydb.cursor()

    insertStatement = "INSERT INTO people (name, email, phonenumber) VALUES (%s, %s, %s)"
    usrInput = input("Input new person's name, email, and phone number:")
    values = usrInput.split()
    sqlValues = (values[0],values[1],values[2])

    mycursor.execute(insertStatement,sqlValues)
    
    mydb.commit()
    print(mycursor.rowcount, "record inserted")
    print("Current database of people:")

    mycursor.execute("SELECT * FROM people")
    myresult = mycursor.fetchall()

    for x in myresult:
        print(x)