"""
Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word
and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
"""

import re


def pig_latin_word_creator(word):
    # Locate the first instance of a vowel
    vowel_search = vowel_regex.search(word)  # Match object; contains the matched vowel

    # If a match is found, split up the word
    # Otherwise, no vowels were found in the given word and return the word
    if vowel_search:
        # Split the string at that first instance, but retain the vowel using partition
        partition_list = word.partition(vowel_search.group())
        beginning, middle, end = partition_list  # unpack tuple

        # Create pig latin word from pieces of the partitioned word
        pig_latin_end = beginning + "ay"
        pig_latin_beginning = middle + end + "-"
        pig_latin_word = pig_latin_beginning + pig_latin_end
    else:
        pig_latin_word = word

    return pig_latin_word


# Create a regex pattern of vowels
vowel_regex = re.compile(r'[aeiouAEIOU]')

# Prompt the user for an input
# TO-DO: expand to sentence
str = input("Enter a word:").strip()

word_list = str.split(" ")

pig_latin_sentence = ""

for index in word_list:
    pig_latin_sentence += pig_latin_word_creator(index) + " "

print(pig_latin_sentence)


