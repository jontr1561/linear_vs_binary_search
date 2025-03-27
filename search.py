import random
import time


# Creation of SearchAlgorithm class
class SearchAlgorithms:
    def __init__(self):
        self.array = []


# function that generates an array of specific size filled with random integers
    def generate_array(self, size):
        size = int(size)  # converts the user inputted size variable to be an int
        self.array = random.sample(range(-2**32, 2**32), size)  # randomly generates an array of inputted size
        return self.array


# Performs a linear search for a target character given an array
    def linear_search(self, array, target):
        for character in array:  # goes through each element int the array in order
            if character == target:
                return array.index(character)  # presents the index of the character if it is found
        else:
            return -1  # returns "-1" in the case the target is not found in the array

# Performs a binary search for a target character given an array
    def binary_search(self, array, target):
        mid = len(array)//2  # finds the middle index of the array
        character = array[mid]  # assigns character variable as the character in the middle index of the array
        if character == target:
            return array.index(character)  # if character matches the target, the index of the character is returned
        elif character < target:
            new_array = array[mid:]
            return self.binary_search(new_array, target)  # if the character is less than the target, the function recurs with top half of the original array
        elif character > target:
            new_array = array[:mid]
            return self.binary_search(new_array, target)  # if the character is larger than the target, the function recurs with bottom half of the original array
        else:
            return -1


# Records the time it takes for both Linear and Binary search to perform on a sorted list
def test_sorted():
    instant = SearchAlgorithms()
    generated_array = instant.generate_array(input("Input size of array: "))
    choice = random.choice(generated_array)
    generated_array = sorted(generated_array)
    linear_start = time.time()
    linear = instant.linear_search(generated_array, choice)
    linear_end = time.time()
    linear_time = linear_end - linear_start
    print(f"The linear search took: {linear_time:.60f} seconds")
    print(f"The target is found at index {linear}")
    binary_start = time.time()
    binary = instant.binary_search(generated_array, choice)
    binary_end = time.time()
    binary_time = binary_end - binary_start
    print(f"The binary search took:{binary_time:.60f} seconds")
    print(f"The target is found at index {binary}")


test_sorted()


# Records the time it takes for both Linear and Binary search to perform on and unsorted array
def test_unsorted():
    instant = SearchAlgorithms()  # creates an instant of SearchAlgorithm class
    generated_array = instant.generate_array(input("Input size of array: "))  # generates a random array
    choice = random.choice(generated_array)  # generates a random character within the array
    linear_start = time.time()  # starts the timer for the linear search function
    linear = instant.linear_search(generated_array, choice)  # starts the linear search function
    linear_end = time.time()  # stops the timer for the linear search function
    linear_time = linear_end - linear_start  # gets the time it takes for the linear search function to complete
    print(f"The linear search took:{linear_time:.60f} seconds")
    print(f"The target is found at index: {linear}")
    binary_start = time.time()  # starts the timer for the binary search function
    binary = instant.binary_search(generated_array, choice)  # starts the binary search function
    binary_end = time.time()  # stops the timer for the binary search function
    binary_time = binary_end - binary_start  # gets the time it takes for the binary search function to complete
    print(f"The binary search took:{binary_time:.30f} seconds")
    print(f"The target is found at index: {binary}")


test_unsorted()
