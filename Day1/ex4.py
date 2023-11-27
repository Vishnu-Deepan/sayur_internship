# problem #4
# write a program to find if two strings are same.
# two string are considered same if both strings have same letters in same order, but from different starting point
# eg abcd is same as bcda (a is moved to the right)
# abcd is same as cdab 
# abcd is  not same as cdba

def are_strings_same(str1, str2):
    return len(str1) == len(str2) and str1 in str2 + str2

print(are_strings_same("abcd", "bcda"))    
print(are_strings_same("abcd", "cdab"))    
print(are_strings_same("abcd", "cdba"))  
print(are_strings_same("abcd", "acbd"))   
