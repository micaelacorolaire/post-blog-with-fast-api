import mysql.connector
# Configura la conexión a MySQL
db_config = {
    "user": "root",
    "password": "micaelacorolaire",
    "host": "localhost",
    "database": "postblogwithfastapi",
}

conn = mysql.connector.connect(**db_config)