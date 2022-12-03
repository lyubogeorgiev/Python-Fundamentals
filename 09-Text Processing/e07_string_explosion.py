text = input()

count_to_remove = 0
i = 0
while True:
    i += 1

    if i >= len(text):
        break

    if text[i] == '>':
        # print(text[i + 1])
        count_to_remove += int(text[i + 1])
    elif count_to_remove > 0:
        # i -= 1
        while count_to_remove > 0:
            if text[i] != '>' and len(text) > i:
                # print(text[:i])
                # print(text[i + 1:])
                text = text[:i] + text[i + 1:]
                count_to_remove -= 1
                i -= 1
            else:
                break
        # for j in range(i + 1, i + 1 + count_to_remove):
        #     if text[j] != '>':
        #         text = text[:j] + text[j + 1:]
        #         count_to_remove -= 1
        #     else:
        #         break


print(text)

