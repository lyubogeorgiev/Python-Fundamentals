price_ratings = list(map(int, input().strip().split(", ")))
entry_point = int(input())
type_of_items = input()

left_sum = 0
right_sum = 0

if type_of_items == "cheap":
    # calculate left sum
    for i in range(entry_point):
        if price_ratings[i] < price_ratings[entry_point]:
            left_sum += price_ratings[i]

    # calculate right sum
    for i in range(entry_point+1, len(price_ratings)):
        if price_ratings[i] < price_ratings[entry_point]:
            right_sum += price_ratings[i]

else:
    # calculate left sum
    for i in range(entry_point):
        if price_ratings[i] >= price_ratings[entry_point]:
            left_sum += price_ratings[i]

    # calculate right sum
    for i in range(entry_point+1, len(price_ratings)):
        if price_ratings[i] >= price_ratings[entry_point]:
            right_sum += price_ratings[i]

bigger_sum = left_sum if left_sum > right_sum else right_sum
bigger_sum_name = "Left" if left_sum >= right_sum else "Right"
print(f'{bigger_sum_name} - {bigger_sum}')