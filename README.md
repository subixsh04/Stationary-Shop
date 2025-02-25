# Stationary Shop Management System

## Overview:

This project is a Stationary Shop Management System developed using Python and MySQL. The system allows users to manage a stationary shop with three main categories:
 - BASICS
 - ART SUPPLIES
 - GENERAL
It enables customers to browse items, select products, and generate a bill based on their purchases.

## Features
 - User Authentication: Customers enter their name and phone number before making purchases.
 - Category-Based Item Selection: Customers can choose items from different categories.
 - Billing System: Generates an itemized bill with quantity, price, and total amount.
 - Database Integration: Uses MySQL to store and retrieve item details.

## Techonologies Used:
 - Python (for program logic and database interaction)
 - MySQL (for data storage and retrieval)

## Project Strucutre
 - User-Defined Functions:
    - `MENU()`: Displays the menu.
    - `BASIC()`, `ARTSUPPLIES()`, `GENERAL()`: Display category-specific items.
 - Parameterized SQL Queries: Used to fetch item prices dynamically from the database.

## Database Tables:
The system uses three tables:
 1. ss_basic - Stores basic stationary items like pens, pencils, erasers, etc.
 2. ss_art_supplies - Stores art-related supplies like brushes, sketch pens, colors, etc.
 3. ss_general - Stores general items like staplers, calculators, writing pads, etc.

## Installation & Setup
 1. Install Python and MySQL.
 2. Run the Python script to create the database and tables.
 3. Execute the program and follow the prompts to interact with the system.

## Conclusion
This system simplifies the management of a stationary shop, reducing paperwork and improving efficiency. It can be expanded with additional features and categories as needed.

## Authors
 1. Subiksha Vaidhyanathan
 2. Deepika Prabhakar
 3. Theertha
