def get_num_words(text):
    return len(text.split())

def get_num_chars(text):
    char_count = {}
    for i in range(0, len(text)):
        char = text[i].lower()
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count
