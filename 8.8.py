from test import testEqual

def mirror(input):
    # index splicing from problem 6
    return input + input[::-1]

# user input for visible example
text = raw_input("Type the string you would like to reverse.")
print("Here is your string, with its mirror: " + mirror(text))

print("Tests:")
testEqual(mirror('good'),'gooddog')
testEqual(mirror('Python'),'PythonnohtyP')
testEqual(mirror(''), '')
testEqual(mirror('a'),'aa')