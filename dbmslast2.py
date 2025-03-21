'''

-- Create the trading_platform database
CREATE DATABASE IF NOT EXISTS trading_platform;

-- Switch to the trading_platform database
USE trading_platform;
drop database trading_platform;
-- Create User table
CREATE TABLE IF NOT EXISTS User (
    User_ID INT AUTO_INCREMENT PRIMARY KEY,
    Username VARCHAR(50) NOT NULL UNIQUE,
    Password VARCHAR(50) NOT NULL,
    Phone_No VARCHAR(15),
    Email VARCHAR(255),
    PAN_No VARCHAR(15),
    Bank_Account_No VARCHAR(20)
);

-- Create BankTransaction table
CREATE TABLE IF NOT EXISTS BankTransaction (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT,
    Transaction_Type VARCHAR(50),
    Amount DECIMAL(10, 2),
    Date_Time DATETIME,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
);

-- Create Stock table
CREATE TABLE IF NOT EXISTS Stock (
    Stock_ID INT AUTO_INCREMENT PRIMARY KEY,
    Stock_Name VARCHAR(255),
    Current_Price DECIMAL(10, 2)
);

-- Create Portfolio table
CREATE TABLE IF NOT EXISTS Portfolio (
    Portfolio_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT,
    Stock_ID INT,
    Quantity INT,
    Buy_Price DECIMAL(10, 2),
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Stock_ID) REFERENCES Stock(Stock_ID)
);

-- Create ShareTransaction table
CREATE TABLE IF NOT EXISTS ShareTransaction (
    Transaction_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT,
    Stock_ID INT,
    Transaction_Type VARCHAR(50),
    Quantity INT,
    Order_Type VARCHAR(50),
    Price DECIMAL(10, 2),
    Date_Time DATETIME,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Stock_ID) REFERENCES Stock(Stock_ID)
);

-- Create Watchlist table
CREATE TABLE IF NOT EXISTS Watchlist (
    Watchlist_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT,
    Stock_ID INT,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Stock_ID) REFERENCES Stock(Stock_ID)
);

-- Create CurrentPrices table
CREATE TABLE IF NOT EXISTS CurrentPrices (
    CurrentPrices_ID INT AUTO_INCREMENT PRIMARY KEY,
    Stock_ID INT,
    Price DECIMAL(10, 2),
	Date_Time DATETIME,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Stock_ID) REFERENCES Stock(Stock_ID)
);

-- Create Order table
CREATE TABLE IF NOT EXISTS `Order` (
    Order_ID INT AUTO_INCREMENT PRIMARY KEY,
    User_ID INT,
    Stock_ID INT,
    Order_Type VARCHAR(50),
    Quantity INT,
    Price_Per_Unit DECIMAL(10, 2),
    Date_Time DATETIME,
    FOREIGN KEY (User_ID) REFERENCES User(User_ID),
    FOREIGN KEY (Stock_ID) REFERENCES Stock(Stock_ID)
);

-- Insert sample data into the User table
INSERT INTO User (Username, Password, Phone_No, Email, PAN_No, Bank_Account_No)
VALUES
    ('kumarpal362', 'kumar123', '6354587009', 'Kumarpal.vce22@sot.pdpu.ac.in', 'ABCDE1234F', '1234567890123456'),
    ('dev_patel', 'dev456', '8200405029', 'Dev.pce22@sot.pdpu.ac.in', 'FGHIJ5678K', '2345678901234567'),
    ('dhruvin_kadivar', 'dhruvin789', '7984205409', 'Dhruvin.kce22@sot.pdpu.ac.in', 'KLMNO9012L', '3456789012345678'),
    ('yash_mavani', 'yash2222', '7715930103', 'Yash.mce2222@sot.pdpu.ac.in', 'PQRST3456M', '4567890123456789');

-- Insert sample data into the Stock table
INSERT INTO Stock (Stock_Name, Current_Price)
VALUES
    ('COALINDIA', 456.35),
    ('HAL', 3565.40),
    ('BEL', 228.75),
    ('ADANIENT', 3242),
    ('HDFCBANK', 1536.35),
    ('HINDCOPPER', 357.85),
    ('IOC', 172.80),
    ('ADANIGREEN', 1907.50),
    ('NBCC', 136.40),
    ('STLTECH', 140.35),
    ('TATAPOWER', 431.95),
    ('ADANIPOWER', 617.90),
    ('RELIANCE', 2959.15),
    ('BAJFINANCE', 7230.25),
    ('ITC', 436.95),
    ('VEDANTA', 361.80),
    ('INFOSYS', 1506.80),
    ('TCS', 3984.65);

-- Insert sample data into the BankTransaction table for Kumarpal Vakharia
INSERT INTO BankTransaction (User_ID, Transaction_Type, Amount, Date_Time)
VALUES
    (1, 'Deposit', 10000.00, '2023-01-15 10:30:00'),
    (1, 'Withdrawal', 5000.00, '2023-02-10 14:45:00'),
    (1, 'Deposit', 8000.00, '2023-03-05 09:15:00');

-- Insert sample data into the BankTransaction table for Dev Patel
INSERT INTO BankTransaction (User_ID, Transaction_Type, Amount, Date_Time)
VALUES
    (2, 'Deposit', 5000.00, '2023-01-20 11:00:00'),
    (2, 'Withdrawal', 2000.00, '2023-02-15 13:30:00'),
    (2, 'Withdrawal', 1500.00, '2023-03-20 10:45:00');

-- Insert sample data into the BankTransaction table for Dhruvin Kadivar
INSERT INTO BankTransaction (User_ID, Transaction_Type, Amount, Date_Time)
VALUES
    (3, 'Deposit', 12000.00, '2023-01-25 08:45:00'),
    (3, 'Withdrawal', 3000.00, '2023-02-18 15:00:00'),
    (3, 'Deposit', 5000.00, '2023-03-30 12:30:00');

-- Insert sample data into the BankTransaction table for Yash Mavani
INSERT INTO BankTransaction (User_ID, Transaction_Type, Amount, Date_Time)
VALUES
    (4, 'Deposit', 7000.00, '2023-01-10 09:00:00'),
    (4, 'Withdrawal', 2500.00, '2023-02-22 11:20:00'),
    (4, 'Deposit', 9000.00, '2023-03-15 14:10:00');

-- Insert sample data into the Portfolio table for Kumarpal Vakharia
INSERT INTO Portfolio (User_ID, Stock_ID, Quantity, Buy_Price)
VALUES
    (1, 1, 20, 450.00),
    (1, 4, 15, 3200.00),
    (1, 8, 10, 1800.00);

-- Insert sample data into the Portfolio table for Dev Patel
INSERT INTO Portfolio (User_ID, Stock_ID, Quantity, Buy_Price)
VALUES
    (2, 2, 5, 3550.00),
    (2, 5, 8, 1500.00),
    (2, 10, 12, 425.00);

-- Insert sample data into the Portfolio table for Dhruvin Kadivar
INSERT INTO Portfolio (User_ID, Stock_ID, Quantity, Buy_Price)
VALUES
    (3, 3, 25, 235.00),
    (3, 6, 18, 340.00),
    (3, 11, 15, 415.00);

-- Insert sample data into the Portfolio table for Yash Mavani
INSERT INTO Portfolio (User_ID, Stock_ID, Quantity, Buy_Price)
VALUES
    (4, 7, 30, 175.00),
    (4, 9, 20, 130.00),
    (4, 12, 10, 600.00);

-- Insert sample data into the ShareTransaction table for Kumarpal Vakharia
INSERT INTO ShareTransaction (User_ID, Stock_ID, Transaction_Type, Quantity, Order_Type, Price, Date_Time)
VALUES
    (1, 1, 'Buy', 10, 'Market', 455.25, '2023-01-18 09:30:00'),
    (1, 4, 'Sell', 5, 'Limit', 3150.00, '2023-02-12 11:45:00'),
    (1, 8, 'Buy', 8, 'Stop Loss', 1850.00, '2023-03-08 14:20:00');

-- Insert sample data into the ShareTransaction table for Dev Patel
INSERT INTO ShareTransaction (User_ID, Stock_ID, Transaction_Type, Quantity, Order_Type, Price, Date_Time)
VALUES
    (2, 2, 'Buy', 3, 'Market', 3570.75, '2023-01-23 10:15:00'),
    (2, 5, 'Buy', 5, 'Limit', 1535.50, '2023-02-18 13:00:00'),
    (2, 10, 'Sell', 8, 'Market', 440.20, '2023-03-12 15:30:00');

-- Insert sample data into the ShareTransaction table for Dhruvin Kadivar
INSERT INTO ShareTransaction (User_ID, Stock_ID, Transaction_Type, Quantity, Order_Type, Price, Date_Time)
VALUES
    (3, 3, 'Buy', 15, 'Market', 240.50, '2023-01-28 08:00:00'),
    (3, 6, 'Sell', 10, 'Limit', 360.80, '2023-02-22 10:45:00'),
    (3, 11, 'Buy', 5, 'Market', 420.75, '2023-03-18 12:00:00');

-- Insert sample data into the ShareTransaction table for Yash Mavani
INSERT INTO ShareTransaction (User_ID, Stock_ID, Transaction_Type, Quantity, Order_Type, Price, Date_Time)
VALUES
    (4, 7, 'Buy', 20, 'Limit', 178.40, '2023-01-15 11:30:00'),
    (4, 9, 'Sell', 10, 'Market', 125.60, '2023-02-28 14:15:00'),
    (4, 12, 'Buy', 5, 'Limit', 605.25, '2023-03-25 09:45:00');

-- Insert sample data into the Watchlist table for Kumarpal Vakharia
INSERT INTO Watchlist (User_ID, Stock_ID)
VALUES
    (1, 2),
    (1, 5),
    (1, 9);

-- Insert sample data into the Watchlist table for Dev Patel
INSERT INTO Watchlist (User_ID, Stock_ID)
VALUES
    (2, 1),
    (2, 3),
    (2, 10);

-- Insert sample data into the Watchlist table for Dhruvin Kadivar
INSERT INTO Watchlist (User_ID, Stock_ID)
VALUES
    (3, 4),
    (3, 7),
    (3, 11);

-- Insert sample data into the Watchlist table for Yash Mavani
INSERT INTO Watchlist (User_ID, Stock_ID)
VALUES
    (4, 8),
    (4, 12),
    (4, 16);



-- Create the trading_platform database
CREATE DATABASE IF NOT EXISTS trading_platform;

-- Switch to the trading_platform database
USE trading_platform;

CREATE TABLE IF NOT EXISTS CurrentPrices (
    CurrentPrices_ID INT AUTO_INCREMENT PRIMARY KEY,
    Stock_ID INT,
    Price DECIMAL(10, 2),
    Date_Time DATETIME,
    FOREIGN KEY (Stock_ID) REFERENCES Stock(Stock_ID)
);


INSERT INTO CurrentPrices (Stock_ID, Price, Date_Time)
VALUES
    (1, 456.35, NOW()),     -- COALINDIA
    (2, 3565.40, NOW()),    -- HAL
    (3, 228.75, NOW()),     -- BEL
    (4, 3242, NOW()),       -- ADANIENT
    (5, 1536.35, NOW()),    -- HDFCBANK
    (6, 357.85, NOW()),     -- HINDCOPPER
    (7, 172.80, NOW()),     -- IOC
    (8, 1907.50, NOW()),    -- ADANIGREEN
    (9, 136.40, NOW()),     -- NBCC
    (10, 140.35, NOW()),    -- STLTECH
    (11, 431.95, NOW()),    -- TATAPOWER
    (12, 617.90, NOW()),    -- ADANIPOWER
    (13, 2959.15, NOW()),   -- RELIANCE
    (14, 7230.25, NOW()),   -- BAJFINANCE
    (15, 436.95, NOW()),    -- ITC
    (16, 361.80, NOW()),    -- VEDANTA
    (17, 1506.80, NOW()),   -- INFOSYS
    (18, 3984.65, NOW());   -- TCS




    USE trading_platform;

SET SQL_SAFE_UPDATES = 0;

UPDATE CurrentPrices
SET Price = 
    CASE 
        WHEN Stock_ID = 1 THEN 475.50    -- COALINDIA
        WHEN Stock_ID = 2 THEN 3521.75   -- HAL
        WHEN Stock_ID = 3 THEN 219.25    -- BEL
        WHEN Stock_ID = 4 THEN 3085.60   -- ADANIENT
        WHEN Stock_ID = 5 THEN 1550.80   -- HDFCBANK
        WHEN Stock_ID = 6 THEN 330.20    -- HINDCOPPER
        WHEN Stock_ID = 7 THEN 175.30    -- IOC
        WHEN Stock_ID = 8 THEN 1875.35   -- ADANIGREEN
        WHEN Stock_ID = 9 THEN 138.50    -- NBCC
        WHEN Stock_ID = 10 THEN 132.80   -- STLTECH
        WHEN Stock_ID = 11 THEN 423.20   -- TATAPOWER
        WHEN Stock_ID = 12 THEN 598.40   -- ADANIPOWER
        WHEN Stock_ID = 13 THEN 2985.35  -- RELIANCE
        WHEN Stock_ID = 14 THEN 7219.10  -- BAJFINANCE
        WHEN Stock_ID = 15 THEN 427.75   -- ITC
        WHEN Stock_ID = 16 THEN 364.90   -- VEDANTA
        WHEN Stock_ID = 17 THEN 1480.25  -- INFOSYS
        WHEN Stock_ID = 18 THEN 3949.20  -- TCS
    END;



-- Create the trading_platform database
CREATE DATABASE IF NOT EXISTS trading_platform;

-- Switch to the trading_platform database
USE trading_platform;
show tables;


ALTER TABLE User
ADD COLUMN Name VARCHAR(255);
select * from user;






USE trading_platform;
UPDATE User
SET Name = 'Kumarpal Vakharia'  -- Replace 'Kumarpal' with the correct name for each user
WHERE User_ID = 1;  -- Replace '1' with the appropriate User_ID for each user

UPDATE User
SET Name = 'Dev Patel'  
WHERE User_ID = 2;  

UPDATE User
SET Name = 'Yash Malavi'  
WHERE User_ID = 4;

UPDATE User
SET Name = 'Dhruvin'  
WHERE User_ID = 3;




USE trading_platform;
INSERT INTO BankTransaction (User_ID, Transaction_Type, Amount, Date_Time)
VALUES
    (5, 'Deposit', 4000.00, '2023-03-10 09:00:00'),
    (5, 'Withdrawal', 2500.00, '2023-02-22 11:20:00');



USE trading_platform;
CREATE TABLE DemandAccount (
    User_ID INT NOT NULL,
    Balance DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (User_ID),
    FOREIGN KEY (User_ID) REFERENCES User(User_ID)
);


USE trading_platform;

INSERT INTO Stock (Stock_Name, Current_Price)
VALUES
    ('COALINDIA', 456.35),
    ('HAL', 3565.40),
    ('BEL', 228.75),
    ('ADANIENT', 3242),
    ('HDFCBANK', 1536.35),
    ('HINDCOPPER', 357.85),
    ('IOC', 172.80),
    ('ADANIGREEN', 1907.50),
    ('NBCC', 136.40),
    ('STLTECH', 140.35),
    ('TATAPOWER', 431.95),
    ('ADANIPOWER', 617.90),
    ('RELIANCE', 2959.15),
    ('BAJFINANCE', 7230.25),
    ('ITC', 436.95),
    ('VEDANTA', 361.80),
    ('INFOSYS', 1506.80),
    ('TCS', 3984.65);




USE trading_platform;
UPDATE CurrentPrices AS cp
JOIN (
    SELECT 
        s.Stock_ID,
        ROUND((s.Current_Price * (1 + RAND() * 0.1 - 0.05)), 2) AS new_price
    FROM Stock AS s
) AS new_prices ON cp.Stock_ID = new_prices.Stock_ID
SET cp.Price = new_prices.new_price,
    cp.Date_Time = NOW();


CREATE DATABASE IF NOT EXISTS login_system;

USE login_system;

CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password) VALUES ('user1', '1234');
INSERT INTO users (username, password) VALUES ('kp', '1234');


CREATE DATABASE IF NOT EXISTS login_system;

USE login_system;

CREATE TABLE users (
    id INT(11) AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL
);

INSERT INTO users (username, password) VALUES ('user1', '1234');
INSERT INTO users (username, password) VALUES ('kp', '1234');
INSERT INTO users (username, password) VALUES ('dev', '12345678');

SELECT * FROM users
'''



