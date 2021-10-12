from piro import db_open_conn, db_close_conn
# import psycopg2
    
# def db_open_conn():
#     conn = psycopg2.connect(
#             host = "localhost",
#             user = "praise",
#             password = "praise123",
#             database = "python_praise",
#             port = "5432"
#         )
#     return conn
# print(db_open_conn)

# def db_close_conn():
#   conn = db_open_conn()

#   return conn.close()


def test():
  conn = db_open_conn()

  cursor = conn.cursor()
  cursor.execute("select version()")
  data = cursor.fetchone()
  return data

print(test())


def create_table():
  conn = db_open_conn()
  conn.autocommit = True
  cursor = conn.cursor()
  cursor.execute("create table employees(employ_id  SERIAL PRIMARY KEY, employ_name char(30) not null, place char(30) not null, job_type char(30) not null)")
  cursor.execute("create table students(stud_id  SERIAL PRIMARY KEY, stud_name char(30) not null, place char(30) not null, field char(30) not null)")
  cursor.execute("create table workers(worker_id  SERIAL PRIMARY KEY, worker_name char(30) not null, place char(30) not null, job_type char(30) not null)")
  print("Table created...")

# create_table()

def insert_table():
  conn = db_open_conn()
  conn.autocommit = True
  cursor = conn.cursor()
  cursor.execute('''INSERT INTO EMPLOYEES(employ_name, place, job_type) VALUES ('Ramya', 'Delhi', 'Student')''')
  cursor.execute('''INSERT INTO STUDENTS(stud_name, place, field) VALUES ('Praise', 'Delhi', 'Computer Science')''')
  cursor.execute('''INSERT INTO workers(worker_name, place, job_type) VALUES ('Amit', 'Agra', 'Technician')''')

# insert_table()

def del_table():
  conn = db_open_conn()
  conn.autocommit = True
  cursor = conn.cursor()
  cursor.execute('''DELETE FROM employees WHERE employ_id=2''')
  cursor.execute('''DELETE FROM students WHERE stud_id=2''')
  cursor.execute('''DELETE FROM workers WHERE worker_id=2''')

# del_table()

def upd_table():
  conn = db_open_conn()
  conn.autocommit = True
  cursor = conn.cursor()
  cursor.execute('''UPDATE students SET place='Mumbai' WHERE stud_id=2''')

upd_table()

def alter_table():
  conn = db_open_conn()
  conn.autocommit = True
  cursor = conn.cursor()
  cursor.execute('''''')

def select_db():
  conn = db_open_conn()
  cursor = conn.cursor()
  cursor.execute("SELECT * from students")
  result1 = cursor.fetchone()
  # print(result1)

  result2 = cursor.fetchall()
  print(result2)

select_db()

db_close_conn()



