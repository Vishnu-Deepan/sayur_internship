# Problem #2
# Write a program that reads a passage or string and counts the occurrences of two consecutive words 
# that are the same without any other specific word in between.
#  For example, count the occurrences of "apple apple" but not "apple orange apple."


def count_consecutive_occurrences(text):
    words = text.split()
    count = 0

    for i in range(len(words) - 1):
        if words[i] == words[i + 1]:
            count += 1

    return count

passage = "apple orange apple apple orange orange apple"
result = count_consecutive_occurrences(passage)
print(f"Occurrences of consecutive words: {result}")