import mysql.connector
from mysql.connector import Error
from decimal import Decimal, ROUND_HALF_UP

# Establishing the database connection
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="kumarpal",
            database="trading_platform"
        )
        return connection
    except Error as e:
        print("Error connecting to database:", e)
        return None

# Function to get total investment for a user
def get_total_investment(user_id):
    total_investment_query = """
        SELECT SUM(p.Quantity * s.Current_Price)
        FROM Portfolio p
        JOIN Stock s ON p.Stock_ID = s.Stock_ID
        WHERE p.User_ID = %s
    """
    cursor.execute(total_investment_query, (user_id,))
    total_investment = cursor.fetchone()[0] or Decimal(0)

    return total_investment

# Function to show investment stocks
def show_investment_stocks(user_id):
    investment_stocks_query = """
        SELECT s.Stock_ID, s.Stock_Name, s.Current_Price, IFNULL(SUM(p.Quantity), 0) AS Quantity
        FROM Stock s
        LEFT JOIN Portfolio p ON s.Stock_ID = p.Stock_ID AND p.User_ID = %s
        GROUP BY s.Stock_ID, s.Stock_Name, s.Current_Price
    """
    cursor.execute(investment_stocks_query, (user_id,))
    investment_stocks = cursor.fetchall()

    print("\nInvestment Stocks")
    print("Stock ID | Stock Name | Current Price | Quantity")
    print("-" * 50)
    for stock in investment_stocks:
        stock_id, stock_name, current_price, quantity = stock
        print(f"{stock_id:<9} | {stock_name:<11} | {current_price:<13} | {quantity:<8}")

    total_investment = get_total_investment(user_id)
    print("\nTotal Investment:", total_investment)

