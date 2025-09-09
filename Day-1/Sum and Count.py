def Sum_of_numbers(numbers):
    Sum_of_numbers = sum(numbers)
    return Sum_of_numbers

def Count_of_numbers(numbers):
    Count_of_numbers = len(numbers)
    return Count_of_numbers

numbers = [1,2,3]
print("Given Numbers:",numbers)
print("The Sum is :",Sum_of_numbers(numbers))
print("The Count is :",Count_of_numbers(numbers))
