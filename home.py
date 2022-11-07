import mysql.connector

mydb = mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'home_db')

mycursor = mydb.cursor()

while(True):
    print('''
            Enter the option below
            1 :Insert
            2 :View
            3 :Search
            4 :Exit
    ''')

    choice = int(input("Enter the choice you need"))

    if(choice == 1):
        print("Enter the details")
        temp = int(input("Enter the temperature"))
        hum = int(input("Enter the humidity"))
        moist = input("Enter the moisture")
        sensor = input("Enter the sensor value")
        sql = "INSERT INTO `home_automation`(`temp`, `humidity`, `moisture`, `date`, `sensor_values`) VALUES(%s,%s,%s,now(),%s)"
        data = (temp,hum,moist,sensor)
        mycursor.execute(sql,data)
        mydb.commit()
    elif(choice==2):
        print('View the data')
    elif(choice==3):
        print("Search the data using the date")
    elif(choice==4):
        break