'''
Project: Binary Searc Tree
Author: Curtis Van Ausdal
Course: Intro to Data Struc. And Algorythms
Date: Apr 8 2023

Description:Not really sure yet

Lessons Learned: How to make binary search tree and fumble around for hours on implementing it

'''
from pathlib import Path
from string import whitespace, punctuation
from bst import BST


class Pair:
    ''' Encapsulate letter,count pair as a single entity.

    Realtional methods make this object comparable
    using built-in operators.
    '''

    def __init__(self, letter, count=1):
        self.letter = letter
        self.count = count

    def advance(self):
        self.count = self.count + 1

    def __eq__(self, other):
        return self.letter == other.letter

    def __hash__(self):
        return hash(self.letter)

    def __ne__(self, other):
        return self.letter != other.letter

    def __lt__(self, other):
        return self.letter < other.letter

    def __le__(self, other):
        return self.letter <= other.letter

    def __gt__(self, other):
        return self.letter > other.letter

    def __ge__(self, other):
        return self.letter >= other.letter

    def __repr__(self):
        return f'({self.letter}, {self.count})'

    def __str__(self):
        return f'({self.letter}, {self.count})'


def make_tree():
    ''' A helper function to build the tree.

    The test code depends on this function being available from main.
    :param: None
    :returns: A binary search tree
    '''

    # Read from the file character by character. If a character is not in the tree, insert it in its proper place and set its associated count value to 1.
    new_lines = []
    with open('around-the-world-in-80-days-3.txt', 'r') as infile:
        lines = infile.readlines()
        for line in lines:
            new_line = line.strip()
            new_lines.append(new_line)
        # print(new_lines)
        new = (" ".join(new_lines))
        change1 = new.replace(" ", "")  # remove whitespace
        change2 = change1.replace(",", "")  # remove commas
        change3 = change2.replace(".", "")  # remove period
        change4 = change3.replace("-", "")  # remove dash
        change5 = change4.replace(";", "")  # remove semicolon
        change6 = change5.replace("'", "")  # remove single quotes
        change7 = change6.replace('"', '')  # removedouble quotes
        change8 = change7.replace('(', '')  # remove open paran
        change9 = change8.replace(')', '')  # remove closing paren
        change10 = change9.replace(':', '')  # remove colon
        change11 = change10.replace("'", '')  # remove '
        change12 = change11.replace("?", '')  # remove question mark
        change13 = change12.replace("!", '')  # remove exlamation
        change14 = change13.replace("`", "")  # remove `
        final_string = change14.lower()


        # stringy = 'helloworld'
        # print(final_string)
        global counting
        counting = 1
        Tree = BST()
        # Read from the file character by character. If a character is not in the
        # tree, insert it in its proper place and set its associated count value to 1.

        for char in final_string:
            try:
                node = Tree.find(Pair(char))
                node.count +=1


            except ValueError:
                # print('valueerror encountered')
                Tree.add(Pair(char,1))
    return Tree.inorder()

def main():
    # Program kicks off here.
    T = BST()
    print(make_tree())

    # z = Pair('z',1)
    # a = Pair('a',1)
    # b = Pair('b',1)

    # print(z)
    # T.add(z)
    # T.add(a)
    # print(T.inorder())
    # T.remove(z)
    # T.add(b)

    print(T.inorder())


if __name__ == "__main__":
    main()
