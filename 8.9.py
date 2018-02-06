from test import testEqual

def remove(substr,the_str):
    # find method returns index of first occurance
    index = the_str.find(substr)
    if index < 0: # substr doesn't exist in the_str
        return the_str
    # return_str variable made by index splicing of the_str around removed substr
    return_str = the_str[:index] + the_str[index+len(substr):]
    return return_str

# get user input for example
b_str = raw_input("What is the string you wish to remove from?")
a_str = raw_input("What would you like to remove from that?")
print(remove(a_str, b_str))

testEqual(remove('egg', 'bicycle'), 'bicycle')
testEqual(remove('an', 'banana'),'bana')
testEqual(remove('cyc', 'bicycle'), 'bile')
testEqual(remove('iss', 'Mississippi'), 'Missippi')