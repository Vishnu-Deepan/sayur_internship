# Question 4: Encode the user input using the following algorithm using the encode Key (a number)
# For each word in the odd position, move each letter in the word by the number of positions mentioned in the key.
# For words in the even position, reverse the word and then do the same as the odd position

def encode_sentence(input_sentence, key):
    # Split input_sentence into words
    words = input_sentence.split()
    encoded_words = []

    for i, word in enumerate(words):
        if i % 2 == 0:  # Even-positioned word
            reversed_word = word[::-1]  # Reverse the word
            encoded_word = ''.join([chr(ord(char) - key) for char in reversed_word])
        else:  # Odd-positioned word
            encoded_word = ''.join([chr(ord(char) + key) for char in word])

        encoded_words.append(encoded_word)

    encoded_sentence = ' '.join(encoded_words)
    return encoded_sentence

# Get input_sentence from the user
input_sentence = input("Enter a sentence: ")

# Get key from the user
key = int(input("Enter the encoding key (a number): "))

encoded_sentence = encode_sentence(input_sentence, key)
print(encoded_sentence)
