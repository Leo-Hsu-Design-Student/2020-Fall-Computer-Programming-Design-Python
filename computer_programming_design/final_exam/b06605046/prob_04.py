# Problem 4. Anagrams - anagram() (20 pts)

def anagram(str1, str2):
    # write your answer here
    # complete the function
    anagram_bool=False#assign a boolean
    lower_str1=str1.lower()#standardized the string
    lower_str2=str2.lower()#standardized the string
    for i in range(len(lower_str1)):#see if there is the same character in str2
        if lower_str1[i] not in lower_str2 :
            anagram_bool=False
            break
        else:
            anagram_bool=True
    if anagram_bool==True:#if true, check if there is the same character in str1
        for i in range(len(lower_str2)):
            if lower_str2[i] not in lower_str1:
                anagram_bool=False
                break
            else:
                anagram_bool=True
    return anagram_bool



if __name__ == '__main__':
    print(anagram('Cat', 'Act'))
    print(anagram('arc', 'car'))
    print(anagram('Night', 'thing'))
    print(anagram('march', 'match'))
    print(anagram('hi', 'hit'))
