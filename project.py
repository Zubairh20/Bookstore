# create a bookstore dictionary with book titles and their prices
book_store = {
    "moby dick": 12.00,
    "botchan": 10.50,
    "grapes of wrath": 11.00,
    "limberlost": 10.00,
    "candide": 15.99,
    "the odyssey": 14.50,
    "a country doctor": 12.50,
    "i capture the castle": 10.00,
    "the easy life in kamusari": 13.99
}


def main():
    sub_total = 0
    while True:

        # take user input
        book = input("Please enter your book title or Q to quit: ").lower()

        # check if item is in book_store dictionary
        if book in book_store:
            sub_total += book_store[book]
            print("sub_total: ${:.2f}".format(sub_total))

        # the user can exit if they don't choose any books
        elif book == "q":
            if sub_total == 0:
                break
            # the user does not want to choose any more books and wants total
            else:
                #calculate subtotal
                print("sub_total: ${:.2f}".format(sub_total))

                # call the calculate_tax function
                tax = calculate_tax(sub_total)
                print("tax: ${:.2f}".format(tax))

                #call the bonus_credit function to find out if user spent $50 or more
                bonus = round(bonus_credit(sub_total), 2)
                print("bonus credit: ${:.2f}".format(bonus))

                # user input to join book club or not
                book_club = input("Would you like to join the book club for $10 off of any book purchase(y/n)? ").lower()
                # calling the join_book_club function
                club = round(join_book_club(book_club), 2)
                print("Book club credit: ${:.2f}".format(club))

                # get the final total
                total = sub_total + tax - bonus - club
                total = round(total, 2)
                print("Total: $", total)
                break

    # final greeting for customer whether they make a purchase or not
    print("Thanks for stopping by!")

# a function to calculate the tax of 7%
def calculate_tax(x):
    tax = round(x * .07, 2)
    return tax


# if the user spends $50 dollars or more, they get $5 dollars off their purchase
def bonus_credit(payment):
    bonus = 0.00
    if payment >= 50:
        bonus += 5.00
    return bonus

# if the user says yes to joining the book club in main method they will receive $10 dollars off their purchase
def join_book_club(word):
    club = 0.00
    if word.startswith("y", 0):
        club += 10.00
        return club
    else:
        return club


if __name__ == "__main__":
    main()