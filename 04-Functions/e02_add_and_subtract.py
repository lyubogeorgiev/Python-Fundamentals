def add_and_subtract(a, b, c):
    def sum_numbers(first_num, second_num):
        return first_num + second_num

    def subtract(first_num, second_num):
        return first_num - second_num

    return subtract(sum_numbers(a, b), c)


num_a = int(input())
num_b = int(input())
num_c = int(input())

print(add_and_subtract(num_a, num_b, num_c))
