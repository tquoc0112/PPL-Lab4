# PPL LAB 4 _ ITITWE21039 + ITITWE21118
import math
import string 
from functools import reduce

def main():
    while True:
        print("\nChoose the question to solve:")
        print("1. Question 1: Array operations")
        print("2. Question 2: Distance between two pixels")
        print("3. Question 3: Text Pipeline processing ")
        print("4. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            question_1()
        elif choice == "2":
            question_2()
        elif choice == "3":
            question_3()
        elif choice == "4":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def question_1():
    A = input_array()
    while True:
        print("\nChoose an operation to perform for Question 1:")
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
    # Traditional way
    print("1A Using traditional algorithm")
    print("[", end="")
    for x in A:
        print(x * x, end="")
        if x != A[-1]:
            print(", ", end="")
    print("]")

    # Using higher-order functions
    print("1A Using higher-order functions")
    squared_numbers = list(map(lambda x: x * x, A))
    print(squared_numbers)

def one_b(A):
    # Traditional way
    print("1B Using traditional algorithm")
    print("[", end="")
    for x in A:
        print(x * x * x, end="")
        if x != A[-1]:
            print(", ", end="")
    print("]")

    # Using higher-order functions
    print("1B Using higher-order functions")
    cubed_numbers = list(map(lambda x: x * x * x, A))
    print(cubed_numbers)

def one_c(A):
    # 1C Using traditional algorithm
    print("1C Using traditional algorithm")
    squares_in_range = []
    for x in A:
        square = x * x
        if 20 <= square <= 40:
            squares_in_range.append(square)
    print(squares_in_range)

    # 1C Using higher-order functions
    print("1C Using higher-order functions")
    squared_numbers = list(map(lambda x: x * x, A))
    squares_in_range = list(filter(lambda x: 20 <= x <= 40, squared_numbers))
    print(squares_in_range)

def one_d(A):
    # Traditional way
    print("1D Using traditional algorithm")
    print("[", end="")
    for x in A:
        if x % 2 == 0:
            print(x, end="")
        if x != A[-1]:
            print(", ", end="")
    print("]")

    # Using higher-order functions
    print("1D Using higher-order functions")
    even_numbers = list(filter(lambda x: x % 2 == 0, A))
    print(even_numbers)

def question_2():
    # Prompt the user to input coordinates
    x1, y1 = map(float, input("Enter coordinates of the first pixel (x1, y1): ").split())
    x2, y2 = map(float, input("Enter coordinates of the second pixel (x2, y2): ").split())

    # Using lambda to calculate the distance between two pixels
    distance = lambda x1, y1, x2, y2: math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    
    # Calculate and display the result
    result = distance(x1, y1, x2, y2)
    print(f"The distance between the two pixels is: {result}")



def question_3():
    text = input("Enter the text to process: ")

    # removing punctuation
    remove_punctuation = lambda txt: txt.translate(str.maketrans('', '', string.punctuation))

    # lowercase string txt 
    to_lowercase = lambda txt: txt.lower()

    # splitting text into words in string txt
    split_text = lambda txt: txt.split()

    # filtering stop words from list of words in string txt  (common stop words: the, is, in, and, to, a)
    filter_stop_words = lambda words: [word for word in words if word not in {"the", "is", "in", "and", "to", "a"}]

    # Compose function to combine transformations
    def compose(*functions):
        return reduce(lambda f, g: lambda x: f(g(x)), functions)

    # Create the processing pipeline
    pipeline = compose(filter_stop_words, split_text, to_lowercase, remove_punctuation)
    result = pipeline(text)
    print("Processed text:", result)

if __name__ == "__main__":
    main()