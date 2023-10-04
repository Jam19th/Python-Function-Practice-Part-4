# Write a Python function called max_num()to find the maximum of three numbers.
def max_num(a, b, c):
    return max([a, b, c])

print('max_num', max_num(1, 2, 3))

# Write a Python function called mult_list() to multiply all the numbers in a list.
def mult_list(my_list):
    if len(my_list) == 0:
        return 0
    prod = my_list[0]
    if len(my_list) > 1:
        for num in my_list[1:]:
            prod = prod * num
            
    return prod

print('mult_list', mult_list([1, 2, 3, 4, 5]))
print('mult_list', mult_list([1, 2, 3, 4, 5, 6]))

# Write a Python function called rev_string() to reverse a string.
def rev_string(my_string):
    return my_string[::-1]

print('rev_string', rev_string("Hello World!"))
print('rev_string',rev_string("123456789"))

# Write a Python function called num_within() to check whether a number falls in a given range.

    # The function accepts the number, beginning of range, and end of range (inclusive) as arguments.
def num_within(target, start, end):
    return target in range(start, end + 1)


    # Examples: num_within(3,2,4) returns True, num_within(3,1,3) returns True, num_within(10,2,5) returns False.
print('num_within', num_within(3, 2, 4))
print('num_within', num_within(3, 1, 3))
print('num_within', num_within(10, 2, 5))


# Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1], [1, 1]]

def pascal(n):
    if n < 1:
        print('n must be greater than 0')
    elif n == 1:
        print(triangle[0])
    else:
        row_number = 2
        while len(triangle) < n:
            row = []
            prev_row = triangle[row_number - 1]
            length = len(prev_row) + 1
            for i in range(length):
                if i == 0:
                    row.append(1)
                elif i > 0 and i < length -1:
                    value = triangle[row_number -1][i -1] + triangle[row_number -1][i]
                    row.append(value)
                else:
                    row.append(1)
            triangle.append(row)
            row_number += 1
            
        for row in triangle:
            print(row)
            
pascal(2)
pascal(5)
pascal(10)
