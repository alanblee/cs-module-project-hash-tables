def word_count(s):
    # get rid of the special characters
    special_char = [
        '"',
        ":",
        ";",
        ",",
        ".",
        "-",
        "+",
        "=",
        "/",
        "\\",
        "|",
        "[",
        "]",
        "{",
        "}",
        "(",
        ")",
        "*",
        "^",
        "&",
    ]
    filteredStr = "".join(filter(lambda char: char not in special_char, s))
    str_arr = filteredStr.lower().split()
    word_cache = {}
    for str in str_arr:
        if str not in word_cache:
            word_cache[str] = 0
        word_cache[str] += 1

    return word_cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(
        word_count(
            "This is a test of the emergency broadcast network. This is only a test."
        )
    )

