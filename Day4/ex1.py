# Problem #1
# write a program that reads a passage and reverses the order of 
# letters in each word while keeping the word order intact. Use function.
# Eg- input - I am Sayur
# Output I ma ruyaS


def reverse_words(passage):
    words = passage.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

input_passage = "I am Sayur"
output_passage = reverse_words(input_passage)
print(f"Input: {input_passage}\nOutput: {output_passage}")
