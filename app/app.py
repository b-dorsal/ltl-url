from flask import Flask, request
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
    
    content = """
        <h1>ltl-url</h1>
        <form action="/create" method="post">
            <input type="text" name="url">
            <input type="submit">
        </form>
    """
    
    return content


@app.route("/<uuid>")
def reroute(uuid):
    cur = conn.cursor()

    cur.execute("""SELECT url FROM `ltlurldb`.`links` WHERE `uuid` = %s""", [uuid])
    result = cur.fetchone()
    url = result[0]
    cur.close()

    return f'<html><head><title>ltlurl</title></head><body><h1>{url}</h1><p>Redirecting...</p><script>setTimeout(function(){{window.location.replace("{url}")}}, 2000);</script></body>'


@app.route("/create", methods = ["POST"])
def create():
    
    url = request.form['url']
    uuid = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(6))
    
    cur = conn.cursor()

    cur.execute("""INSERT INTO `ltlurldb`.`links` (url, uuid) VALUES (%s, %s)""", [url,uuid])
    conn.commit()
    cur.close()

    return f'<h1>{uuid}</h1>'



if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)