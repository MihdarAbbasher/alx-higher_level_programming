--insert ex --
insert_stmt = (
  "INSERT INTO employees (emp_no, first_name, last_name, hire_date) "
  "VALUES (%s, %s, %s, %s)"
)
data = (2, 'Jane', 'Doe', datetime.date(2012, 3, 23))
cursor.execute(insert_stmt, data)




--select ex--
select_stmt = "SELECT * FROM employees WHERE emp_no = %(emp_no)s"
cursor.execute(select_stmt, { 'emp_no': 2 })




-- cursor.execute(operation, params=None, multi=False)
-- iterator = cursor.execute(operation, params=None, multi=True)

-- multiple statements

operation = 'SELECT 1; INSERT INTO t1 VALUES (); SELECT 2'
for result in cursor.execute(operation, multi=True):
  if result.with_rows:
    print("Rows produced by statement '{}':".format(
      result.statement))
    print(result.fetchall())
  else:
    print("Number of rows affected by statement '{}': {}".format(
      result.statement, result.rowcount))
