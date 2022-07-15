# Decided to do this exercise with 3 different ways

# First one with using dictionary

n= int(input("Enter amount of Words to Enter - "))
dict = {}
for i in range(n):   
    words = input('Enter word: ')
    if words in dict:      # adding words in dictionary and counting them
        dict[words] += 1     
    else:
        dict[words] = 1
   
print(len(dict))        # printing number of distinct words
print(' '.join([str(dict[i]) for i in dict]))      # printing words occurrences


# Second one: using several lists

n= int(input("Enter amount of Words to Enter - "))
mylist = []
distinctList = []
wordsCountList = []
for i in range(n):    # adding inputs in list
    words = input('Enter word: ')
    mylist.append(words)
for i in mylist:            # adding distinct words in another list and counting them
    if i in distinctList:
        continue
    else:
        distinctList.append(i)
        counts = mylist.count(i)
    wordsCountList.append(counts)

print(len(distinctList))       # printing number of distinct words
print(' '.join([str(i) for i in wordsCountList]))     # printing words occurrences

# Third one: using set
 
n= int(input("Enter amount of Words to Enter - "))
myList = []
for i in range(n):    # adding inputs in list
    words = input('Enter word: ')
    myList.append(words)

print(len(set(myList)))   # printing number of distinct words
counts = [myList.count(i) for i in set(myList)]    # counting words occurrences
print(' '.join([str(i) for i in counts]))    #  printing words occurrences