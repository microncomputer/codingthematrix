"""
2.12 Lab: Comparing voting records using dot-product
In this lab, we will represent a US senator’s voting record as a vector over R, and will use
dot-products to compare voting records. For this lab, we will just use a list to represent a
vector.
"""

'''
Task 2.12.1: Write a procedure create_voting_dict(strlist) that, given a list of
strings (voting records from the source file), returns a dictionary that maps the last name
of a senator to a list of numbers representing that senator’s voting record. You will need to
use the built-in procedure int(·) to convert a string representation of an integer (e.g. ‘1’)
to the actual integer (e.g. 1).
'''


def create_voting_dict(strlist):
    assert isinstance(strlist, list)

    # remove trailing newlines(\n) and split each element(string) by spaces into a list for each element
    s = [strlist[i].rstrip().split(' ') for i in range(len(strlist))]

    return {s[i][0]: [int(s[i][j]) for j in range(3, len(s[i]))] for i in range(len(s))}


def main():
    f = open('voting_record_dump109.txt')
    mylist = list(f)


if __name__ == '__main__':
    main()
