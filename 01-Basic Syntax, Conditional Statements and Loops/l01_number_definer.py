number = float(input())


def print_num(number_type):
    if 0 < abs(number) < 1:
        print("small", end=" ")
    elif abs(number) > 1000000:
        print("large", end=" ")

    print(number_type)


if number == 0:
    print("zero")
elif number > 0:
    print_num("positive")
else:
    print_num("negative")
