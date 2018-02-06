#Number 11

def count(text,ltr):
    count = 0
    for c in text:
        if c == "a":
            cpunt += 1
    return (count)

print (count ("banana","b") == 2)
print (count ("banana","b") == 2)

#Number 12

def remove(phrase, word):
    new = word.replace(phrase, "")
    return new


print(remove("yes", "yesooo"))

#Number 6
layout = "{0:>10}{1:>2}{2:>5}{3:>5}{4:>5}{5:>5}{6:>5}{7:>5}{8:>5}{9:>5}{10:>5}{11:>5}{12:>4}{13:>5}"
print(layout.format("", "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"))
print(layout.format("", ":", "------", "-----", "------", "------", "------", "------", "------","------",
                    "------", "-----", "----", ""))
for i in range(1,13):
    print(layout.format(i, ":", i, i*2, i*3, i*4, i*5, i*6, i*7, i*8, i*9, i*10, i*11, i*12))

#Number 9
def remove_letter(letter, word):
    new = 0
    while new < len(word):
        if word[new] == letter:
            final = word[:letter] + word[letter:]
        new += 1
    return final


remove_letter("a", "apple")