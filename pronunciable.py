import math
"""
Task - Write a python program to list all pronunciable substrings of a given string. 
       A string is said to be pronunciable if it has at least one vowel (a, e, i, o, u) 
       after at-most 2 consonants (letters except a, e, i, o, u). 
       [Example - “zay” is pronunciable but “zby” is not).
Observation - 
  There should be atleast one vowel after max 2 consonants in the combinations of characters of given string
  Eg. If input is House
       then valid outputs are 
          1. H #Invalid output - 0 vowel present
          2. o #valid output - 1 vowel 0 consonant

Approach - recursive brute force
            1. Take Input
            2. Split input into a list
            3. score = 0
            4. make a queue
            5. pop the first element of queue
            4. If character is consonet
                call_func with score+1
               else
                call_func with score = 0
            6. add poped queue
"""
def comb(words:list, n: int, score: int, prefix: str, v: bool):
    
    if n < 0 or math.floor(score/3) > 0:
        return
    #check if vowel exists in the prefix
    if(v):
        print(prefix)
    # call function n times
    for i in range(0,n):
        # pop the first element of queue
        c = words.pop(0)
        if c in ['a', 'e', 'i', 'o', 'u']:
            comb(words, n-1, 0, prefix + c, True)
        else:
            comb(words, n-1, score+1, prefix + c, v | False)
        # add the poped function
        words.append(c)


def pronunciable():
    # input 
    words = input("Word? ").lower()
    words = [i for i in words]
    comb(words, len(words), 0, prefix="", v = False)

def main():
    pronunciable()
  
if __name__=="__main__":
    main()