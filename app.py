from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def home():
    db_host = os.getenv("DB_HOST")
    db_name = os.getenv("POSTGRES_DB")

    return f"Flask App Connected to Database: {db_name} on {db_host}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
    

    ##a