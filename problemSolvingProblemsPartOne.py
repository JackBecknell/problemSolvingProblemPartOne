
# Task 1: Write code that takes a string as input and returns the string reversed.
# I made two seperate ways to do this. Let me explain the first.
# 1.start functon with 'def' reserved keyword
# 2.Name function 'reverse_string'.
# 3.Name one parameter 'string'.
# 4.Below, inside the scope, set return keyword and take 'string' and slice it.
# 5.The slice will be [::-1]. Here we are utilizing the third place holder to 'step' through the value that was input in reverse and once its complete our new value is returned. Both start and stop positions within the slice can be empty but step is set to '-1' as we want to reverse the string.
# 6.Leaving the scope of the function we can set a variable to recieve our returned value
# 7.The variable will equal a function call followed by user input so the user can choose the string they want reversed
# 8.Let her rip.

def reverse_string(string):
    return string[::-1]

reversed_string = reverse_string(input('Enter string to be reversed: '))
print(reversed_string)

# Task 2: Write code that takes a string as input and capitalize the first letter of each word. Words 
# will be separated by only one space. i.e. “hello world” should be outputted as “Hello 
# World” 
# 1. Declare a new function called 'old_school_title_method' with one parameter 'string'.
# 2. Set a blank string to be the final return value.
# 3. Declare a variable to count index position.
# 4. Start a for loop iterating over the string that was input.
# 5. Set first if statment to make the first letter capitalized as long as it isnt a space and add it to our return value. Then add 1 to the index pos.
# 6. Set next elif statment to check to see if the index value behind it was a space, if so capitalize the current character and add it to the return value. The add 1 to the index pos.
# 7. Set final else statment for all other letters to be added into the final return value without being tampered and add 1 to the index pos. ""
def old_school_title_method(string):
    title_method_string = ''
    index_position = 0
    for character in string:
        if index_position == 0 and index_position != ' ':
            title_method_string += string[index_position].upper()
            index_position += 1
        elif string[index_position-1] == ' ':
            title_method_string += string[index_position].upper()
            index_position += 1
        else:
            title_method_string += character
            index_position += 1
    return title_method_string

upper_case_string = old_school_title_method(input('Title method this: '))
print(upper_case_string)
# Task 3 
# THIS TOOK A LOOOONG TIME!!!
# 1.Declare variable 'compact_string' and set parameter to string.
# 2.Declare variable for the compacted string.
# 3.Declare variable for 'index_count'.
# 4.Declare variable for 'count'.
# 5.Declare a for loop iterating over characters in the string.
# 6.Set if statement to look for the end of the string by comparing index_count to the length of the string -1.
# 7.If previous step is true add compacted_string by the character we were on + the count and return the value.
# 8.On the next elif check to see if the current character == the following index.
# 9.If it's equal, add 1 to the count and index position before you move on to the next character. 
# 10. At the bottom declare the 'else' portion to take the compacted string add the character + count
# 11. Below that reset count to 1.
# 12. Then add 1 to the index count"

def compact_string(string):
    compacted_string = ''
    index_count = 0
    count = 1
    for character in string:
        if index_count == len(string)-1:
            return compacted_string + character + str(count)
        elif character == string[index_count+1]:
            count += 1
            index_count += 1
        else:
            compacted_string = compacted_string + character + str(count)
            count = 1
            index_count += 1

compacted_string = compact_string(input('Input string to be compacted: '))
print(compacted_string)