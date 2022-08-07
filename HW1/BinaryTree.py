
# File: BinaryTree.py
# Author(s): Xiongyu Chen

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
        return self._depth_help(self._top)
    def _depth_help(self, cur_node):
        depth = 0
        if cur_node != None:
            depth += 1
            if cur_node._left != None:
                left_depth = self._depth_help(cur_node._left)
            else:
                left_depth = 0
            if cur_node._right != None:
                right_depth = self._depth_help(cur_node._right)
            else:
                right_depth = 0
            depth += max(left_depth, right_depth)
        return depth
    def __eq__(self, other):
        self_list = str(self).split(' ')
        self_list.sort()
        other_list = str(other).split(' ')
        other_list.sort()
        return self_list == other_list
    def min(self):
        if str(self) != '':
            return min([int(i) for i in str(self).split(' ')])
        else:
            return None
    def max(self):
        if str(self) != '':
            return max([int(i) for i in str(self).split(' ')])
        else:
            return None
    def mean(self):
        if str(self) == '':
            return None
        else:
            value = [int(i) for i in str(self).split(' ')]
            return sum(value) / len(value)