def show_portfolio(user_id):
    portfolio_query = """
        SELECT p.Stock_ID, s.Stock_Name, 
               SUM(p.Quantity) AS Quantity, 
               AVG(p.Buy_Price) AS Avg_Buy_Price,
               cp.Price AS Current_Price
        FROM Portfolio p
        JOIN Stock s ON p.Stock_ID = s.Stock_ID
        JOIN CurrentPrices cp ON p.Stock_ID = cp.Stock_ID
        WHERE p.User_ID = %s
        GROUP BY p.Stock_ID, s.Stock_Name, cp.Price
    """
    cursor.execute(portfolio_query, (user_id,))
    portfolio = cursor.fetchall()

    total_investment = get_total_investment(user_id)

    print("\nPortfolio with Profit/Loss based on Current Price and Average Buy Price")
    print("Stock Name | Quantity | Avg Buy Price | Current Price | Profit/Loss (Amount) | Profit/Loss (%)")
    print("-" * 130)
    total_profit_loss = 0
    for stock in portfolio:
        stock_id, stock_name, quantity, avg_buy_price, current_price = stock
        profit_loss_amount = (current_price - avg_buy_price) * quantity
        profit_loss_percentage = (profit_loss_amount / (avg_buy_price * quantity)) * 100 if avg_buy_price != 0 else 0
        total_profit_loss += profit_loss_amount
        print(f"{stock_name:<11} | {quantity:<8} | {avg_buy_price:<13.2f} | {current_price:<13} | "
              f"{profit_loss_amount:<21.2f} | {profit_loss_percentage:.2f}%")

    total_profit_loss_percentage = (total_profit_loss / total_investment) * 100 if total_investment != 0 else 0
    print("-" * 130)
    print("Total Profit/Loss (Amount):", round(total_profit_loss, 2))
    print("Total Profit/Loss (%):", round(total_profit_loss_percentage, 2))

