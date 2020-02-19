
def is_anagram(str,compare):
    lenStr=len(str)
    lenCompare=len(compare)
    if lenStr !=lenCompare:
        return -1
    check =0
    for i in str:
        if helper(i,compare):
            check+=1
            j=lenStr

    if check==lenStr:
        return 1
    return -1

def helper(char,compare):
    for letter in compare:
        if char == letter:
            return True
    return False
print(is_anagram("racecar","carrace"))
print(is_anagram("alien","neila"))
print(is_anagram("sauce","uasec"))
print(is_anagram("sue","npda"))
print(is_anagram("auce","usec"))
print(is_anagram("sues","uess"))

