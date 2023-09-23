from flask import Flask, request, render_template, url_for
import mysql.connector
import random
import string

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
cur.close()

app = Flask(__name__)


@app.route("/")
def homepage():
    return render_template("home.html")


@app.route("/<uuid>")
def reroute(uuid):
    cur = conn.cursor()
    uuid = uuid.upper()
    cur.execute("""SELECT url FROM `ltlurldb`.`links` WHERE `uuid` = %s""", [uuid])
    result = cur.fetchone()
    url = result[0]
    cur.close()

    return render_template("url.html", url=url)


@app.route("/create", methods = ["POST"])
def create():
    
    url = request.form['url']
    uuid = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
    uuid = uuid.upper()
    cur = conn.cursor()

    cur.execute("""INSERT INTO `ltlurldb`.`links` (url, uuid) VALUES (%s, %s)""", [url,uuid])
    conn.commit()
    cur.close()

    return render_template("create.html", uuid=uuid)



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)