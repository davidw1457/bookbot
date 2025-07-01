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

def sort_on(items):
    return items["num"]

def sort_dictionary(dic):
    dic_list = []
    for k, v in dic.items():
        dic_list.append({"char": k, "num": v})
    dic_list.sort(reverse=True, key=sort_on)
    return dic_list
