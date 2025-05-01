def count_words(text): #Count the words in the file, return total
    words = text.split()
    word_count = len(words) #Give the length of the test
    return word_count

def count_chars(text):
    char_counts = {}
    for c in text:
        if c.lower() in char_counts:
            char_counts[c.lower()] += 1
        else:
            char_counts[c.lower()] = 1



    return char_counts
    