def count(text,ltr):
    count = 0
    for c in text:
        if c == "a":
            cpunt += 1
    return (count)

print (count ("banana","b") == 2)
print (count ("banana","b") == 2)

#Number 12

def find2 (strng, ch, start):
    ix = start
    while ix < len(strng):
        if strng [ix] == ch:
            return ix
        ix += 1
    return -1

print (find2("banana", "a", 2))
test (find2("banana", "a", 2) == 3)