import sys


class Stack:
    stack = []
    size_stack = 0

    def is_empty(self):
        return self.size_stack == 0

    def push(self, elem):
        self.stack.append(elem)
        self.size_stack += 1

    def pop(self):
        if self.size() != 0:
            elem = self.stack.pop()
            self.size_stack -= 1
            return elem
        else:
            return None

    def peek(self):
        elem = self.stack[-1]
        return elem

    def size(self):
        return self.size_stack


def check_brackets(check_str: str):
    brackets_pairs = {')': '(', ']': '[', '}': '{'}
    result_dict = {True: 'Сбалансированно', False: 'Несбалансированно'}

    stack = Stack()
    for br in check_str:
        if br in brackets_pairs.keys():
            if stack.is_empty():
                return result_dict[False]
                break
            elif stack.pop() != brackets_pairs[br]:
                break
        else:
            stack.push(br)

    return result_dict[stack.is_empty()]


if __name__ == '__main__':
    check_str_list = sys.argv[1:]
    for check_str in check_str_list:
        is_balanced = check_brackets(check_str.strip())
        print(f'{check_str.strip()} -> {is_balanced}')
