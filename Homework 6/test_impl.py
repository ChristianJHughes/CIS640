# "Testing for Coverage (and Correctness)"
# CIS 640 - Tu/Th 1:05
# Author: Christian J. Hughes

# To run a test for code coverage, use the following command:
# pytest --cov-fail-under=100 --cov=. --cov-report=term-missing -s --cov-config=coverage.rc --timeout=180 --timeout_method=thread test_impl.py

# To run the tests independent of code coverage, use the following command:
# pytest test_impl.py

import hypothesis.strategies as st
from hypothesis import given
import impl
import pytest

# Generates a list of full of floats, text, integers, booleans, and other lists.
strategy = st.lists(elements=st.floats(allow_nan=False, allow_infinity=False), unique=True) | st.lists(elements=st.text(), unique=True) | st.lists(elements=st.integers(), unique=True) | st.lists(elements=st.booleans(), unique=True)

# If a new BST is initialized, then the root node should be equal to None.
@pytest.mark.timeout(2, 'thread')
def test_root_is_None_after_initialize():
    bst = impl.BST()
    result = bst.root
    assert result == None

# If a BST contains no items, then calls to delete() should return False regardless of argument passed to delete.
@pytest.mark.timeout(2, 'thread')
def test_delete_on_empty_BST_returns_False():
    bst = impl.BST()
    result = bst.delete("")
    assert result == False

# If a set of values is inserted into the BST and then immediately deleted, then the inserted values must no longer be present in the tree.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_insert_then_delete_values_should_be_no_longer_present_in_BST(a):
    bst = impl.BST()
    for x in a:
        bst.insert(x)
    for x in a:
        bst.delete(x)
    for x in a:
        assert bst.search(x) == False

# If a set of values is inserted into the BST, then calls to search() on that set of values should all be True.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_insert_then_search_all_values(a):
    bst = impl.BST()
    for x in a:
        bst.insert(x)
    for x in a:
        assert bst.search(x) == True

# If a search is called with a value that does not exist in the BST, then False must be returned.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_search_no_value_in_BST_returns_False(a):
    bst = impl.BST()
    for x in a:
        assert bst.search(x) == False

# If many values are inserted into the BST, then the root must not be None. Test Not complete.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_insert_many_values_root_is_not_None(a):
    bst = impl.BST()
    for x in a:
        bst.insert(x)
    result = bst.root


# If a set of values is inserted into the BST and then immediately deleted, then the root of the BST should be equal to None. Test Not complete.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_insert_then_delete_values_root_should_be_None(a):
    bst = impl.BST()
    for x in a:
        bst.insert(x)
    for x in a:
        bst.delete(x)
    result = bst.root

# If insert() is called with a value that already exists in the BST, then insert should return False.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_insert_values_that_already_exist_returns_False(a):
    bst = impl.BST()
    for x in a:
        bst.insert(x)
    for x in a:
        assert bst.insert(x) == False

# If insert() is called with a value that does not exist in the BST, then insert() should return True.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_insert_new_values_returns_True(a):
    bst = impl.BST()
    for x in a:
        assert bst.insert(x) == True

# If delete() is called with a value that exists in the BST, then delete() should return True.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_delete_valid_value_returns_True(a):
    bst = impl.BST()
    for x in a:
        bst.insert(x)
    for x in a:
        assert bst.delete(x) == True

# If delete() is called on values that do not exist in the BST, then delete() should return False.
@given(strategy)
@pytest.mark.timeout(2, 'thread')
def test_delete_invalid_value_returns_False(a):
    bst = impl.BST()
    for x in a:
        assert bst.delete(x) == False
