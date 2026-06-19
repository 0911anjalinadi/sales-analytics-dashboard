from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="phoenix@#45",
        database="sales_analytics"
    )

@app.route("/")
def dashboard():

    conn = get_connection()
    cursor = conn.cursor()

    # Total Revenue
    cursor.execute("SELECT SUM(sale_amount) FROM sales")
    revenue = cursor.fetchone()[0]

    # Total Customers
    cursor.execute("SELECT COUNT(*) FROM customers")
    customers = cursor.fetchone()[0]

    # Total Products
    cursor.execute("SELECT COUNT(*) FROM products")
    products = cursor.fetchone()[0]

    # Top Customer
    cursor.execute("""
        SELECT c.customer_name, SUM(s.sale_amount) AS total_spent
        FROM sales s
        JOIN customers c ON s.customer_id = c.customer_id
        GROUP BY c.customer_name
        ORDER BY total_spent DESC
        LIMIT 1
    """)
    top_customer = cursor.fetchone()

    # Recent Sales
    cursor.execute("""
        SELECT
            c.customer_name,
            p.product_name,
            s.sale_amount,
            s.sale_date
        FROM sales s
        JOIN customers c ON s.customer_id = c.customer_id
        JOIN products p ON s.product_id = p.product_id
        ORDER BY s.sale_date DESC
    """)
    recent_sales = cursor.fetchall()

    # Product Revenue
    cursor.execute("""
        SELECT
            p.product_name,
            SUM(s.sale_amount)
        FROM sales s
        JOIN products p ON s.product_id = p.product_id
        GROUP BY p.product_name
    """)
    product_revenue = cursor.fetchall()

    # Top 3 Customers
    cursor.execute("""
        SELECT
            c.customer_name,
            SUM(s.sale_amount)
        FROM sales s
        JOIN customers c ON s.customer_id = c.customer_id
        GROUP BY c.customer_name
        ORDER BY SUM(s.sale_amount) DESC
        LIMIT 3
    """)
    top_customers = cursor.fetchall()

    # Monthly Revenue
    cursor.execute("""
        SELECT
            DATE_FORMAT(sale_date,'%Y-%m'),
            SUM(sale_amount)
        FROM sales
        GROUP BY DATE_FORMAT(sale_date,'%Y-%m')
        ORDER BY DATE_FORMAT(sale_date,'%Y-%m')
    """)
    monthly_revenue = cursor.fetchall()

    # Customer List
    cursor.execute("""
    SELECT customer_id, customer_name, city
    FROM customers
    ORDER BY customer_id ASC
""")
    customer_list = cursor.fetchall()

    # Product List
    cursor.execute("""
        SELECT product_id, product_name
        FROM products
    """)
    product_list = cursor.fetchall()

    # Chart Data
    product_names = [row[0] for row in product_revenue]
    product_amounts = [float(row[1]) for row in product_revenue]

    months = [row[0] for row in monthly_revenue]
    month_amounts = [float(row[1]) for row in monthly_revenue]

    conn.close()

    return render_template(
        "dashboard.html",
        revenue=revenue,
        customers=customers,
        products=products,
        top_customer=top_customer,
        recent_sales=recent_sales,
        product_revenue=product_revenue,
        top_customers=top_customers,
        monthly_revenue=monthly_revenue,
        product_names=product_names,
        product_amounts=product_amounts,
        months=months,
        month_amounts=month_amounts,
        customer_list=customer_list,
        product_list=product_list
    )
@app.route("/add_customer", methods=["POST"])
def add_customer():

    name = request.form["customer_name"]
    city = request.form["city"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers (customer_name, city)
        VALUES (%s, %s)
    """, (name, city))

    conn.commit()
    cursor.close()
    conn.close()

    # ✅ IMPORTANT RETURN (fix)
    return redirect("/")

@app.route("/delete_customer/<int:id>")
def delete_customer(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        DELETE FROM customers
        WHERE customer_id = %s
    """, (id,))

    conn.commit()
    cursor.close()
    conn.close()

    # ✅ MUST RETURN
    return redirect("/")

@app.route("/edit_customer/<int:id>")
def edit_customer(id):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_id, customer_name, city
        FROM customers
        WHERE customer_id = %s
    """, (id,))

    customer = cursor.fetchone()

    cursor.close()
    conn.close()

    return render_template(
        "edit_customer.html",
        customer=customer
    )


@app.route("/update_customer/<int:id>", methods=["POST"])
def update_customer(id):

    customer_name = request.form["customer_name"]
    city = request.form["city"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE customers
        SET customer_name = %s,
            city = %s
        WHERE customer_id = %s
    """, (customer_name, city, id))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")

@app.route("/add_sale", methods=["POST"])
def add_sale():

    customer_id = request.form["customer_id"]
    product_id = request.form["product_id"]
    sale_amount = request.form["sale_amount"]
    sale_date = request.form["sale_date"]

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sales
        (customer_id, product_id, sale_amount, sale_date)
        VALUES (%s, %s, %s, %s)
    """, (customer_id, product_id, sale_amount, sale_date))

    conn.commit()

    cursor.close()
    conn.close()

    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)