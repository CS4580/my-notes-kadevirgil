""" Iterators in Python Example
    Date: October 7th, 2024
    Class: CS 4580 (Data Science) - Fall 2024
    Name: Kade Virgil
"""

def main():
    """Driven Function
    """
    iterable = ['Freshman', 'Sophomore', 'Junior', 'Senior']
    # Create an iterator for the iterable array 'iterable'
    iterator = iter(iterable)
    # print the first element of the iterable array, using the next() function
    print(next(iterator)) # Freshman
    print(next(iterator)) # Sophomore
    print(next(iterator)) # Junior
    print(next(iterator)) # Senior


    # TODO: Add a function with a try and except block to test the iterator

    # TODO: Then, use a Generator
    
    

if __name__ == '__main__':
    main()