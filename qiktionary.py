from random import randint
from string import ascii_lowercase
alpha = [a for a in ascii_lowercase]
english_file = 'coha-samples-lexicon.txt'
words = [line.rstrip('\n') for line in open(english_file, encoding='latin-1')][3:]
poss_words = []
poss_sized_words =[]
size = int(input('Enter word length -> '))
try:
    for i in range(len(words)):
        poss_words.append(words[i].split()[1])
    poss_words = list(set([f.lower() for f in poss_words if len(f) == size]))
    poss_words = [f for f in poss_words if len(set(f)) == size]
    for word in poss_words:
        if len([v for v in list(word) if v in alpha]) == len(word): poss_sized_words.append(word)
except IndexError:
    print(len(poss_words))
big_list = poss_sized_words
#print(big_list)
small_list = []

while len(big_list) > 5:
    if len(big_list) <= 30: print(big_list)
    loop = 'N'
    while loop is not 'Y':
        rand_word = big_list[randint(0, len(big_list) - 1)]
        print(f'Try {rand_word}')
        loop = input('suitable word ? -> ')

    count = int(input('How many correct? -> '))

    for w in big_list:
        if len([value for value in list(w) if value in list(rand_word)]) == count: small_list.append(w)
    big_list = list(set(small_list))
    small_list = []

print(big_list)

    
#five_letter_words = [word for word in english if len(word) == 5]
#possible_words = [word for word in five_letter_words if len(set(word)) == 5]
#print(f'{len(possible_words)} possible words found')

