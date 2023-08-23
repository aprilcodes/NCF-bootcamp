
# IDC 5100: Introduction to Data Science Bootcamp

# 1.2: Implement a function "mean_min()" that takes in a list of integers and returns a
# list, with the first element being the mean of the input list and the second being the minimum
# value in the input list.

def mean_min():
    global output_list
    output_list = []
    integer_list = [4, 7, 12, 6, 15]
    mean_value = sum(integer_list) / len(integer_list)
    sorted_list = sorted(integer_list)
    min_value = sorted_list[0]
    output_list = [mean_value, min_value]
    return output_list

mean_min()
print(output_list)


# 2.1: Implement a method “price_per_sqft()” for the house class that 
# returns the price per square foot of a house object. Test your 
# method by creating a house object and calling the method on it.

class house:
    def __init__(self, sqft, price, num_rooms, num_stories, fireplace):
        self.sqft = sqft
        self.price = price
        self.num_rooms = num_rooms
        self.num_stories = num_stories
        self.fireplace = fireplace

    def price_per_sqft(self):
        self.per_sqft = self.price / self.sqft
        return self.per_sqft

home = house(4304, 799999, 16, 1, True)
print(home.price_per_sqft())
