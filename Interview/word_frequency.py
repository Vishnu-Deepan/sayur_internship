# 2. You are writing an essay. You don't want the any word to appear very frequently. Write a program that will take your essay as input (maybe from a file) and print the number of times each unique word appears in your essay.


# SOLUTION
import re
from collections import Counter

def count_word_frequencies(text):
    # Tokenizing
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Count the words using Counter
    word_freq = Counter(words)
    
    return word_freq

# Read the paragraph from the file
with open("essay.txt", "r") as file:
    essay_text = file.read()

word_frequencies = count_word_frequencies(essay_text)

# Printing the word frequencies
for word, frequency in word_frequencies.items():
    print(f"{word}: {frequency}")

# Sample Output (assuming "essay.txt" contains the essay text):
# you: 5
# are: 3
# writing: 2
# an: 3
# essay: 4
# ...
