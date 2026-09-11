USE sprint1_db;
SELECT * FROM customers;
SELECT * FROM products WHERE price > 30000;
SELECT * FROM products ORDER BY price DESC;
SELECT category_id, COUNT(*) AS product_count FROM products GROUP BY category_id;

SELECT
    o.order_id,
    c.customer_name,
    o.total_amount
FROM orders o
INNER JOIN customers c
ON o.customer_id = c.customer_id;

SELECT
    c.customer_name,
    o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_name,
    o.order_id
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    c.customer_name,
    o.order_id
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id

UNION

SELECT
    c.customer_name,
    o.order_id
FROM customers c
RIGHT JOIN orders o
ON c.customer_id = o.customer_id;

SELECT
    product_name,
    price,
    CASE
        WHEN price >= 50000 THEN 'Expensive'
        WHEN price >= 20000 THEN 'Medium'
        ELSE 'Affordable'
    END AS price_category
FROM products;

SELECT *
FROM products
WHERE price > (
    SELECT AVG(price)
    FROM products
);

WITH customer_orders AS (
    SELECT
        customer_id,
        SUM(total_amount) AS total_spent
    FROM orders
    GROUP BY customer_id
)
SELECT *
FROM customer_orders
WHERE total_spent > 30000;

SELECT
    product_name,
    price,
    ROW_NUMBER() OVER (
        ORDER BY price DESC
    ) AS row_num
FROM products;

SELECT
    product_name,
    price,
    RANK() OVER (
        ORDER BY price DESC
    ) AS price_rank
FROM products;


SELECT
    product_name,
    price,
    DENSE_RANK() OVER (
        ORDER BY price DESC
    ) AS price_dense_rank
FROM products;

SELECT
    order_id,
    order_date,
    total_amount,
    LAG(total_amount) OVER (
        ORDER BY order_date
    ) AS previous_amount
FROM orders;

SELECT
    order_id,
    order_date,
    total_amount,
    LEAD(total_amount) OVER (
        ORDER BY order_date
    ) AS next_amount
FROM orders;

CREATE INDEX idx_product_price
ON products(price);

CREATE INDEX idx_order_customer
ON orders(customer_id);

CREATE VIEW customer_order_summary AS
SELECT
    c.customer_id,
    c.customer_name,
    COUNT(o.order_id) AS total_orders,
    SUM(o.total_amount) AS total_spent
FROM customers c
LEFT JOIN orders o
ON c.customer_id = o.customer_id
GROUP BY
    c.customer_id,
    c.customer_name;
    
SELECT *
FROM customer_order_summary;