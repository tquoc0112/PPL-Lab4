# PPL LAB 4 _ ITITWE21039 + ITITWE21118
import math
from functools import reduce
import string

def main():
    while True:
        print("\nHi Ms Hanh, please Choose the question to solve:")
        print("1. One: Array operations")
        print("2. Two: Distance between two pixels")
        print("3. Three: Text processing pipeline")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            one()
        elif choice == "2":
            two()
        elif choice == "3":
            three()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

# Question 1 functions
def one():
    A = input_array()
    while True:
        print("\nChoose an operation to perform for One:")
        print("1. (1A) Calculate squares of numbers")
        print("2. (1B) Calculate cubes of numbers")
        print("3. (1C) Filter squares in range [20, 40]")
        print("4. (1D) Extract even numbers")
        print("5. Go back to main menu")
        
        choice = input("Enter your choice: ")
        if choice == "1":
            one_a(A)
        elif choice == "2":
            one_b(A)
        elif choice == "3":
            one_c(A)
        elif choice == "4":
            one_d(A)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

def input_array():
    A = []
    n = int(input("Enter the number of elements in your array of numbers: "))
    for i in range(n):
        ele = int(input(f"Enter element {i+1}: "))
        A.append(ele)
    print("The array of numbers you entered:")
    print(A)
    return A

def one_a(A):
    print("1A Using higher-order functions")
    squared_numbers = list(map(lambda x: x * x, A))
    print(squared_numbers)

def one_b(A):
    print("1B Using higher-order functions")
    cubed_numbers = list(map(lambda x: x * x * x, A))
    print(cubed_numbers)

def one_c(A):
    print("1C Using higher-order functions")
    squared_numbers = list(map(lambda x: x * x, A))
    squares_in_range = list(filter(lambda x: 20 <= x <= 40, squared_numbers))
    print(squares_in_range)

def one_d(A):
    print("1D Using higher-order functions")
    even_numbers = list(filter(lambda x: x % 2 == 0, A))
    print(even_numbers)

# Question 2 function
def two():
    x1, y1 = map(float, input("Enter coordinates of the first pixel (x1, y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of the second pixel (x2, y2): ").split())

    distance = lambda x1, y1, x2, y2: math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    result = distance(x1, y1, x2, y2)
    print(f"The distance between the two pixels is: {result}")

# Question 3 functions
def three():
    text = input("Enter the text to process: ")

    # Define individual text processing functions
    def remove_punctuation(text):
        return text.translate(str.maketrans('', '', string.punctuation))

    def to_lowercase(text):
        return text.lower()

    def split_text(text):
        return text.split()

    def filter_stop_words(words):
        stop_words = {"the", "is", "in", "and", "to", "a"}
        return [word for word in words if word not in stop_words]

    # Compose function to combine transformations
    def compose(*functions):
        return reduce(lambda f, g: lambda x: f(g(x)), functions)

    # Create the processing pipeline
    pipeline = compose(filter_stop_words, split_text, to_lowercase, remove_punctuation)
    result = pipeline(text)
    print("Processed text:", result)

if __name__ == "__main__":
    main()
