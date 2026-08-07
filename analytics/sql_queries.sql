-- ======================================
-- Total Customers
-- ======================================

SELECT COUNT(*) AS total_customers
FROM customers;

-- ======================================
-- Total Products
-- ======================================

SELECT COUNT(*) AS total_products
FROM products;

-- ======================================
-- Total Orders
-- ======================================

SELECT COUNT(*) AS total_orders
FROM orders;

-- ======================================
-- Total Revenue
-- ======================================

SELECT SUM(total_amount) AS total_revenue
FROM orders;

-- ======================================
-- Average Order Value
-- ======================================

SELECT ROUND(AVG(total_amount),2) AS average_order_value
FROM orders;

-- ======================================
-- Highest Order Value
-- ======================================

SELECT MAX(total_amount) AS highest_order
FROM orders;

-- ======================================
-- Lowest Order Value
-- ======================================

SELECT MIN(total_amount) AS lowest_order
FROM orders;

-- ======================================
-- Order Status Distribution
-- ======================================

SELECT
order_status,
COUNT(*) AS total_orders
FROM orders
GROUP BY order_status
ORDER BY total_orders DESC;

-- ======================================
-- Top 10 Customers
-- ======================================

SELECT
customer_id,
COUNT(*) AS total_orders
FROM orders
GROUP BY customer_id
ORDER BY total_orders DESC
LIMIT 10;

-- ======================================
-- Top 10 Products
-- ======================================

SELECT
product_id,
COUNT(*) AS total_sales
FROM orders
GROUP BY product_id
ORDER BY total_sales DESC
LIMIT 10;