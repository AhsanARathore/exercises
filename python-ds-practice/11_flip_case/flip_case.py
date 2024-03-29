def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    lst = []

    for letter in phrase:
        if to_swap.lower() == letter.lower():
            if letter.islower():
                lst.append(letter.upper())
            else:
                lst.append(letter.lower())

        else:
            lst.append(letter)

    return lst


result = flip_case("aAAAHhhh", "a")
print(result)
