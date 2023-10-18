# Problem #1
# Read a passage from a file. (If you don't know how to handle files in Python, you can hardcode a long passage)
# Count the number of times the word 'the' followed by another 'the' without 'a' in between.


# Defining passage
passage = "The king went to the forest with the wife and a servant. The king shot a deer. The king went to the forest again the next day."

# Split the passage into words
words = passage.split()
count = 0

# Count double 'the' without 'a' in between
for i in range(len(words) - 1):
    if words[i].lower() == 'the' and words[i + 1].lower() == 'the':
        if i == 0 or words[i - 1].lower() != 'a':
            count += 1

print("Count:", count)
