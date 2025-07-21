# 📦 Product Inventory SQL Project

Welcome to the **Product Inventory Database** project!  
This repository features a complete SQL solution for creating and managing an inventory database — ideal for aspiring data analysts, developers, and learners.

---

## 🚀 Project Overview

This project demonstrates:

- ✅ How to create a product inventory database
- ✅ Writing and executing SQL scripts
- ✅ Populating large datasets with real-world attributes
- ✅ Performing analysis-ready database design

---

## 📂 Files Included

| File Name     | Description                                                   |
|---------------|---------------------------------------------------------------|
| `Products.sql`| SQL script that creates a database and populates sample data  |

---

## 🎯 Project Goals

- 🧠 Understand relational database design  
- 🧾 Practice DDL (Data Definition Language) and DML (Data Manipulation Language)  
- 🔎 Explore how product data can be queried

---

## 💡 Sample SQL Queries

```sql
-- Get top 5 most expensive products
SELECT Product_Name, Price 
FROM products 
ORDER BY Price DESC 
LIMIT 5;

-- Count of products per category
SELECT Product_Category, COUNT(*) 
FROM products 
GROUP BY Product_Category;

-- Average rating by category
SELECT Product_Category, AVG(Product_Ratings) AS Avg_Rating 
FROM products 
GROUP BY Product_Category;
