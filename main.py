# Check if a word is an anagrams 
# Example:
# find_anagrams("hello") --> False
# find_anagrams("racecar") --> True
first = input("The first to be scaled: ")
second = input("The second to be scaled: ")

def find_anagrams(first, second):
    # [assignment] Add your code here

    first = first.replace(" ", "")
    second = second.replace(" ", "")
    if (len(first) == len(second)):
        if(sorted(first) == sorted(second)):
            return True

    else:
        return False

print(find_anagrams(first, second))
