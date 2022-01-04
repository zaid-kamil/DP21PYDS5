def word_count(message):
    return len(message.split())

data = 'Hi everyone how are u all'
print(word_count(data))

data = 'This is so easy'
print(word_count(data))

print(word_count('word'))
