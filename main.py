# CodeGrade step0
# Run this cell without changes

# SQL Library and Pandas Library
import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect('data.sqlite')

pd.read_sql("""SELECT * FROM sqlite_master""", conn)

# CodeGrade step1
# Replace None with your code
df_boston = pd.read_sql("""
    SELECT e.firstName, e.lastName
    FROM employees e
    JOIN offices o
    USING(officeCode)
    WHERE o.city = "Boston"
""", conn)

df_boston

df_city = pd.read_sql("""
SELECT * FROM employees
""", conn)

df_city

# CodeGrade step2
# Replace None with your code
df_zero_emp = pd.read_sql("""
    SELECT o.officeCode, o.city
    FROM offices o
    LEFT JOIN employees e
    USING(officeCode)
    WHERE e.employeeNumber IS NULL
""", conn)

df_zero_emp

# CodeGrade step3
# Replace None with your code
df_employee = pd.read_sql("""
    SELECT e.firstName, e.lastName, o.city, o.state
    FROM employees e
    LEFT JOIN offices o
    USING(officeCode)
    ORDER BY firstName,lastName
""", conn)

df_employee

# CodeGrade step4
# Replace None with your code
df_contacts = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, c.phone, c.salesRepEmployeeNumber
    FROM customers c
    LEFT JOIN orders o
    USING(customerNumber)
    WHERE orderNumber IS NULL
    ORDER BY c.contactLastName ASC;

""", conn)

df_contacts

# CodeGrade step5
# Replace None with your code
df_payment = pd.read_sql("""
    SELECT c.contactFirstName, c.contactLastName, p.amount, p.paymentDate
    FROM customers c
    JOIN payments p
    USING(customerNumber)
    ORDER BY CAST(p.amount AS REAL) DESC;

""", conn)

df_payment

# CodeGrade step6
# Replace None with your code
df_credit = pd.read_sql("""
    SELECT e.employeeNumber,e.firstName,e.lastName, COUNT(c.customerNumber) as customer_numbers
    FROM employees e
    JOIN customers c
    ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY e.employeeNumber, e.firstName, e.lastName
    HAVING AVG(c.creditLimit) > 90000
    ORDER BY customer_numbers DESC
    LIMIT 4;

""", conn)

df_credit

# CodeGrade step7
# Replace None with your code
df_product_sold = pd.read_sql("""
    SELECT p.productName, COUNT(od.orderNumber) AS numorders,
    SUM(od.quantityOrdered) AS totalunits
    FROM products p
    JOIN orderdetails od
    ON p.productCode = od.productCode
    GROUP BY p.productName
    ORDER BY totalunits DESC;

""", conn)

df_product_sold

# CodeGrade step8
# Replace None with your code
df_total_customers = pd.read_sql("""
    SELECT p.productName, p.productCode, COUNT(DISTINCT o.customerNumber) AS numpurchasers
    FROM products p
    JOIN orderdetails od
    ON p.productCode = od.productCode
    JOIN orders o
    ON od.orderNumber = o.orderNumber
    GROUP BY p.productCode, p.productName
    ORDER BY numpurchasers DESC;
""", conn)
df_total_customers

# CodeGrade step9
# Replace None with your code
df_customers = pd.read_sql("""
    SELECT o.officeCode, o.city, COUNT(c.customerNumber) AS n_customers
    FROM offices o
    JOIN employees e
    ON o.officeCode = e.officeCode
    JOIN customers c
    ON e.employeeNumber = c.salesRepEmployeeNumber
    GROUP BY o.officeCode, o.city;
""", conn)
df_customers

# CodeGrade step10
# Replace None with your code
df_under_20 = pd.read_sql("""
    WITH low_products AS (
    SELECT  p.productCode
    FROM products p
    JOIN orderdetails od
    ON p.productCode = od.productCode
    JOIN orders o
    ON od.orderNumber = o.orderNumber
    GROUP BY p.productCode
    HAVING COUNT(DISTINCT o.customerNumber) < 20
)

    SELECT DISTINCT e.employeeNumber, e.firstName, e.lastName, of.city, of.officeCode
    FROM employees e
    JOIN offices of
    ON e.officeCode = of.officeCode
    JOIN customers c
    ON e.employeeNumber = c.salesRepEmployeeNumber
    JOIN orders o
    ON c.customerNumber = o.customerNumber
    JOIN orderdetails od
    ON o.orderNumber = od.orderNumber
    JOIN low_products lp
    ON od.productCode = lp.productCode
    ORDER BY e.lastName ASC;
""", conn)

df_under_20

# Run this cell without changes

conn.close()