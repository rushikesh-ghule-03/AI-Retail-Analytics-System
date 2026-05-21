CREATE DATABASE retail_analytics;

USE retail_analytics;

SELECT COUNT(*) FROM superstore;
SELECT * FROM superstore;

SELECT SUM(Sales) AS Total_Sales
FROM superstore;

SELECT AVG(Sales) AS Average_Sales
FROM superstore;

SELECT MAX(Sales) AS Highest_Sales
FROM superstore;

SELECT MIN(Sales) AS Lowest_Sales
FROM superstore;

SELECT 
    Category,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Category;

SELECT 
    Category,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Category;


SELECT 
    Region,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY Region;

SELECT 
    Region,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY Region;


SELECT 
    `Customer Name`,
    SUM(Sales) AS Total_Sales
FROM superstore
GROUP BY `Customer Name`
ORDER BY Total_Sales DESC
LIMIT 10;

SELECT 
    `Product Name`,
    SUM(Profit) AS Total_Profit
FROM superstore
GROUP BY `Product Name`
ORDER BY Total_Profit ASC
LIMIT 10;

SELECT 
    Discount,
    AVG(Profit) AS Average_Profit
FROM superstore
GROUP BY Discount
ORDER BY Discount;
