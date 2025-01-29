def firstPalindrome(words: list[str]) -> str:
    """
    Given an array of strings words, return the first palindromic string in the array. 
    If there is no such string, return an empty string "".

    A string is palindromic if it reads the same forward and backward.

    Possível solução: Two Pointer
    Melhor solução: inverter array com [::-1]
    """
    palindrome = ""

    for word in words:
        l, r = 0, len(word) - 1

        while l < r:
            if word[l] != word[r]: break
            l += 1
            r -= 1
        if l < r: continue

        return word

    return palindrome

words_1 = ["abc","car","ada","racecar","cool"]
words_2 = ["notapalindrome","racecar"]
print(firstPalindrome(words_1))