def calculate_demand_balance(user_id):
    try:
        # Query to get the sum of 'Deposit' transactions
        deposit_query = "SELECT SUM(Amount) FROM BankTransaction WHERE User_ID = %s AND Transaction_Type = 'Deposit'"

        # Query to get the sum of 'Withdrawal' transactions
        withdrawal_query = "SELECT SUM(Amount) FROM BankTransaction WHERE User_ID = %s AND Transaction_Type = 'Withdrawal'"

        # Execute the queries
        cursor.execute(deposit_query, (user_id,))
        deposit_sum = cursor.fetchone()[0] or Decimal(0)

        cursor.execute(withdrawal_query, (user_id,))
        withdrawal_sum = cursor.fetchone()[0] or Decimal(0)

        # Calculate the demand balance
        demand_balance = deposit_sum - withdrawal_sum

        return demand_balance

    except Error as e:
        print("Error calculating demand account balance:", e)
        return None

# Function to add stock to portfolio
def add_stock_to_portfolio(user_id):
    try:
        stock_id = int(input("Enter Stock ID to add to your portfolio: "))
        quantity = int(input("Enter Quantity to purchase: "))

        # Get the current price of the stock
        stock_price_query = "SELECT Current_Price FROM Stock WHERE Stock_ID = %s"
        cursor.execute(stock_price_query, (stock_id,))
        current_price = cursor.fetchone()[0]

        total_price = current_price * quantity

        # Get the demand account balance
        demand_balance = calculate_demand_balance(user_id)

        if demand_balance is not None:
            if demand_balance >= total_price:
                # Update the demand account balance
                new_demand_balance = demand_balance - total_price
                update_demand_balance_query = "UPDATE DemandAccount SET Balance = %s WHERE User_ID = %s"
                cursor.execute(update_demand_balance_query, (new_demand_balance, user_id))
                connection.commit()


        if demand_balance >= total_price:
            # Add the stock to the portfolio
            add_portfolio_query = "INSERT INTO Portfolio (User_ID, Stock_ID, Quantity, Buy_Price) VALUES (%s, %s, %s, %s)"
            cursor.execute(add_portfolio_query, (user_id, stock_id, quantity, current_price))
            connection.commit()

            print("Stock added to portfolio successfully.")
            print("Updated Demand Account Balance:", new_demand_balance)

            # Insert data into ShareTransaction table
            insert_share_transaction_query = """
            INSERT INTO ShareTransaction (User_ID, Stock_ID, Transaction_Type, Quantity, Order_Type, Price, Date_Time)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
            """
            cursor.execute(insert_share_transaction_query, (user_id, stock_id, 'Buy', quantity, 'Market', current_price))
            connection.commit()
        else:
            print("Insufficient balance in your demand account.")

    except ValueError:
        print("Invalid input. Please enter valid Stock ID and Quantity.")

