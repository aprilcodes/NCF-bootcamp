# IDC 5100: Introduction to Data Science Bootcamp
# Assignment 2 - Python Basics and Version Control
"""
To-Do:
Implement a function "mean_min()" that takes in a list of integers and returns a
list, with the
first element being the mean of the input list and the second being the minimum
value in the input list.
Note:
You may not use functions from other packages that will do this for you. e.g.
np.min(), np.mean(). However,
there are multiple solutions to creating this function.
"""

def mean_min():
    global output_list
    output_list = []
    integer_list = [4, 7, 12, 6, 15]
    mean_value = sum(integer_list) / len(integer_list)
    sorted_list = sorted(integer_list)
    min_value = sorted_list[0]
    output_list = [min_value, mean_value]
    return output_list

mean_min()
print(output_list)
