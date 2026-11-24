def get_num_words(text):
    words = text.split()
    return len(words)


def get_char_count(text):
    text = text.lower()
    char_count = {}
    for char in text:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count


def sort_on(char_count: tuple[str, int]) -> int:
    return char_count[1]


def chars_dict_to_sorted_list(char_counts: dict[str, int]) -> list[tuple[str, int]]:
    pairs = []

    for char in char_counts:
        count = char_counts[char]
        pairs.append((char, count))

    return sorted(pairs, key=sort_on, reverse=True)
