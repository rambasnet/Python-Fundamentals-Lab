"""
File I/O Lab
By: FIXME

CSCI 110
Date: FIXME

Program prompts user to enter name of the file that contains 10 integers.
It opens, reads and stores the numbers into a list.
Program will then sort the numbers in the list in ascending and descending 
orders.
Program will then print the sorted lists to an output file along with the 
largest and smallest values in the list.

NOTE: All fixme's are each worth 10 points except for the FIXME 1 which is 
worth 20 points.
"""

from typing import List
from typing import TextIO


def read_data() -> List[int]:
    """Read data from a file.

    Returns:
        List[int]: List of integers
    """
    ints: List[int] = []
    # FIXME 1 (20 points):
    # Prompt user to enter input file name
    # open the file; read each number one line at a time;
    # and store it into ints list
    # close the file
    # return the ints
    return ints


def sort_list_ascending_order(ints: List[int]) -> None:
    """Sort the provided list in ascending order.

    Args:
        ints (List[int]): the list to be sorted.
    """
    # FIXME 2
    # sort ints list in ascending order


def sort_list_descending_order(ints: List[int]) -> None:
    """Sort the provided list in descending order.

    Args:
        ints (List[int]): the list to be sorted.
    """
    # FIXME 3
    # sort ints in descending order


def print_list(out_file: TextIO, ints: List[int]) -> None:
    """Print the list of integers to the output file.

    Args:
        out_file (TextIO): output file object to write to
        ints (List[int]): list of integers to write to file
    """

    for n in ints:
        # FIXME 4
        # write each `n` one line at a time to file
        # handled by out_file object
        pass
    out_file.write('\n')


def write_data(ints: List[int]) -> None:
    """Write data to output file.
    """
    output_file_name = input('Enter a file to write output to: ')
    # FIXME 10
    # write each integer in ints to the output file
    pass


def menu() -> None:
    """Display menu options to the user.
    """
    print("Menu Options:")
    print("1. Read numbers from a file")
    print("2. Sort numbers in ascending order and write to a file")
    print("3. Sort numbers in descending order and write to a file")
    print("4. Print largest number to the screen")
    print("5. Print smallest number to the screen")
    print("6. Print the numbers to the screen")
    print("7. Exit the program")


def main() -> None:
    """Main function that solves the problem.
    """
    integers = []  # list to store integers
    while True:
        menu()
        choice = input('Enter your choice (1-6): ')
        # math the choice and call the appropriate function
        # match concept introduced in Python 3.10
        match choice:
            case '1':
                integers = read_data()
            case '2':
                # FIXME 5
                pass
            case '3':
                # FIXME 6
                pass
            case '4':
                # FIXME 7
                pass
            case '5':
                # FIXME 8
                pass
            case '6':
                # FIXME 9
                pass
            case '7':
                print('Exiting the program. Goodbye!')
                break


if __name__ == '__main__':
    main()
