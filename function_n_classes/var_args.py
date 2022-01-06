def avg(*values):
    return sum(values)/ len(values)

def vowel_counter(vowel_char, *words):
    c = 0
    for word in words:
        vc = word.casefold().count(vowel_char)
        c +=vc
    return c

# comprehension
def vowel_counter_comp(vowel_char, *words):
    return sum([word.casefold().count(vowel_char) for word in words])


# print(avg(1,2,3,3,123,13,12,3))
# print(avg(1,12,3))
# print(avg(90,45,93,54,67,78))

count = vowel_counter('a','Apple','Banana','Cherry','Japan')
print("A found",count,"times")
count = vowel_counter_comp('e','Apple','Banana','Cherry','Japan')
print("E found",count,"times")

