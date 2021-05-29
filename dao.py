import pymysql
import os
from dotenv import load_dotenv
load_dotenv()

db = pymysql.connect(host=os.environ.get("DBIP"),
                    user=os.environ.get("USER"),
                    password=os.environ.get("PASSWORD"),
                    database='profrate'
                    )

async def insert_prof():
    return
async def delete_prof(id):
    with db.cursor() as cursor:
        sql = "DELETE FROM Professors where profid = %s"
        cursor.execute(sql, (id))
    return
async def insert_rating():
    return
async def delete_rating():
    return
async def get_profid(lastname: str):
    with db.cursor() as cursor:
        # Create a new record
        sql = "SELECT profid FROM Professors where lastname = %s"
        cursor.execute(sql, (lastname))
    return int(cursor.fetchone()[0])