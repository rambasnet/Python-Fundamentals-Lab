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

totalInts = 10


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


def main() -> None:
    """Main function that solves the problem.
    """
    integers = []  # list to store integers
    integers = read_data()
    output_file_name = input('Enter a file to write output to: ')
    with open(output_file_name, 'w', encoding='utf-8') as out_file:
        out_file.write("Numbers entered:\n")
        print_list(out_file, integers)
        # sort numbers
        sort_list_ascending_order(integers)
        out_file.write("Numbers sorted in ascending order:\n")
        print_list(out_file, integers)

        # FIXME 5
        # Call sort_list_descending_order function

        # FIXME 6
        # Write the sorted list in descending order to the output file

        # FIXME 7
        # Print the largest number to the output file

        # FIXME 8
        # Print the smallest number to the output file

    print(
        f'All done! Check the {output_file_name} for results.')


# FIXME 9
# Call main function if this module is run as the main module
