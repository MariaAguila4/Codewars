def email_list(domains):
    emails = []
    for users in domains:
        for user in domains[users]:
            emails.append(user + "@" + users)
    return (emails)


print(email_list(
    {"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"],
     "hotmail.com": ["bruce.wayne"]}))


def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group, users in group_dictionary.items():
        # Now go through the users in the group
        for user in users:
            if user not in user_groups:
                user_groups[user] = []
            user_groups[user].append(group)
    return (user_groups)


print(groups_per_user({"local": ["admin", "userA"],
                       "public": ["admin", "userB"],
                       "administrator": ["admin"]}))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)
print(wardrobe)


def add_prices(basket):
    # Initialize the variable that will be used for the calculation
    total = 0
    # Iterate through the dictionary items
    for element in basket:
        # Add each price to the total calculation
        # Hint: how do you access the values of
        # dictionary items?
        total += basket[element]
    # Limit the return value to 2 decimal places
    return round(total, 2)


groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
             "coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries))  # Should print 28.44


def format_address(address_string):
    # Declare variables
    pingu = ""
    # Separate the address string into parts
    pepe = address_string.split()
    print(pepe)
    # Traverse through the address parts
    for i in pepe:
        # Determine if the address part is the
        # house number or part of the street name
        # Does anything else need to be done
        # before returning the result?
        if (i.isdigit()):
            num = i
        else:
            pingu += " " + i
    # Return the formatted string
    return "house number {} on street named{}".format(num, pingu)


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))


# Should print "house number 55 on street named North Center Drive"

def highlight_word(sentence, word):
    return sentence.replace(word, word.upper())


print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))


def squaress(start, end):
    lista = []
    for n in range(start, end + 1):
        lista.append(n * n)
    return lista


def squares(start, end):
    return [n * n for n in range(start, end + 1)]


print(squares(2, 3))  # Should be [4, 9]
print(squares(1, 5))  # Should be [1, 4, 9, 16, 25]
print(squares(0, 10))  # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]


def car_listing(car_prices):
    result = ""
    for i in car_prices:
        result += "{} costs {} dollars".format(i, car_prices[i]) + "\n"
    return result


print(car_listing({"Kia Soul": 19000, "Lamborghini Diablo": 55000, "Ford Fiesta": 13000, "Toyota Prius": 24000}))


def combine_guests(guests1, guests2):
    # Combine both dictionaries into one, with each key listed
    # only once, and the value from guests1 taking precedence
    for i in guests2:
        if (i not in guests1):
            guests1[i] = guests2[i]
    return guests1


Rorys_guests = {"Adam": 2, "Brenda": 3, "David": 1, "Jose": 3, "Charlotte": 2, "Terry": 1, "Robert": 4}
Taylors_guests = {"David": 4, "Nancy": 1, "Robert": 2, "Adam": 1, "Samantha": 3, "Chris": 5}

print(combine_guests(Rorys_guests, Taylors_guests))


def count_letters(text):
    result = {}
    text = text.lower()
    text = text.replace(" ", "")
    print(text)
    # Go through each letter in the text
    for letter in text:
        if ( letter.isalpha()):
            if letter not in result:
                result[letter] = 1
            else:
                result[letter] += 1
    return result


print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence."))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}

animal = "Hippopotamus"
print(animal[3:6])
print(animal[-5])
print(animal[10:])
colors = ["red", "white", "blue"]
colors.insert(2, "yellow")
print(colors)

host_addresses = {"router": "192.168.1.1", "localhost": "127.0.0.1", "google": "8.8.8.8"}
print(host_addresses.keys())

#!/usr/bin/env python3
import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = numpy.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())
