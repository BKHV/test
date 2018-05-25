import psycopg2

DATABASE_URL = os.environ['DATABASE_URL']

conn = psycopg2.connect(DATABASE_URL, sslmode='require')
cur = conn.cursor()     
cur.execute("INSERT INTO bot_users (username) VALUES ('AAA')")
conn.commit()
cur.close()
conn.close() 

app = Flask(__name__)
if __name__ == "__main__":
    app.run()