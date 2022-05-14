from flask import Flask
from flask_mysqldb import MySQL
from requests import get

app = Flask(__name__)

app.config["DEBUG"] = True
app.config["MYSQL_HOST"] = "mysql_api_container"
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "flaskdocker"

mysql = MySQL(app)

@app.route("/", methods=["GET"])
def index():
    data = get("https://randomuser.me/api")
    return data.json()


@app.route("/inserthost", methods=["POST"])
def inser_thost():
    data = get("https://randomuser.me/api").json()
    user_name = data["results"][0]["name"]["first"]

    cur = mysql.connection.cursor()
    cur.execute("""INSERT INTO users(name) VALUES(%s)""", (user_name))
    mysql.connection.commit()
    cur.close()

    return user_name


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
