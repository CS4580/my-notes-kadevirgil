""" Library to calculate the number of digits
    for different algorithms
"""

from math import factorial as fac


def fac_length(num):
    """ Count the number of digits in a factorial number

    Args:
        num (int): interger value to calcualte factorial

    Returns:
        int: number of digits for factorial of input
    """
    result = fac(num)
    length = len(str(result))
    return length


def main():
    """ Driven Function
    """
    number = 5
    digits = fac_length(number)
    print(f'You have {digits} digits in factorial({number})')


if __name__ == '__main__':
    main()