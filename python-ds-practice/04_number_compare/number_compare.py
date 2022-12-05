def number_compare(a, b):
    """Report on whether a>b, b>a, or b==a

        >>> number_compare(1, 1)
        'Numbers are equal'

        >>> number_compare(-1, 1)
        'Second is greater'

        >>> number_compare(1, -2)
        'First is greater'
    """
    if a == b:
        print("numbers are equal")
    if a > b:
        print("first number is greater")
    if a < b:
        print("Second number is greater")


number_compare(1, 1)
number_compare(1, 2)
number_compare(3, 2)
