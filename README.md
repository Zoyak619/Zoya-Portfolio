Welcome to the Pop-Cafe Mini-Project!

Project background
The purpose of this project is to build a command line interface (CLI) cafe app (Pop-Cafe) in a busy business district. 
The cafe offers homemade lunches and drinks, and the client needs a simple but functional system to help manage products, couriers and customer orders. 
The project was developed during the Data Engineering Bootcamp with Generation. 

Client Requirements

* Maintain a collection of products and couriers 
  The app allows users to view, add, update, and delete products in both food/drink categories as well as the couriers.
  All data is sorted in dictionaries in lists and saved to .csv files. 

* When a customer makes a new order, to create this on the system 
  New customer orders can be created, viewed, updated, and deleted.
  Each order contains customers name, address, phone, chosen courier, status, and items ordered. 

* Update the status of an order i.e.: preparing, out-for-delivery, delivered. 
  All orders can be updated to reflect different status such as preparing, out-for-delivery, and delivered. 

* Upon exist off the app, all data to be persisted and not lost 
  All data for products, orders and couriers is saved to .csv files each time the app exists, so nothing is lost between app usage. This was from weeks 1 -4
  From weeks 5 - 6 - all data for products, couriers and orders have been updated to an SQL Database and csv is no longer needed. 

* Upon starting the app, to load all persisted data 
  When the app loads it automatically loads all the latest saved data from sql database. 

* Need to be sure the app has been tested and proven to work well 
  The code is split across modules with functions making it easier to write unit tests for each individual part later.
  The code is split for better readability.
  Main.py - Main application file which handles mnues and user navigation
  Products_db_app.py - CRUD operations for products
  Couriers_db_app.py - CRUD operations for couriers
  Orders_db_app.py - CRUD operations for orders
  Valid_phone.py - Phone validation function
  Test_valid_phone.py - unit tests for phone validation
  Test_view_orders.py - unit tests for viewing orders by status and couriers. 
  
* Need to receive regular software updates. 
  The app is modular and uses functions for every menu action, which makes it easier to extend / improve without having to re-write everything.

Week to Week progress 


How to run the app
Is this running in a venv? How do I get started using this app?

Unit Testing?


Project reflection
