import sqlite3

db = sqlite3.connect("projec.db")

c = db.cursor()

c.execute(
    """
          CREATE TABLE users(
              number integer,
              surnmae text,
              state integer,
              city text,
          )
          """
)

db.commit()

db.close()
