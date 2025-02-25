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
