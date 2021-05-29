import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

db = pymysql.connect(host=os.environ.get("DBIP"),
                    user=os.environ.get("USER"),
                    password=os.environ.get("PASSWORD"),
                    database='profrate'
                    )

async def insert_prof(fname: str, lname: str):
    with db.cursor() as cursor:
        sql = "INSERT INTO Professors (firstname,lastname) VALUES (%s,%s)"
        cursor.execute(sql,(fname, lname))
        db.commit()
    return
async def delete_prof(lastname: str):
    with db.cursor() as cursor:
        sql = "DELETE FROM Professors where lastname = %s"
        cursor.execute(sql,(lastname))
        db.commit()
    return

async def insert_rating(profid: int, userid: str, quality: int, difficulty: int, gradereceived: int):
    with db.cursor() as cursor:
        sql = "INSERT INTO Ratings (profid,raterid,quality,difficulty,gradereceived) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql,(profid, userid.replace('!',''), quality, difficulty, gradereceived))
        db.commit()
    return
    
async def delete_rating(profid: int, userid: str):
    with db.cursor() as cursor:
        sql = "DELETE FROM Ratings where profid = %s and raterid = %s"
        cursor.execute(sql, (profid, userid.replace('!','')))
        db.commit()

async def get_rating(profid: int, userid: str):
    with db.cursor() as cursor:
        # Create a new record
        sql = "SELECT * FROM Ratings where profid = %s and raterid = %s"
        cursor.execute(sql, (profid, userid.replace('!','')))
    return cursor.fetchone()[0] if cursor.rowcount != 0 else -1

async def get_profid(lastname: str):
    with db.cursor() as cursor:
        # Create a new record
        sql = "SELECT profid FROM Professors where lastname = %s"
        cursor.execute(sql, (lastname))
    return int(cursor.fetchone()[0]) if cursor.rowcount != 0 else -1
        
    
    