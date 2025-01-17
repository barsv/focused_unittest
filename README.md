# What is it for?

I use it when I need to debug only one test and I don't want to deal with command line parameters or modification of unittest.main().

# Installation

```bash
!pip install focused_unittest
```

# Usage

```
# test_example.py
import unittest
from focused_unittests import FocusedTestCase, focus

class TestExample(FocusedTestCase):

    @focus
    def test_add(self):
        self.assertEqual(2 + 3, 5)

    @focus
    def test_subtract(self):
        self.assertEqual(3 - 2, 1)

    def test_multiply(self):
        self.assertEqual(3 * 2, 6)

    def test_divide(self):
        self.assertEqual(6 / 2, 3)

if __name__ == '__main__':
    unittest.main()
```

Basically I change `unittest.TestCase` to `FocusedTestCase` and I add `@focus` decorator to the methods I need to debug. Now I can debug with just F5 in vscode.