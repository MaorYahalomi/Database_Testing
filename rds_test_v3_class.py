import pymysql
import json
a = 20

with open('creds//creds.json') as file:
    creds = json.load(file)

    db_url=creds["db_url"]
    db_user=creds["db_user"]
    db_pass=creds["db_pass"]
    db_name=creds["db_name"]

with open('names.json') as file:
    names = json.load(file)
    name_list = names["names_list"]

class DB_Manager:

  def __init__(self, url, username, password, database_name):
        self.db_url = url
        self.db_user = username
        self.db_pass = password
        self.db_name = database_name
        self.connection, self.cursorObject = self.db_connect(db_url, db_user, db_pass, db_name)
   

  def db_connect(self, db_url, db_user, db_pass, db_name):
    connection = pymysql.connect(host=db_url,
                                user=db_user,
                                password=db_pass,
                                database=db_name,
                                charset='utf8mb4',
                                connect_timeout= 5,
                                cursorclass=pymysql.cursors.DictCursor)

    cursorObject = connection.cursor()
    return connection, cursorObject

  def create_table(self):
    # # # SQL Create new Table:
    sqlQuery = "CREATE TABLE Users(Username varchar(32), Password int, Company varchar(32), Mail varchar(32))"
    self.cursorObject.execute(sqlQuery)
    sqlQuery = "show tables"
    self.cursorObject.execute(sqlQuery)

  def fetch_all_data(self):
    # Fetch all the rows
    self.cursorObject.execute("SELECT * FROM Users")
    myresult = self.cursorObject.fetchall()
    for x in myresult:
      print(x)
      self.cursorObject.close()

  def query(self, data):
  # Add new Record:
    # sql = 'INSERT INTO Users (Username, Password, Company, Mail) VALUES ("bob", "1s2522","Amazon","bob@amazon.com")'
    # sql = 'INSERT INTO Users (Username, Password, Company, Mail) VALUES ("Maor", "123456","Amazon","mm@amazon.com")'
    # sql = 'INSERT INTO Users (Username, Password, Company, Mail) VALUES ("bibi", "1q234W56","Amazon","bibi@amazon.com")'
    sql = f"INSERT INTO Users (Username, Password, Company, Mail) VALUES ('{data['Username']}','{data['Password']}','{data['Company']}','{data['Mail']}')"
    print(sql)
    self.cursorObject.execute(sql)
    self.connection.commit()


## Main:

data = {"Username": "Aviv", "Password": "123456",
        "Company": "AWS", "Mail": "aviv@amazon.com"}

db_connection = DB_Manager(db_url, db_user, db_pass, db_name)
# db_connection.create_table()
# db_connection.query(data)
db_connection.fetch_all_data()



