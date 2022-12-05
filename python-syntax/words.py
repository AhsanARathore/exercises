def print_upper_words(words):
    '''prints out each word but on a seperate line'''

    for word in words:
        print(word.upper())


def print_upper_words_with_e(words):
    '''prints out each word but on a seperate line only if the word starts with e'''
    for word in words:
        if word.startswith('e') or word.startswith('E'):
            print(word.upper())


def print_upper_words_with_letter(words, start_with):
    '''prints out each word but on a seperate line only if they start with a certain letter'''
    for word in words:
        for letter in start_with:
            if word.startswith(letter):
                print(word.upper())
