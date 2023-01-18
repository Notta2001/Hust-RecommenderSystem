import sqlite3

class SQLite3:
  def __init__(self):
    try:
      self.sqlite_connection = sqlite3.connect('/home/notta/Desktop/Coding/hust-20221/recommender-system/db/thesis-DSS.db')
      self.cursor = self.sqlite_connection.cursor()
      print("Database created and Successfully Connected to SQLite")

      sqlite_select_query = "select * from teacher;"
      self.cursor.execute(sqlite_select_query)
      record = self.cursor.fetchall()
      degree_score = {
        ""
      }
      for doc in record:
        degrees = doc[3].split(", ")
        for degree in degrees:
          print(degree)
      print("First data", record[0][3])
      self.cursor.close()
    except sqlite3.Error as error:
      print("Error whilte connecting to sqlite", error)
    finally:
      if self.sqlite_connection:
        self.sqlite_connection.close()
        print("The SQLite connection is closed!") 

SQLite3()