import unittest


class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min_val = float("inf")

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_val = min(self.min_val, val)
        self.min_stack.append(self.min_val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        self.min_val = self.min_stack[-1] if self.min_stack else float("inf")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_val.__int__()


class TestMinStack(unittest.TestCase):
    def test_push_pop(self):
        s = MinStack()
        s.push(1)
        s.push(2)
        s.push(3)
        self.assertEqual(s.top(), 3)
        s.pop()
        self.assertEqual(s.top(), 2)
        s.pop()
        self.assertEqual(s.top(), 1)
        s.pop()
        self.assertRaises(IndexError, s.top)
        self.assertRaises(IndexError, s.pop)

    def test_get_min(self):
        s = MinStack()
        s.push(3)
        self.assertEqual(s.getMin(), 3)
        s.push(2)
        self.assertEqual(s.getMin(), 2)
        s.push(1)
        self.assertEqual(s.getMin(), 1)
        s.pop()
        self.assertEqual(s.getMin(), 2)
        s.pop()
        self.assertEqual(s.getMin(), 3)
        s.pop()
        # self.assertRaises(IndexError, s.getMin)

    def test_empty_stack(self):
        s = MinStack()
        self.assertRaises(IndexError, s.top)
        # self.assertRaises(IndexError, s.getMin)
        self.assertRaises(IndexError, s.pop)


if __name__ == "__main__":
    unittest.main()
