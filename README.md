📊 Sales Analytics Dashboard

A full-stack Sales Analytics Dashboard built using Flask, MySQL, HTML, CSS, and Chart.js.
This project visualizes business sales data with KPIs, charts, and tables, and helps analyze customer and product performance in real time.

✨ Features

📊 Dashboard KPIs

Total Revenue
Total Customers
Total Products
Top Customer

🧾 Sales Management

View recent sales transactions
Track customer purchases
Monitor product sales

👥 Customer Analytics

Top customers list
Customer-wise revenue breakdown

📦 Product Analytics

Product-wise revenue tracking
Performance comparison

📅 Time-based Analysis

Monthly revenue trends
Business growth tracking

📈 Interactive Charts

Bar chart for product revenue
Line chart for monthly revenue

🗄️ Database Integration

MySQL relational database
Real-time query execution using Flask

🛠️ Tech Stack

Backend:
Python (Flask)
MySQL Connector

Frontend:
HTML5
CSS3
Jinja2 Templates

Visualization:
Chart.js

Database:
MySQL

📂 Project Structure
sales-analytics-dashboard/
│
├── app.py
├── templates/
│   ├── dashboard.html
│   └── edit_customer.html
│
├── static/
│   └── style.css
│
└── README.md

🚀 How It Works
Flask connects to MySQL database
Queries fetch sales, customer, product data
Data is processed in Python
Jinja2 renders HTML dashboard
Chart.js visualizes analytics

⚙️ Setup Instructions
# 1. Clone repo
git clone https://github.com/0911anjalinadi/sales-analytics-dashboard.git

# 2. Install dependencies
pip install flask mysql-connector-python gunicorn

# 3. Run app
python app.py

🌟 Project Preview
<img width="1656" height="1017" alt="Screenshot 2026-06-20 122037" src="https://github.com/user-attachments/assets/431ef84c-7f72-464d-b145-0abb38d2593f" />

<img width="1573" height="976" alt="Screenshot 2026-06-20 122057" src="https://github.com/user-attachments/assets/601fba16-194c-4582-af98-e67b4e5180d2" />

<img width="1566" height="838" alt="Screenshot 2026-06-20 122115" src="https://github.com/user-attachments/assets/054f3729-82e1-4111-b2cf-f541a2559203" />

<img width="1552" height="1020" alt="Screenshot 2026-06-20 122131" src="https://github.com/user-attachments/assets/8ef915d7-fb98-41cb-b639-2a4168edb5f0" />

<img width="1567" height="647" alt="Screenshot 2026-06-20 122143" src="https://github.com/user-attachments/assets/6f848759-7759-42dd-80bd-6d8f6a991de3" />

📊 Example Queries Used
SELECT SUM(sale_amount) FROM sales;

SELECT c.customer_name, SUM(s.sale_amount)
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_name;

💡 Future Improvements
Add login authentication
Add search + filter system
Export reports (PDF/Excel)
Role-based admin panel
Cloud database integration
GROUP BY c.customer_name;

