import pymysql
import json
a = 13

names = [
    "Aaren",
    "Aarika",
    "Abagael",
    "Abagail",
    "Abbe",
    "Abbey",
    "Abbi",
    "Abbie",
    "Abby",
    "Abbye",
    "Abigael",
    "Abigail",
    "Abigale",
    "Abra",
    "Ada",
    "Adah",
    "Adaline",
    "Adan",
    "Adara",
    "Adda",
    "Addi",
    "Addia",
    "Addie",
    "Addy",
    "Adel",
    "Adela",
    "Adelaida",
    "Adelaide",
    "Adele",
    "Adelheid",
    "Adelice",
    "Adelina",
    "Adelind",
    "Adeline",
    "Adella",
    "Adelle",
    "Adena",
    "Adey",
    "Adi",
    "Adiana",
    "Adina",
    "Adora",
    "Adore",
    "Adoree",
    "Adorne",
    "Adrea",
    "Adria",
    "Adriaens",
    "Adrian",
    "Adriana",
    "Adriane",
    "Adrianna",
    "Adrianne",
    "Adriena",
    "Adrienne",
    "Aeriel",
    "Aeriela",
    "Aeriell",
    "Afton",
    "Ag",
    "Agace",
    "Agata",
    "Agatha",
    "Agathe",
    "Aggi",
    "Aggie",
    "Aggy",
    "Agna",
    "Agnella",
    "Agnes",
    "Agnese",
    "Agnesse",
    "Agneta",
    "Agnola",
    "Agretha",
    "Aida",
    "Aidan",
    "Aigneis",
    "Aila",
    "Aile",
    "Ailee",
    "Aileen",
    "Ailene",
    "Ailey",
    "Aili",
    "Ailina",
    "Ailis",
    "Ailsun",
    "Ailyn",
    "Aime",
    "Aimee",
    "Aimil",
    "Aindrea",
    "Ainslee",
    "Ainsley",
    "Ainslie",
    "Ajay",
    "Alaine",
    "Alameda",
    "Alana",
    "Alanah",
    "Alane",
    "Alanna",
    "Alayne",
    "Alberta",
    "Albertina",
    "Albertine",
    "Albina",
    "Alecia",
    "Aleda",
    "Aleece",
    "Aleen",
    "Alejandra",
    "Alejandrina",
    "Alena",
    "Alene",
    "Alessandra",
    "Aleta",
    "Alethea",
    "Alex",
    "Alexa",
    "Alexandra",
    "Alexandrina",
    "Alexi",
    "Alexia",
    "Alexina",
    "Alexine",
    "Alexis",
    "Alfi",
    "Alfie",
    "Alfreda",
    "Alfy",
    "Ali",
    "Alia",
    "Alica",
    "Alice",
    "Alicea",
    "Alicia",
    "Alida",
    "Alidia",
    "Alie",
    "Alika",
    "Alikee",
    "Alina",
    "Aline",
    "Alis",
    "Alisa",
    "Alisha",
    "Alison",
    "Alissa",
    "Alisun",
    "Alix",
    "Aliza",
    "Alla",
    "Alleen",
    "Allegra",
    "Allene",
    "Alli",
    "Allianora",
    "Allie",
    "Allina",
    "Allis",
    "Allison",
    "Allissa",
    "Allix",
    "Allsun",
    "Allx",
    "Ally",
    "Allyce",
    "Allyn"]

with open('creds//creds.json') as file:
    creds = json.load(file)

    db_url=creds["db_url"]
    db_user=creds["db_user"]
    db_pass=creds["db_pass"]
    db_name=creds["db_name"]

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
    # sql = 'INSERT INTO Users (Username, Password, Company, Mail) VALUES ("bob", "1s2522","Amazon","aamzm@amazon.com")'
    # sql = 'INSERT INTO Users (Username, Password, Company, Mail) VALUES ("Maor", "123456","Amazon","mm@amazon.com")'
    # sql = 'INSERT INTO Users (Username, Password, Company, Mail) VALUES ("bibi", "1q234W56","Amazon","amzm@amazon.com")'
    sql = f"INSERT INTO Users (Username, Password, Company, Mail) VALUES ('{data['Username']}','{data['Password']}','{data['Company']}','{data['Mail']}')"
    print(sql)
    self.cursorObject.execute(sql)
    self.connection.commit()


## Main:

data = {"Username": "Aviv", "Password": "123456",
        "Company": "AWS", "Mail": "aviv@amazon.com"}
db_connection = DB_Manager(db_url, db_user, db_pass, db_name)
db_connection.query(data)
# db_connection.create_table()
db_connection.fetch_all_data()


