from flask import Flask
import mysql.connector

import os


sql_username = os.getenv('SQL_USR_USERNAME')
sql_password = os.getenv('SQL_USR_PASSWORD')

conn = mysql.connector.connect(
  host="mysql",
  user=sql_username,
  password=sql_password
)

cur = conn.cursor()
cur.execute("select @@version")
output = cur.fetchall()
print(output)
conn.close()
app = Flask(__name__)


@app.route("/")
def homepage():
    return "<h1>ltl-url</h1>"


@app.route("/<uuid>")
def reroute(uuid):
    
    conn = mysql.connector.connect(
        host="mysql",
        user=sql_username,
        password=sql_password
    )
    cur = conn.cursor()
      
    # Select query
    cur.execute(f'SELECT url FROM links WHERE uuid like \'{uuid}\'')
    output = cur.fetchall()
      
    for i in output:
        print(i)
      
    # To close the connection
    conn.close()
    
    return "<h1>ltl-url</h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)