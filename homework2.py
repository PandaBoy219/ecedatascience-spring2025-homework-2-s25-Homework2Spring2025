from typing import List, Tuple

def histogram(input_dictionary: dict) -> list:
    # data is a dictionary that contains the following keys: 'data', 'n', 'min_val', 'max_val'
    # n is an integer
    # min_val and max_val are floats
    # data is a list
    # input_dictionary: A dictionary with the following keys:
    # data: List of floats
    # n: integer
    # min_val: float
    # max_val: float

    # Returns:
    # A list representing the histogram

    # Write your code here

    # Get values from dictionary
    data = input_dictionary['data']
    n = input_dictionary['n']
    min_val = input_dictionary['min_val']
    max_val = input_dictionary['max_val']

    # Check if max and min values are the same
    if min_val == max_val:
        print('Error: min_val and max_val are the same value')
        return []

    # Ensure that n is a positive integer and not equal to 0
    if n <= 0:
        return[]
    
    # Swap the min and max values if neccessary 
    if min_val > max_val:
        min_val, max_val = max_val, min_val
    
    # Initialize the histogram with n number of 0s
    hist = [0] * n

    # Compute bin width
    w = (max_val - min_val) / n

    # Fill in the histogram
    for value in data:
        if min_val < value < max_val:
            bin_index = int((value - min_val) / w)
            if bin_index == n:
                bin_index -= 1
            hist[bin_index] += 1

    return hist

    

    


    # return the variable storing the histogram
    # Output should be a list
    pass

# Here, the function first checks if the lower and upper bounds are the same, 
# if they are it prints an error message and returns an empty list. 
# If lower bound is greater than upper bound, it swaps their values. 
# If number of bins is less than or equal to 0, it returns an empty list. 
# Then it initializes an empty list hist of length n and calculates the width of each bin. 
# Then it iterates through the data, 
# and for each value checks if it is within the range of the histogram and if it is, 
# it increments the bin it belongs to. Finally, it returns the histogram.

def combine_birthday_data(person_to_day: List[Tuple[str, int]], 
                          person_to_month: List[Tuple[str, int]], 
                          person_to_year: List[Tuple[str, int]]) -> dict:
    #person_to_day, person_to_month, person_to_year are list of tuples

    # Write your code here

    # return the variable storing output
    # Output should be a dictionary

    pass

# We first define the current year as 2024, which will be used to calculate the age of each person later on.
# We create an empty dictionary month_to_people_data that will store the final data in the format specified in the problem statement.
# We iterate over the both values in the tuple of the person_to_month list (note that person_to_month is a list of tuples, which means each item in the list is a tuple) 
# using a for loop. For each iteration, we extract the corresponding day, year and age values from the person_to_day and person_to_year lists using the current name as the "key".
# We then use the current month as the key and a tuple of (name, day, year, age) as the value to update the month_to_people_data dictionary.
# Only change the value to a list data type, when there are multiple entries with the same key. This will help append for other tuples to the same month.
# Finally, we return the month_to_people_data dictionary as the output of the function.
