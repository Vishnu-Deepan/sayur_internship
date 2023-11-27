# Problem #1
# Generate the following output using for loop. Go until g.
# a
# aba
# abacaba
# abacabadabacaba
# abacabadabacabaeabacabadabacaba

def generate_pattern():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    result = ""

    for i in range(7):  #until g
        result += alphabet[i]
        if i > 0:
            result += result[::-1]

        print(result)

generate_pattern()
