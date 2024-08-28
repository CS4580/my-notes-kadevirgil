""" Counting the amount of words from an online .txt file
"""
from urllib.request import urlopen

def word_count(address):
    """ Calculates the numher of words in a file given an address

    Args:
        address (str): the path to the web file

    Returns:
        int: returns the number of words
    """
    # Read file from web
    temp = ""
    with urlopen(address) as data:
        for line in data:
            temp += line.decode('utf-8')

        words = temp.split()
        word_count = len(words)

    return word_count

def main():
    """ Driven Function
    """
    file_addr = 'http://icarus.cs.weber.edu/~hvalle/sample_data/poem.txt'
    count = word_count(file_addr)
    print(f'The number of words in the file is: {count}')


if __name__ == '__main__':
    main()