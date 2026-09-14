def find_largest(first_number, second_number):
    if first_number > second_number:
        return first_number
    elif second_number > first_number:
        return second_number
    else:
        return"Numbers are equal."

largest_first = find_largest(5,6)
print(largest_first)

largest_second = find_largest(500,60)
print(largest_second)

largest_equal = find_largest(5,5)
print(largest_equal)