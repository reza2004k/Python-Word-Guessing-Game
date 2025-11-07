import sys
def result(chance):
    for k in mylist:
        print(k, end=' ')
    print('\n\n▁▂▄▅▆▇█ 𝙔𝙤𝙪 𝙬𝙤𝙣 𝙬𝙞𝙩𝙝 ' + str(5 - chance) + ' 𝙬𝙧𝙤𝙣𝙜 █▇▆▅▄▂▁\n')
    sys.exit(0)


def func(chance):
    l = input('\n\nGuess the letter of the word => ' + f'kind of {kind}' + 'You have ' + str(chance) + ' chance:')

    if (l in word):
        for j in range(size_word):
            if word[j] == l:
                mylist[j] = str(l)

        if '-' not in mylist:
            result(chance)

    else:
        print('\n' + l + ' is not in the word\n')
        chance -= 1

    for k in mylist:
        print(k, end=' ')

    if (chance == 0):
        print("")
        print('\n\n██▓▒­░⡷⠂You lost ◔_◔ ,the word was ' + word + "⠐⢾░▒▓██ \n")
    else:
        func(chance)


import random

file = open('word.txt', 'r')
lines = file.readlines()
random_line = random.choice(lines)
word = ''
kind = ''
k = int(0)
for i in random_line:
    if i != ',' and k == 0:
        word += i
    elif i == ',':
        k = int(1)

    if (k == 1):
        if (i != ','):
            kind += i

size_word = len(word)
mylist = []
for i in word:
    mylist.append('-')

print()
for k in mylist:
    print(k, end=' ')

func(int(5))