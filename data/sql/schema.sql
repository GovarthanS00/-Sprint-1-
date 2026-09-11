CREATE DATABASE sprint1_db;

USE sprint1_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_name VARCHAR(100) NOT NULL,
    city VARCHAR(50),
    email VARCHAR(100) UNIQUE
);

CREATE TABLE categories (
    category_id INT PRIMARY KEY AUTO_INCREMENT,
    category_name VARCHAR(100) NOT NULL
);

CREATE TABLE products (
    product_id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100) NOT NULL,
    category_id INT,
    price DECIMAL(10,2) NOT NULL,
    stock INT DEFAULT 0,
    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY AUTO_INCREMENT,
    customer_id INT,
    order_date DATE,
    total_amount DECIMAL(10,2),
    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
);

CREATE TABLE order_items (
    item_id INT PRIMARY KEY AUTO_INCREMENT,
    order_id INT,
    product_id INT,
    quantity INT NOT NULL,
    price DECIMAL(10,2),
    FOREIGN KEY (order_id)
        REFERENCES orders(order_id),
    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
);

INSERT INTO customers
(customer_name, city, email)
VALUES
('Arun', 'Chennai', 'arun@gmail.com'),
('Kumar', 'Coimbatore', 'kumar@gmail.com'),
('Ravi', 'Salem', 'ravi@gmail.com'),
('Priya', 'Chennai', 'priya@gmail.com'),
('Divya', 'Bangalore', 'divya@gmail.com');

INSERT INTO categories
(category_name)
VALUES
('Laptop'),
('Mobile'),
('Accessories');

INSERT INTO products
(product_name, category_id, price, stock)
VALUES
('Dell Laptop', 1, 55000, 10),
('HP Laptop', 1, 60000, 8),
('iPhone', 2, 70000, 15),
('Samsung Mobile', 2, 30000, 20),
('Keyboard', 3, 1500, 50),
('Mouse', 3, 800, 100);

INSERT INTO orders
(customer_id, order_date, total_amount)
VALUES
(1, '2026-09-01', 55000),
(2, '2026-09-02', 70000),
(3, '2026-09-03', 30000),
(4, '2026-09-04', 1500),
(5, '2026-09-05', 60000);

INSERT INTO order_items
(order_id, product_id, quantity, price)
VALUES
(1, 1, 1, 55000),
(2, 3, 1, 70000),
(3, 4, 1, 30000),
(4, 5, 1, 1500),
(5, 2, 1, 60000);




SELECT * FROM customers;
SELECT * FROM categories;
SELECT * FROM products;
SELECT * FROM orders;

SELECT * FROM order_items;