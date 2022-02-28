# Task 1
#Write code that takes a string as input and returns the string reversed
#I made two seperate ways to do this. Let me explain the first.
# 1.start funciton with 'def' reserved keyword
# 2.Name function 'reverse_string'.
# 3.Name one parameter 'string'.
# 4.Below, inside the scope, set return keyword and take 'string' and slice it.
# 5.The slice will be [::-1]. start and stop can be empty but step is set to '-1' as we want to reverse the string.
# 6.Leaving the scope of the function we can set a variable to recieve our returned value
# 7.The variable will equal a funtion call followed by user input so the user can choose the string they want reversed
# 8.Let her rip.

def reverse_string(string):
    return string[::-1]

reversed_string = reverse_string(input('Enter string to be reversed: '))
print(reversed_string)

#My second shorter means of reversing a string.

print(input('Enter string to be reversed: ')[::-1])

# Task 2
# Write code that takes a string as input and capitalize the first letter of each word. Words 
# will be separated by only one space. i.e. “hello world” should be outputted as “Hello 
# World” 
# Only did it one way this time.
# 1. set variable 'using_title_method' to recieve value.
# 2. Make set equals sign to input.
# 3. Inside the parens following 'input' give our user a cue to type a sentance.
# 4. Outside the parens after the cue to the user, put '.title()' method to capitalize whatever the user input.
# 5. ta daaaa
using_title_method = input('Enter your title: ').title()
print(using_title_method)

# Task 3 (unfinished)
# THIS TOOK A LOOOONG TIME!!!
# ""
#
original_string = 'haaardeeesst taaask'
print(len(original_string))
compacted_string = ''
count = 1
for index in range(18):
    if original_string[index] == original_string[index+1]:
        count += 1
    else:
        compacted_string = compacted_string + original_string[index] + str(count)
        count = 1

print(compacted_string)
#on line 47 try looking at the previous index instead of the following index pos.