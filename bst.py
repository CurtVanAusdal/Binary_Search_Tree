class BST:
    class BST_Node:
        def __init__(self, item):
            self.right = None
            self.left = None
            self.item = item

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def add(self, item):
        if self.root is None:
            self.root = BST.BST_Node(item)
        else:
            current_node = self.root
            while current_node:
                if item < current_node.item:  # compare Pair objects
                    if current_node.left is None:
                        current_node.left = BST.BST_Node(item)
                        return
                    current_node = current_node.left
                else:
                    if current_node.right is None:
                        current_node.right = BST.BST_Node(item)
                        return
                    current_node = current_node.right

    def find(self, item):
        current_node = self.root
        while current_node:
            if item < current_node.item:
                current_node = current_node.left
            elif item > current_node.item:
                current_node = current_node.right
            else:
                return current_node.item  # returns the Pair object
        raise ValueError('value does not exist in tree')

    def size(self):
        def size_help(root):
            if root is None:
                return 0
            else:
                return 1 + size_help(root.left) + size_help(root.right)

        return size_help(self.root)

    def height(self):
        def height_helper(root):
            if root is None:
                return 0
            left_height = height_helper(root.left)
            right_height = height_helper(root.right)
            return max(left_height, right_height) + 1

        return height_helper(self.root) - 1

    def preorder(self):
        order_list = []

        def help_pre(cur, listy):
            if cur is None:
                return
            listy.append(cur.item)  # append the Pair object
            help_pre(cur.left, listy)
            help_pre(cur.right, listy)

        help_pre(self.root, order_list)
        return order_list

    def postorder(self):
        post_list = []

        def help_post(cur, listy):
            if cur is None:
                return
            help_post(cur.left, listy)
            help_post(cur.right, listy)
            listy.append(cur.item)  # append the Pair object

        help_post(self.root, post_list)
        return post_list

    def inorder(self):
        in_list = []

        def help_in(cur, listy):
            if cur is None:
                return
            help_in(cur.left, listy)
            listy.append(cur.item)  # append the Pair object
            help_in(cur.right, listy)

        help_in(self.root, in_list)
        return in_list

    def remove(self, item):
        if self.root is None:
            return
        self.root = self.remove_help(self.root, item)

    def find_min(self, node):
        while node.left:
            node = node.left
        return node

    def remove_help(self, node, item):
        if node is None:
            return node
        if item < node.item:
            node.left = self.remove_help(node.left, item)
        elif item > node.item:
            node.right = self.remove_help(node.right, item)
        else:
            if node.left is None:
                val = node.right
                node = None
                return val
            elif node.right is None:
                val = node.left
                node = None
                return val
            val = self.find_min(node.right)
            node.item = val.item
            node.right = self.remove_help(node.right, val.item)
        return node
