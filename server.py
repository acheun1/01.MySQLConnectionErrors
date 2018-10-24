#Assignment: MySQL connection errors
#2018 10 07
#Cheung Anthony

# Create a simple registration page with the following fields:

from flask import Flask

from mysqlconnection import connectToMySQL

app = Flask(__name__)
mysql = connectToMySQL('twitter')

print("all the users", mysql.query_db("SELECT * FROM users;"))

if __name__=="__main__":
    app.run(debug=True)
