
from piro import db_open_conn,db_close_conn


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
# insert_table()

def select_db():
  conn = db_open_conn()
  cursor = conn.cursor()
  cursor.execute("SELECT employ_name, place from employees")
  result1 = cursor.fetchone()
  print(result1)

  result2 = cursor.fetchall()
  print(result2)

select_db()

db_close_conn()



