This project implements a Binary Search Tree (BST) in Python, which is designed to store and manipulate Pair objects. Each Pair object consists of a letter (or character) and a count representing the frequency of that letter. The project allows for insertion, removal, and searching of Pair objects within the tree. It also supports common tree traversal techniques such as inorder, preorder, and postorder.

The primary purpose of this project is to provide a hands-on experience in implementing and understanding binary search trees. It is designed to work with text processing, where characters are read from a file and inserted into the tree based on their frequency, allowing for the counting of character occurrences in a text.

Key Features:
Insertion: Allows insertion of characters into the tree, storing the character and its associated count.
Traversal: Supports standard tree traversal methods including inorder, preorder, and postorder to explore the contents of the tree.
Removal: Implements a node removal function to delete nodes while maintaining the BST properties.
Size and Height Calculation: Includes methods to calculate the size and height of the tree.
Custom Pair Class: Uses a custom Pair class that encapsulates the character and its count, with relational methods for comparing and ordering objects.
Lessons Learned:
Understanding how binary search trees work and how they are implemented.
Working with tree traversal methods.
Handling custom objects in trees using relational methods like comparison operators (<, >, etc.).
How to manage file input and preprocess text for insertion into the tree.
Example Usage:
python
Copy code
from bst import BST, Pair

def make_tree():
    # Read text from file, preprocess, and insert into the BST
    new_text = "your text here".replace(" ", "").lower()  # preprocess
    tree = BST()
    for char in new_text:
        pair = Pair(char)
        try:
            node = tree.find(pair)
            node.count += 1  # Increment count if the character exists
        except ValueError:
            tree.add(Pair(char, 1))  # Add new pair if not found
    return tree.inorder()

def main():
    T = BST()
    print(make_tree())  # Display the inorder traversal of the BST