def sell_stock_from_portfolio(user_id):
    try:
        stock_id = int(input("Enter Stock ID to sell from your portfolio: "))
        quantity_to_sell = int(input("Enter Quantity to sell: "))

        # Check if the stock is in the user's portfolio and get the quantity and buy price
        stock_details_query = "SELECT Portfolio_ID, Quantity, Buy_Price FROM Portfolio WHERE Stock_ID = %s AND User_ID = %s"
        cursor.execute(stock_details_query, (stock_id, user_id))
        stock_details = cursor.fetchall()

        if not stock_details:
            print("Stock ID not found in your portfolio.")
            return

        total_quantity = sum(detail[1] for detail in stock_details)
        if quantity_to_sell > total_quantity:
            print("Insufficient quantity in your portfolio.")
            return

        # Calculate the selling price based on the average buy price
        total_buy_price = sum(detail[1] * detail[2] for detail in stock_details)
        average_buy_price = total_buy_price / total_quantity

        # Get the current price of the stock
        stock_price_query = "SELECT Current_Price FROM Stock WHERE Stock_ID = %s"
        cursor.execute(stock_price_query, (stock_id,))
        current_price = cursor.fetchone()[0]

        total_sell_price = current_price * quantity_to_sell

        # Remove the sold stocks from the portfolio
        remaining_quantity = quantity_to_sell
        for detail in stock_details:
            portfolio_id = detail[0]
            quantity = detail[1]

            if quantity <= remaining_quantity:
                # Remove the entire stock from the portfolio
                remove_portfolio_query = "DELETE FROM Portfolio WHERE Portfolio_ID = %s"
                cursor.execute(remove_portfolio_query, (portfolio_id,))
                remaining_quantity -= quantity
            else:
                # Update the quantity of the stock in the portfolio
                remaining_quantity -= quantity_to_sell
                update_portfolio_query = "UPDATE Portfolio SET Quantity = %s WHERE Portfolio_ID = %s"
                cursor.execute(update_portfolio_query, (quantity - quantity_to_sell, portfolio_id))
                break

            connection.commit()

        # Get the demand account balance
        demand_balance = calculate_demand_balance(user_id)

        if demand_balance is not None:
            # Update the demand account balance
            new_demand_balance = demand_balance + total_sell_price
            update_demand_balance_query = "UPDATE DemandAccount SET Balance = %s WHERE User_ID = %s"
            cursor.execute(update_demand_balance_query, (new_demand_balance, user_id))
            connection.commit()

            # Insert data into ShareTransaction table
            insert_share_transaction_query = """
            INSERT INTO ShareTransaction (User_ID, Stock_ID, Transaction_Type, Quantity, Order_Type, Price, Date_Time)
            VALUES (%s, %s, %s, %s, %s, %s, NOW())
            """
            cursor.execute(insert_share_transaction_query, (user_id, stock_id, 'Sell', quantity_to_sell, 'Market', current_price))
            connection.commit()

            print("Stock sold from portfolio successfully.")
            print("Updated Demand Account Balance:", new_demand_balance)

    except ValueError:
        print("Invalid input. Please enter valid stock ID and quantity.")

