import pymysql
import discord
import os
from dotenv import load_dotenv
load_dotenv()

db = pymysql.connect(host=os.environ.get("DBIP"),
                    user=os.environ.get("USER"),
                    password=os.environ.get("PASSWORD"),
                    database='profrate'
                    )

def meme():
    with db:
    #with connection.cursor() as cursor:
            # Create a new record
            #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
            #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))

        # connection is not autocommit by default. So you must commit to save
        # your changes.
        #connection.commit()

        with db.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `Ratings`"
            cursor.execute(sql)
            result = cursor.fetchone()
            print(result)