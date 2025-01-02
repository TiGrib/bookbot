def get_text(file_path: str):
    with open(file_path) as f:
        return f.read()


def count_words(text: str):
    return len(text.split())


def count_chars(text: str):
    words = text.split()
    count = {}
    for word in words:
        for char in word.lower():
            if count.get(char, None):
                count[char] += 1
            else:
                count[char] = 1
    return count


def output_report(file_path: str):
    print(f"--- Begin report of {file_path} ---")
    text = get_text(file_path)
    print(f"{count_words(text)} words found in the document\n\n")
    chars = count_chars(text)
    for key, value in chars.items():
        print(f"The '{key}' character was found {value} times")


if __name__ == "__main__":
    output_report("books/frankenstein.txt")
