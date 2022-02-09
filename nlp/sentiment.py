from textblob import TextBlob

msg = "this is a good day to sleep early"

blob = TextBlob(msg)

print(blob.polarity)

if blob.polarity > 0:
    print("your message is positive")
elif blob.polarity < 0 :
    print("your message is negative")
else:
    print('you message is nuetral')