intro = input('Enter your introduction=')
charactercount = 0
wordcount = 1
for i in intro:
    charactercount = charactercount+1
    if(i == ' '):
        wordcount = wordcount+1
print('Number of words in a string')
print(wordcount)
print('Number of letters in the string')
print(charactercount)