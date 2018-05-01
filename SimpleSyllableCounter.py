def syllables(word):

    # y can usually be considered as a syllable due to its pronunciation
    vowels = "aeiouy"
    
    # always separate syllables
    multi_syllables = ["ia"]

    # following are separate syllables unless they're at the end of the word
    multi_syllable_except_at_end = ["ie", "ya", "es", "ed"]
    
    word = word.lower()
    syllable_count = 0
    ends_with_vowel_flag = False
    last_letter = ""
    
    for letter in word:
        if letter in vowels:
            letter_combination = last_letter+letter
            if ends_with_vowel_flag and letter_combination not in multi_syllables \
                    and letter_combination not in multi_syllable_except_at_end:
                ends_with_vowel_flag = True
            else:
                syllable_count += 1
                ends_with_vowel_flag = True
        else:
            ends_with_vowel_flag = False
        last_letter = letter

    # es and ed are usually silent, so removing them
    if len(word) > 2 and word[-2:] in multi_syllable_except_at_end:
        syllable_count -= 1

    # disregard single e at the end, but not ee since it was counted previously
    elif len(word) > 2 and word[-1:] == "e" and word[-2:] != "ee":
        syllable_count -= 1

    return syllable_count