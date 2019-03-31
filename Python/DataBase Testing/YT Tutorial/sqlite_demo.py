import sqlite3
from employee import Employee

conn = sqlite3.connect('employee.db')

c = conn.cursor()

try:
    c.execute("""CREATE TABLE employees (
            first text,
            last text,
            pay integer
            )""")
except Exception as e:
    pass

emp_1 = Employee('John', 'Smith', 5000)
emp_2 = Employee('Johnny', 'Appleseed', 15000)

print(emp_1.first)

# c.execute("INSERT INTO employees VALUES ('James', 'McCarthy', 500)")

c.execute("SELECT * FROM employees WHERE last='McCarthy'")
print(c.fetchone())


conn.commit()

conn.close()