# Function to show share transactions
def show_share_transactions(user_id):
    query = """
    SELECT Stock_ID, Transaction_Type, Quantity, Order_Type, Price, Date_Time
    FROM ShareTransaction
    WHERE User_ID = %s
    """
    cursor.execute(query, (user_id,))
    transactions = cursor.fetchall()

    if transactions:
        print("\nShare Transactions")
        print("Stock ID | Transaction Type | Quantity | Order Type | Price | Date Time")
        print("-" * 70)
        for transaction in transactions:
            print(f"{transaction[0]:<9} | {transaction[1]:<17} | {transaction[2]:<8} | {transaction[3]:<10} | {transaction[4]:<6} | {transaction[5]}")
    else:
        print("\nNo share transactions found.")

    user_menu(user_id)

# Function to show bank transactions
def show_bank_transactions(user_id):
    query = """
    SELECT Transaction_Type, Amount, Date_Time
    FROM BankTransaction
    WHERE User_ID = %s
    """
    cursor.execute(query, (user_id,))
    transactions = cursor.fetchall()

    if transactions:
        print("\nBank Transactions")
        print("Transaction Type | Amount | Date Time")
        print("-" * 50)
        for transaction in transactions:
            print(f"{transaction[0]:<17} | {transaction[1]:<6} | {transaction[2]}")
    else:
        print("\nNo bank transactions found.")

    user_menu(user_id)

