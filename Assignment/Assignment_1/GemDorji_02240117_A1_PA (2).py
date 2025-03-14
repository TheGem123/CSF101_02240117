# Function_1; Prime Number Sum Calculator

"""Compute the sum of prime numbers between start and end."""


def is_prime(n):  # Checking whether the the number 'n' is prime.
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


def sum_of_prime_numb():
    first = int(input("Enter the first digit:"))
    last = int(input("Enter the last digit: "))
    sum = 0
    for p in range(first, last+1):
        if is_prime(p):
            sum += p
    print(f"Sum of prime number:{sum}")


# Function_2; Length Unit converter

def meter_to_feet(meters):
    return meters*3.28  # 1Meter= 3.28 feet


def feet_to_meter(feet):
    return feet / 3.28


def length_converter():
    print("1. Meter to Feet")
    print("2. Feet to meter")

    options = input("choose either of the units (M or F): ")

    if options == 'M':
        meters = float(input("change length in meters to feet: "))
        feet = meter_to_feet(meters)
        print(f"{meters} meter is equal to {feet:.2f} feet.")
    elif options == 'F':
        feet = float(input("convert length in feet to meters: "))
        meters = feet_to_meter(feet)
        print(f"{feet} feet is equal to {meters:.2f} meters.")
    else:
        print("invalid option.")


# Function_3; Consonant Counter

def consonant_counter():
    string = input("Quote of the day please!:")
    # Defining both lowercase and uppercase
    consonants = "bcdfghjklmnpqrstvwxyzBCDFGHJKlMNPQRSTVWXYZ"
    consonants_count = 0  # Initialize consonant count

    for character in string:
        if character in consonants:
            consonants_count += 1
    print(f"Number of consonants: {consonants_count}")


# Function_4; Minimum-Maximum Finder

def min_max_numb():
    """Determine the minimum and maximum numbers from a list of user's input."""
    wanted_numb = int(input("Give me length of numbers you wish to run: "))
    numeric = []
    for x in range(wanted_numb):
        num = float(input(f"Enter number {x+1}: "))
        numeric.append(num)

    if numeric:
        print(f"Minimum digit: {min(numeric)}")
        print(f"Maximum digit: {max(numeric)}")
    else:
        print("Null number.")

# Function_5; Palindrome checker


def palindrome_checker():
    """Check if a given string is a palindrome."""
    elements = input("share your ideas: ")
    if elements == elements[:: -1]:
        print("There exists a palindrome.")
    else:
        print("No sign of palindrome")


# Function_6; word counter
def word_counter(filename):
    words_to_count = ["the", "was", "and"]
    word_count = {}

    """Initialze count for each word in the words_to_count list."""
    for word in words_to_count:
        word_count[word] = 0

        # check if the file exists
        try:  # Open the file and read the content
            with open(filename, 'r') as file:
                text = file.read()
                text = text.lower()
                text = text.translate(
                    str.maketrans(",",  "string.punctuation"))
                words = text.split()  # Splits the text into words

                # Count each word manually
                for word in words:
                    for key in word_count:
                        if word == key:
                            word_count[key] += 1
        except FileNotFoundError:
            return "File Not Found."

        return word_count


# Main program
while True:
    # Display the menu
    print("Select a function (1-6):")
    print("1. Calculate the sum of prime numbers")
    print("2. Convert length units")
    print("3. Count consonants in string")
    print("4. Find min and max numbers")
    print("5. Check for palindrome")
    print("6. Word Counter")
    print("0. Exit program")

    # Get the user's choice
    your_choice = int(input("Enter your choice:"))

    if your_choice == 1:
        sum_of_prime_numb()

    elif your_choice == 2:
        length_converter()

    elif your_choice == 3:
        consonant_counter()

    elif your_choice == 4:
        min_max_numb()

    elif your_choice == 5:
        palindrome_checker()

    elif your_choice == 6:
        word_counter()

    elif your_choice == 0:
        print("Thanks for taking time with us!")
        break

    else:
        print("Error. choose amoung the given options")
