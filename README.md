Welcome to the Pop-Cafe Mini-Project!

Project background
The purpose of this project is to build a command line interface (CLI) cafe app (Pop-Cafe) in a busy business district. 
The cafe offers homemade lunches and drinks, and the client needs a simple but functional system to help manage products, couriers and customer orders. 

The project was developed during the Data Engineering Bootcamp with Generation. 

The app was built with:
* Python(weeks 1 - 6)
* CSV files for data persistence (weeks 1 - 4)
* PostgreSql database for products, couriers and orders (weeks 5 - 6)

Contents 
* client Requirements 
* Modules
* How to run the app 
* Unit testing / how to run unit testing 
* Project reflection 

Client Requirements

A week by week break down off what the client requried for this project: 

Week-1
* Create and product and add it to a list 
* View all prodcuts
* Stretch goal; Update or delete a product

Week-2
* Create a product or order, and add it to the relevant list
* View all products or orders
* Stretch goal, update or delete a product or order

Week-3
* Create a product, courier, or order and add it to a list
* View all products, couriers, or orders
* Update the status of an order
* Persist my data (products and couriers)
* Stretch goal, update or delete a product, order, or courier

Week-4
* Create a product, courier, or order dictionary and add it to a list
* View all products, couriers, or orders
* Update the status of an order
* Persist my data
* Stretch goal, update or delete a product, order, or courier
* Bonus list orders by status or courier

Week-5
* Create a product or courier and add it to a database table
* Create an order and add the order dictionary to a list
* View all products, couriers, or orders
* Update the status of an order
* Persist my data
* Stretch goal, update or delete a product, order, or courier
* Bonus list orders by status or courier
* Bonus track my product inventory
* Bonus import/export my entities in CSV format
  
Week-6
* Create a product, courier, or order and add it to a table
* View all products, couriers, or orders
* Update the status of an order
* Persist my data in a database
* Stretch goal, delete or update a product, order, or courier
* Bonus display orders by status or courier
* Bonus CRUD a list of customers
* Bonus track my product inventory
* Bonus import/export my entities in CSV format

Breakdown - 
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
  From weeks 5 - 6 - all data for products, couriers and orders have been updated to an postgreSQL Database and csv is no longer needed. 

* Upon starting the app, to load all persisted data 
  When the app loads it automatically loads all the latest saved data from sql database. 

* Need to be sure the app has been tested and proven to work well 
  The code is split across modules with functions making it easier to write unit tests for each individual part later.
  The code is split for better readability.

  Modules
  
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

[**/mini_project/**](./mini_project)

[week-1](./week-1)

[week-2](./week-2)

[week-3](./week-3)

[week-4](./week-4)

[week-5](./week-5)

[week-6](./week-6)



How to run the app

1. To run the app you will first need to clone the repository - This will allow you to download all the codes and files to run the app
2. You will then need to create and activate a virtual enviornment
   To do this you will need to run the following codes in your terminal -
   * python -m venv venv
   * for those with a windows device you will need to run - venv\scripts\activate
   * for those with a mac device you will need to run - source venv/bin/activate
3. Once you virtual enviorment is running you wll then need to install the dependecies and to do this you will need to run the following code in your terminal -
   pip install -r requirements.txt
4. You also need to ensure PostgreSQL is running and you have created the required database and tables.
5. Finally you are now ready to run the app - in your terminal you can run the app with the following code -
   python main.py 



Unit Testing?

The app contains some unit testing to ensure key functionallity works correcting. 
The tests which have been carried out so far are validating phone numbers, filtering orders by status and couriers. 

The test use pytest and unittest.mock 
To run the tests make sure to have pytest installed - 
to install pytest you will need to run the following code in your terminal - 
* pip install pytest

To run tests in the whole project/app you will need to run 
pytest

To run a specific file you will need to run - 
* pytest test_valid_phone. py - to view the validating phone
or
* pytest test_view_order.py - to view orders by status/couriers. 

Once run you should see all tests as pass 

Project reflection

How did your design meet the projects requirments? 
I made sure the app covers all the main requirements by letting users add, view, update, and delete products, couriers, and orders, all stored in a PostgreSQL database. Data is then saved and loaded properly every time, and I split the code into separate files for products, couriers, and orders, which makes it easier to manage. 

How did you gaurantee the project's requiremnts? 
I worked through the project step by step, following the weekly goals so nothing was missed. I wrote some unit tests to check my functions including happy, edge, and unhappy cases, and I also tested things manually while running the app. I committed regularly to GitHub, which helped me keep track of my progress and changes.

If you had more time, What would you improve? 
If I had more time, I’d add the other bonus features like product inventory and full CRUD for customers. I’d also maybe make the menus look a bit nicer. I’d like to write more unit tests for the database parts too.

What did you most enjoy implementing? 
I really enjoyed connecting everything to the database and running SQL queries in Python. It felt like a big step up from working with CSVs. I also liked getting my unit tests to pass because it was a good way to see that my logic was actually working. Adding the view orders by status feature was fun too because it made the app feel more complete.

challenges I faced? 
One of the first things I struggled with was breaking my code into separate files/modules. At first, it took refactoring my code to make sure everything still worked properly. It has made me relalise to implement modules from the start. 

Switching from CSV files to using a database was also a challenge for me. Setting up the tables, writing the SQL queries, and getting foreign keys to work took a lot of trial and error. Joining tables for the bonus task viewing orders by status was a little tricky but i got there in the end. 

Unit testing was another thing I found hard at first because it was new to me. Figuring out how to mock user input and write different types of tests happy, unhappy, and edge cases took some time, but I got the hang of it after practice and learning how to patch. 
