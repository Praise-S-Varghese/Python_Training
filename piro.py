import psycopg2
    
def db_open_conn():
    conn = psycopg2.connect(
            host = "localhost",
            user = "praise",
            password = "praise123",
            database = "python_praise",
            port = "5432"
        )
    return conn
print(db_open_conn)

def db_close_conn():
  conn = db_open_conn()

  return conn.close()

