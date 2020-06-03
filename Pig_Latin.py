"""
Pig Latin is a game of alterations played on the English language game.
To create the Pig Latin form of an English word the initial consonant sound is transposed to the end of the word
and an ay is affixed (Ex.: "banana" would yield anana-bay). Read Wikipedia for more information on rules.
"""

import re

# Create a regex pattern of vowels
vowel_regex = re.compile(r'[aeiou]')

# Prompt the user for an input
# TO-DO: expand to sentence
word = input("Enter a word:").strip().lower()

# Locate the first instance of a vowel
vowel_search = vowel_regex.search(word)
print(vowel_search.start())

# Split the string at that first instance, but retain the vowel
partition_list = word.partition(vowel_search.group())
print(partition_list)

# Append "-ay" to the first half of the string
end = partition_list[0] + "ay"
print(end)


