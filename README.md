15th March 2021, I started the Zuri training cohort 1 as a backend trainee. 

This repo consists of my projects during the training.

This is the [Youtube playlist](https://www.youtube.com/watch?v=_pE-jTcLXgY&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P) for the training's backend - python track

## Projects

### Mock ATM Project
   1. The user should see the current date and time after they log in
   
   2. When the user selects option 1, they should be presented with the following:
    
    - How much would you like to withdraw (receive input from the user), output "take your cash"

   3. When the user selects option 2, present them with the following options:
    
    - How much would you like to deposit? (receive input from the user), output current balance.

   4. When the user selects complaint, present them with the following options:
    
    - What issue will you like to report? (Receive input from the user), output "Thank you for contacting us"
   
   *I used lists, dictionary, if and else statement, string methods, input and arithmetic operands*
   
   [Youtube Link](https://www.youtube.com/watch?v=KuZwwbNBhY0&list=PLxuUHF3OiqfWAITD4gPUHZ1GcYRqmyF7P&index=15) and [Github Link to file](https://github.com/PrechyDev/Zuri/blob/main/mock_atm.py)

   [Updated project](https://github.com/PrechyDev/Zuri/blob/main/updated_mock_atm.py) with login, register and a few other functions
    
    
### [Budget App](https://github.com/PrechyDev/Zuri/blob/main/budget.py)
   Create a Budget class that can instantiate objects based on different budget categories like food, clothing, and entertainment. These objects       should allow for
   1.  Depositing funds to each of the categories
   2.  Withdrawing funds from each category
   3.  Computing category balances
   4.  Transferring balance amounts between categories
   
   
### [Full-scale Mock ATM](https://github.com/PrechyDev/Mock-ATM)
This is a badass update to my initial project mock_atm which is in this repository. Here, I split the various functionalities into several files
importing them when needed as module.

#### Features
1. A `register` function connected to a local file system that creates a new user with a generated account number and saves the user details to a new txt file.

2. A `login` function that authenticates if the user input is a valid account number and if user exists. If password is correct, the user gets sent
to `bank operations`, else they try again.

3. A `banking` module  which has several banking operation functions connected to the local database, reading details from it and updating the account 
balance for every transaction.

4. A `validation` module that checks if the inputed account number is valid based on a few checks.

5. A `database` module that has basic `CRUD` functionalities for creating a new user, reading data from a user_file, updating a user account balance
and checking if a user exists before creating a new one.


### [Blog Project](https://github.com/PrechyDev/Django-Blog)
This project is a simple django blog creating using mainly ClassBasedViews and deployed to heroku.
The database used was SQLite.

#### Features

- A `blog` app which is the main component of the blog adding new posts and comments and displaying them to the user.

- An `accounts` app for registration and login

- A `Post` model that creates a new post with `author', `title` and post `body`.

- A  `Comment` model that creates a new Comment object using `post`, `author` and `comment`.

- A home page showing posts

- A post page showing post title, body and comment section

 -  A delete post page 

 -  An edit post page

 -  A register page (a new user can register, their details stored in a database file). 

-    login (checks in the file and logs them in if they are already registered)

-    reset password

-    logout

-    A comment section, you must be logged in to comment

 **[Check out blog](http://prechy-blog.herokuapp.com)**


