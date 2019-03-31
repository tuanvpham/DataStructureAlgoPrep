# https://leetcode.com/problems/min-stack/
# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) - - Push element x onto stack.
# pop() - - Removes the element on top of the stack.
# top() - - Get the top element.
# getMin() - - Retrieve the minimum element in the stack.


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_list = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.min_list) > 0:
            if x <= self.min_list[len(self.min_list)-1]:
                self.min_list.append(x)
        else:
            self.min_list.append(x)

    def pop(self) -> None:
        popElem = self.stack.pop()
        if popElem == self.min_list[len(self.min_list)-1]:
            self.min_list.pop()

    def top(self) -> int:
        return self.stack[len(self.stack)-1]

    def getMin(self) -> int:
        return self.min_list[len(self.min_list)-1]
