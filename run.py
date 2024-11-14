import math
#def main(argv):
#    print("From the input array please enter the question of which you want to see the results in")
#    Questions(input())

#def inputArray(input):
A = []
n = int(input("Enter number of elements of your array of numbers: (newline for each element)"))
for i in range(0, n):
        ele = int(input())
        # adding the element
        A.append(ele)  
print("The array of number you entered:")
print(A)
#def Questions(input):
#    x = input;
#
#    if (x == "1a"):
#        OneA()
#    elif (x == "1b"):
#        OneB()
    

#def OneA():
    #Traditional way
print("1A Using traditional algorithm")
print("[", end="")
for x in A:
        print (x*x, end="")
        if x != A[-1]:
            print (",", end=" ")
        
print("]")
#Using higher-order functions
print ("1A Using higher-order functions")
squared_numbers = list(map(lambda x: x * x,A))
print(squared_numbers)

#def OneB():
#Traditional way
print("1B Using traditional algorithm")
print("[", end="")
for x in A:
    print (x*x*x, end="")
    if x != A[-1]:
        print (",", end=" ")
        
print("]")

    #Using higher-order functions
print ("1B Using higher-order functions")
threepower_numbers = list(map(lambda x: x * x * x ,A))
print(threepower_numbers)

#def OneC():
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
squares_in_range = list(map(lambda x: x if 20 <= x <= 40 else None, squared_numbers))
squares_in_range = [x for x in squares_in_range if x is not None]
print(squares_in_range)

            
#def OneD():
#traditional way 

print("1D Using traditional algorithm")
print("[", end="")
for x in A:
    if ( x%2==0):
        print (x, end="")
    if x != A[-1]:
        print (",", end=" ")
print("]")

#using higher-order functions
check_round_numbers = list(map(lambda x: x if x%2 ==0 else None,A))
round_numbers = [x for x in check_round_numbers if x is not None]
print(round_numbers)