def bigger_Is_greater(w):
    x = len(w) - 2 
    y = len(w) - 1
    while not (w[x] < w[x+1] or x < 0):   # checking if letter is greater than other one
        x -= 1
    if x < 0:           #  printing no answer if word can't be smaller
        print('no answer')
    else:               # changing positions cause letter is greater 
        while not w[y] > w[x]:               
            y -= 1
        w[x], w[y] = w[y], w[x]       
        w[x+1:] = reversed(w[x+1:])
        print(''.join(w))

n = int(input('Enter amount of Words to Enter - '))
for i in range(n):
    words = input('Enter word: ')
    words_list = list(words)
    bigger_Is_greater(words_list)


    