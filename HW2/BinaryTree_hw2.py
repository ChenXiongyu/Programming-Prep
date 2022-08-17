
# File: BinaryTree_hw2.py
# Author(s): xiongyuc

class BinaryTree:
    class _BTNode:
        def __init__(self, value, left = None, right = None):
            self._value = value
            self._left = left
            self._right = right
    def __init__(self):
        self._top = None
    def insert(self, value):
        if self._top == None:
            self._top = BinaryTree._BTNode(value)
        else:
            self._insert_help(self._top, value)
    def _insert_help(self, cur_node, value):
        if value < cur_node._value:
            if cur_node._left == None:
                cur_node._left = BinaryTree._BTNode(value)
            else:
                self._insert_help(cur_node._left, value)
        elif value > cur_node._value:
            if cur_node._right == None:
                cur_node._right = BinaryTree._BTNode(value)
            else:
                self._insert_help(cur_node._right, value)
    def __str__(self):
        return self._str_help(self._top)
    def _str_help(self, cur_node):
        if cur_node == None:
            return '';
        else:
            left_str = self._str_help(cur_node._left)
            right_str = self._str_help(cur_node._right)
            ret = str(cur_node._value)
            if left_str:
                ret = left_str + ' ' + ret
            if right_str:
                ret = ret + ' ' + right_str
            return ret
    def sum(self):
        return self._sum_help(self._top)
    def _sum_help(self, cur_node):
        if cur_node == None:
            return 0;
        else:
            return (self._sum_help(cur_node._left)
                    + cur_node._value
                    + self._sum_help(cur_node._right))
    def size(self):
        return self._size_help(self._top)
    def _size_help(self, cur_node):
        if cur_node == None:
            return 0
        else:
            return 1 + self._size_help(cur_node._left) \
                + self._size_help(cur_node._right)
    def print_pretty(self):
        ret = self._print_pretty_help(self._top)
        if ret:
            print(ret)
    def _print_pretty_help(self, cur_node):
        if cur_node != None:
            left_print = self._print_pretty_help(cur_node._left)
            right_print = self._print_pretty_help(cur_node._right)
            ret = str(cur_node._value)
            if left_print:
                left_print = '\n' + left_print
                left_print = left_print.replace('\n', '\n\t')
                ret = ret + left_print
            if right_print:
                right_print = '\t' + right_print
                right_print = right_print.replace('\n', '\n\t')
                ret = right_print + '\n' + ret
        else:
            ret = ''
        return ret
    def depth(self):
        return self._depth_helper( self._top )
    def _depth_helper(self,cur_node):
        if cur_node == None:
            return 0;
        else:
            return 1 + max(self._depth_helper(cur_node._left), 
                           self._depth_helper(cur_node._right))
    def __eq__(self, other):
        return str(self) == str(other)
    def min(self):
        return self._min_helper(self._top)
    def _min_helper(self, cur_node):
        if cur_node == None:
            return None
        else:
            while(cur_node._left is not None):
                cur_node = cur_node._left
        return cur_node._value
    def max(self):
        return self._max_helper(self._top)
    def _max_helper(self, cur_node):
        if cur_node == None:
            return None
        else:
            while(cur_node._right is not None):
                cur_node = cur_node._right
        return cur_node._value
    def mean(self):
            if self._top == None:
                return None
            else:
                return self.sum()/self.size()
    def __contains__(self, value):
        self = self._top
        while True:
            if self == None:
                return False
            if value == self._value:
                return True
            elif value > self._value:
                self = self._right
            else:
                self = self._left
    def copy(self):
        nums_list = []
        
        def nums_help(cur_node):
            if cur_node == None:
                return
            nums_list.append(cur_node._value)
            nums_help(cur_node._left)
            nums_help(cur_node._right)
        
        def nums(self):
            return nums_help(self._top)
        
        nums(self)
        c = BinaryTree()
        for num in nums_list:
            c.insert(num)
        return c
    def negate(self):
        self._top = self._negate_help(self._top)
    def _negate_help(self, cur_node):
        if cur_node != None:
            cur_node._value = - cur_node._value
            cur_node._right, cur_node._left = \
                self._negate_help(cur_node._left), self._negate_help(cur_node._right)
        return cur_node