import datetime

# Function to deposit money into demand account
def deposit_money(user_id, amount):
    try:
        # Update the demand account balance
        demand_balance = calculate_demand_balance(user_id)

        if demand_balance is not None:
            new_demand_balance = demand_balance + amount
            update_demand_balance_query = "UPDATE DemandAccount SET Balance = %s WHERE User_ID = %s"
            cursor.execute(update_demand_balance_query, (new_demand_balance, user_id))
            connection.commit()

            # Insert the transaction into the BankTransaction table with current date and time
            insert_transaction_query = """
                INSERT INTO BankTransaction (User_ID, Transaction_Type, Amount, Date_Time)
                VALUES (%s, %s, %s, NOW())
            """
            cursor.execute(insert_transaction_query, (user_id, 'Deposit', amount))
            connection.commit()

            print("Money deposited into demand account successfully.")
            print("Updated Demand Account Balance:", new_demand_balance)
        else:
            print("Error occurred while depositing money.")

    except Error as e:
        print("Error depositing money:", e)

# Function to withdraw money from demand account
def withdraw_money(user_id, amount):
    try:
        # Update the demand account balance
        demand_balance = calculate_demand_balance(user_id)

        if demand_balance is not None and demand_balance >= amount:
            new_demand_balance = demand_balance - amount
            update_demand_balance_query = "UPDATE DemandAccount SET Balance = %s WHERE User_ID = %s"
            cursor.execute(update_demand_balance_query, (new_demand_balance, user_id))
            connection.commit()

            # Insert the transaction into the BankTransaction table with current date and time
            insert_transaction_query = """
                INSERT INTO BankTransaction (User_ID, Transaction_Type, Amount, Date_Time)
                VALUES (%s, %s, %s, NOW())
            """
            cursor.execute(insert_transaction_query, (user_id, 'Withdrawal', amount))
            connection.commit()

            print("Money withdrawn from demand account successfully.")
            print("Updated Demand Account Balance:", new_demand_balance)
        else:
            print("Insufficient balance in the demand account.")

    except Error as e:
        print("Error withdrawing money:", e)

