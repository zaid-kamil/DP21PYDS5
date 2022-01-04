# count the num of words with limited num of chars 

def word_counter(msg, limit):
    words = msg.split()
    wl = []
    for item in words:
        if len(item) == limit:
            wl.append(item)
    return len(wl)

data = '''The author who has made a
universe called cosmere is Brandon Sanderson. The author has written
a lot of books'''

print("11 letter words count is:", word_counter(data, limit=11))
