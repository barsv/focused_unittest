import unittest
import ast
import inspect

# src: https://stackoverflow.com/a/31197273
def get_decorators(cls):
    target = cls
    decorators = {}

    def visit_FunctionDef(node):
        decorators[node.name] = []
        for n in node.decorator_list:
            name = ''
            if isinstance(n, ast.Call):
                name = n.func.attr if isinstance(n.func, ast.Attribute) else n.func.id
            else:
                name = n.attr if isinstance(n, ast.Attribute) else n.id

            decorators[node.name].append(name)

    node_iter = ast.NodeVisitor()
    node_iter.visit_FunctionDef = visit_FunctionDef
    node_iter.visit(ast.parse(inspect.getsource(target)))
    return decorators

# The rest of the code below was created by ChatGPT.

def focus(test_func):
    """Decorator to be used to select tests that need to be run."""
    def wrapper(*args, **kwargs):
        # Set a flag indicating the focused test
        test_func.__unittest_focus__ = True
        return test_func(*args, **kwargs)
    return wrapper

# Extend the unittest.TestCase to skip non-focused tests
class FocusedTestCase(unittest.TestCase):
    """Same as unittest.TestCase but adds support for the @focus decorator that selects tests that need to be run."""
    def setUp(self):
        # Get decorators for the current class
        decorators = get_decorators(type(self))
        
        # Check if there are focused tests
        focused_tests = [name for name, decs in decorators.items() if 'focus' in decs]
        if focused_tests and self._testMethodName not in focused_tests:
            self.skipTest('Skipped due to focus')