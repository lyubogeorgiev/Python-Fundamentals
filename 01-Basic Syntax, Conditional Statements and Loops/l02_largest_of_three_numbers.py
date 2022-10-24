first_number = int(input())
second_number = int(input())
third_number = int(input())

largest_number = third_number

if third_number < first_number > second_number:
    largest_number = first_number
elif third_number < second_number > first_number:
    largest_number = second_number

print(largest_number)
