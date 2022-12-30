def sum_numbers(num1, num2):
    return num1 + num2

def subtract (sum, num3):
    return sum - num3

def add_and_subtract(num1, num2, num3):
    sum_of_num1_and_num2 = sum_numbers(num1, num2)
    result = subtract(sum_of_num1_and_num2,num3)
    return result


first_num = int(input())
second_num = int(input())
third_num = int(input())

print(add_and_subtract(first_num, second_num, third_num))