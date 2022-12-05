def single_letter_count(word, letter):
    """How many times does letter appear in word (case-insensitively)?

        >>> single_letter_count('Hello World', 'h')
        1

        >>> single_letter_count('Hello World', 'z')
        0

        >>> single_letter_count("Hello World", 'l')
        3
    """
    count = 0

    for lett in word:
        if lett.lower() == letter.lower():
            count = count + 1

    print(count)


single_letter_count("cheese", "e")