# Function for user login
def login():
    try:
        username = input("Enter your Username: ")
        password = input("Enter your Password: ")

        login_query = "SELECT User_ID FROM User WHERE Username = %s AND Password = %s"
        cursor.execute(login_query, (username, password))
        result = cursor.fetchone()

        if result:
            print("Login successful!")
            user_menu(result[0])
        else:
            print("Invalid username or password. Please try again.")

    except Error as e:
        print("Error:", e)

# Function to create new user account
def create_user():
    print("\nCreate New Account")
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    name = input("Enter Name: ")
    phone_no = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    pan_no = input("Enter PAN Number: ")
    bank_account_no = input("Enter Bank Account Number: ")

    try:
        connection = connect_to_database()
        cursor = connection.cursor()

        create_user_query = """
        INSERT INTO User (Username, Password, Name, Phone_No, Email, PAN_No, Bank_Account_No)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(create_user_query, (username, password, name, phone_no, email, pan_no, bank_account_no))

        connection.commit()
        print("New account created successfully!")

    except Error as e:
        print("Error creating new account:", e)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Main function to display user menu
def user_menu(user_id):
    # sp.Popen("cls", shell=True)
    while True:
        print("\nUser Menu")
        print("1. See Investment Stocks")
        print("2. See Portfolio")
        print("3. Add Stock to Portfolio")
        print("4. Sell Stock from Portfolio")
        print("5. See Transactions (Shares)")
        print("6. See Transactions (Bank)")
        print("7. Calculate Demand Account Balance")
        print("8. Deposit Money into Demand Account")
        print("9. Withdraw Money from Demand Account")
        print("10. Logout")

        choice = input("Enter your choice (1-10): ")

        if choice == '1':
            show_investment_stocks(user_id)
        elif choice == '2':
            show_portfolio(user_id)
        elif choice == '3':
            add_stock_to_portfolio(user_id)
        elif choice == '4':
            sell_stock_from_portfolio(user_id)
        elif choice == '5':
            show_share_transactions(user_id)
        elif choice == '6':
            show_bank_transactions(user_id)
        elif choice == '7':
            demand_balance = calculate_demand_balance(user_id)
            print("Demand Account Balance:", demand_balance)
        elif choice == '8':
            amount = Decimal(input("Enter the amount to deposit: "))
            deposit_money(user_id, amount)
        elif choice == '9':
            amount = Decimal(input("Enter the amount to withdraw: "))
            withdraw_money(user_id, amount)
        elif choice == '10':
            print("Logged out.")
            # Redirect to welcome page or print logout message
            main_menu()  # Assuming you have a welcome_page function
            break  # Exit the loop immediately
        else:
            print("Invalid choice. Please enter a valid option.")

# Function for main menu
def main_menu():
    while True:
        print("\nWelcome to the Trading Platform!")
        print("1. Login")
        print("2. Create New Account")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            login()
        elif choice == '2':
            create_user()
        elif choice == '3':
            print("Exiting the Trading Platform.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")



if __name__ == "__main__":
    connection = connect_to_database()
    cursor = connection.cursor()
    main_menu()
