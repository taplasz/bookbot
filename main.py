def main():
    text = get_text("books/frankenstein.txt")
    words = count_words(text)
    chars = count_characters(text)
    sorted_dict = convert_to_sorted_list(chars)

    print(f"Beginning the analysis of the book...")
    print(f"Number of words found in the book: {words}\n")
    
    for d in sorted_dict:
        if not d["char"].isalpha():
            continue
        print(f"Character {d["char"]} appears {d["num"]} times in the book")

    print(f"\nEnd of analysis. Thanks for using this bot!")   

def get_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    text_lower = text.lower()
    chars = {}
    for char in text_lower:
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] += 1
    return chars

def sort_on(dict):
    return dict["num"]

def convert_to_sorted_list(dict):
    dict_list = []
    for d in dict:
        dict_list.append({"char": d, "num": dict[d]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list

main()
