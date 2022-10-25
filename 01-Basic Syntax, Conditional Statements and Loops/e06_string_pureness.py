n = int(input())

for i in range(n):
    sentence = input()
    sentence_type = 'pure.'
    dirty_symbols = [',', '.', '_']

    for symbol in dirty_symbols:
        if symbol in sentence:
            sentence_type = 'not pure!'
            break

    print(f'{sentence} is {sentence_type}')
