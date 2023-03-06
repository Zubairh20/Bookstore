### Hi there 👋

***Program Functionality***

The purpose of this program is to track information about purchases at a bookstore.  It keeps track of the buyer's own specific purchases, as well as as the bonus credit, the tax, the book club credit, and the final monetary total.  All of this is tracked in three functions in addition to the main() function.  The main() function calls the other three ones and takes care of tasks such as printing and inputting.

**project.py**

This file is where the important code of the program is located.  The code consists of a dictionary containing the names of various books and their corresponding prices, as well as multiple functions.  There is the main() function, where financial information is calculated and the other functions in the code are called.  There are three other functions in additon to the main() function.  The calculate_tax() function, which calcualtes the tax of 7%, the bonus_credit() function, which tracks whether or not the user receives a bonus credit, and the join_book_club() function, which tracks whether or not the user decides to join the book club.


*main()*

    - Stores variables that carry information based on the dictionary of the code, which holds the books and their prices.
    - Calls three additional functions and contains the primary input and print statements.
    - The final total is calculated here.
  
  
*calculate_tax(x)*

This function calculates the tax of 7%.  It multiplies payment by 7%, rounds the result to two decimals with the round() function, before returning it.  The result is then printed in the main method, where the function is called.


*bonus_credit(payment)*

Determines whether or not the user receives a discount or bonus credit of $5.  According to the if-else statement in the function, if the user makes a payment worth $50 or more, they receive it.  If there is no bonus credit, it is printed simply as $0.00.


*join_book_club(word)*

Tracks whether or not the user joins the book club when offered to do so.  According to the function's if-else statement, if the user accepts the offer, they receive $10 off of their book purchase.  If the user rejects the offer, the book club credit is simply printed as $0.00.


**test_project.py**

This file contains code testing project.py using pytest.  Aside from the main() function, which calls other functions to begin with, there are three other functions.  The three functions are test_calcualte_tax(), test_bonus_credit(), and test_join_book_club().  They each test the functionality of their corresponding functions in project.py depending on what input is entered while the program runs.


**requirements.txt**

This file contains list of pip-installable libraries used for project.  It simply serves as a reference for additional information about the building of this project.  In this file, the only one listed is pytest, as that was the only one that was needed for my work.
