def solve(word):

    # Function to calculate the value of a consonant substring
    def consonant_value(s):
        return sum(ord(ch) - ord('a') + 1 for ch in s)

    vowels = 'aeiou'
    consonant_substrings = []
    current_substring = ''

    # Loop through the characters in the word
    for ch in word:
        if ch not in vowels:
            current_substring += ch
        else:
            if current_substring:
                consonant_substrings.append(current_substring)
                current_substring = ''

    if current_substring:
        consonant_substrings.append(current_substring)

    return max(consonant_value(substring) for substring in consonant_substrings)
