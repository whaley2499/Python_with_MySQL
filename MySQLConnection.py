import mysql.connector

def sqlInput(insertStatement,sqlValues):
    try:
        mycursor.execute(insertStatement,sqlValues)
        mydb.commit()
    except:
        print("User input Error")
        raise(AssertionError)

try:
    mydb = mysql.connector.connect(
        host = "localhost",
        user="user",
        password="password123",
        database="nodepeopledb"
    )
except:
    print("Error: Cannot connect to database")
    exit(ConnectionError)

mycursor = mydb.cursor()

if __name__ == "__main__":

    insertStatement = "INSERT INTO people (name, email, phonenumber) VALUES (%s, %s, %s)"
    userInput = input("Input new person's name, email, and phone number seperated by spaces:\n").strip()
    values = userInput.split()
    sqlValues = (values[0],values[1],values[2])

    sqlInput(insertStatement,sqlValues)

    print(mycursor.rowcount, "record inserted")

    userSelection = input("Print Current Database?(Y/N)").upper().strip()
    if userSelection == "Y":
        print("Current database of people: \n")

        mycursor.execute("SELECT * FROM people")
        myresult = mycursor.fetchall()
        for x in myresult:
            print(x)
        print()