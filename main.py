def lengthDiff(str1, str2):
    return len(str1) - len(str2)


print(lengthDiff("Hello", "world"))

# 1. Define the function to accept one parameter — the word whose letters we are counting
# 2. Create a counter to keep track of unique letters
# 3. Loop through every letter in our alphabet string. If the current letter was found in our word, increase our count
# 4. Return the count after looping through all letters.
# The function returns the total number of unique letters in the string.
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"


def uniqueLetterCounter(word):
    lettercounter = 0
    for letter in letters:
        if letter in word:
            lettercounter += 1
    return lettercounter


print(uniqueLetterCounter("ramalamadingdong"))
print(uniqueLetterCounter("Apple"))


# 1. Define the function to accept two parameters. word for the input string and x for the single character
# 2. Create a counter to keep track of the occurrences
# 3. Loop through every letter in the string. If the current letter is equal to the input letter, increase our counter
# 4. Return the counter after looping through the entire string.
# The function returns the number of times a chosen letter appears in word.
def count_times_letter_appears(word, c):
    num_occurences = 0
    for letter in word:
        if letter == c:
            num_occurences += 1
    return num_occurences


print(count_times_letter_appears("ramamlamadingdong", "a"))
print(count_times_letter_appears("forever and always", "e"))


# 1. Define the function to accept two parameters. word for the input string and x for the second string we are searching for
# 2. Split the string into substrings based on the second input parameter
# 3. Count the number of instances the substring appeared in the first input string based on the split string
# 4. Return the result
# In order to get the correct result we need to return one less than the total number of split
# sections — in this example, "iss" was in the string twice, resulting in 3 sections. So we should return 3 - 1.
# function to compare against an entire string instead of a single character.
def count_multiple_letters(word, chars):
    splits = word.split(chars)
    return (len(splits) - 1)


print(count_multiple_letters("mississippi", "iss"))
print(count_multiple_letters("apple", "ple"))


# 1. Define the function to accept three parameters, one string and two characters
# 2. find the starting index of our substring using the second input parameter
# 3. find the ending index of our substring using the third input parameter
# 4. If neither of the indices are -1, return the portion of the first input parameter
# string between the starting and ending indices (not including the starting and ending index)
# If either of the indices are -1, that means the start or end of the substring didn’t exist in our string.
# Return the original string in this case.
# function that is able to extract a portion of a string between two characters.
def substring_between_letters(word, start, end):
    start_ind = word.find(start)
    end_ind = word.find(end)
    if start_ind > -1 and end_ind > -1:
        return (word[start_ind + 1:end_ind])
    return word


print(substring_between_letters("apple", "a", "e"))


# We need a new function that is able to accept two inputs: one for a sentence
# and another for a number. The function returns True if every single word in
# the sentence has a length greater than or equal to the number provided.
# 1. Define the function to accept two parameters, one string, and one number
# 2. Split up the sentence into an array of words
# 3. Loop through the words. If the length of any of the words is less than the provided number return False
# 4. If we made it through the loop without returning False then return True
def char_length(string, num):
    array1 = [string.split()]
    for word in array1:
        if len(word) < num:
            return False
        return True


print(char_length("once upon a time a long long time ago", 12))
