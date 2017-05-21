def find_anagrams(word, anagrams):
    word = sorted(word.lower())
    return [anagram for anagram in anagrams if sorted(anagram.lower()) == word]
