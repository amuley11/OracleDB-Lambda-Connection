import json
import boto3
import os
import cx_Oracle

def lambda_handler(event, context):
    
    host = os.getenv('host') # oracledb.cqpgngvvicic.us-east-2.rds.amazonaws.com
    port = os.getenv('port') # 1521
    sid = os.getenv('sid') # ORCL
    db_user = os.getenv('db_user') # <user-id>
    db_password = os.getenv('db_password') # <password

    dsn_tns = cx_Oracle.makedsn(host, port, service_name = sid)
    conn = cx_Oracle.connect(user = db_user, password = db_password, dsn = dsn_tns, encoding = 'UTF-8')

    c = conn.cursor()
    #c.execute("select * from countries order by gdp desc") # use triple quotes if query is spreading on multiple line
    #c.execute("select * from countries where region = 'Europe'")
    #c.execute("select * from countries where gdp > 2500000")
    c.execute("select * from countries where gdp > 2500000 and region = 'Asia'")
    for row in c:
        print (row[0], '-', row[1], '-', row[2], '-', row[3]) # To show an additional columns, please add , "'-', row[4]" and so on
    conn.close()

    return "Connection established with Oracle database"
