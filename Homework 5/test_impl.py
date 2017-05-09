# "Property-based Testing"
# CIS 640 - Tu/Th 1:05
# Author: Christian J. Hughes

# NOTE: Based on the problem statement, it is assumed that all calls to enqueue will be called with valid/comparable values (with the exception of test_enqueue_bad_values_raise_valueerror()).

import hypothesis.strategies as st
from hypothesis import given
import impl
import pytest

# Generates a list of full of floats, text, integers, booleans, and other lists.
strategy = st.lists(elements=(st.floats(allow_nan=False, allow_infinity=False) | st.text() | st.integers() | st.booleans() | st.lists(elements=(st.integers()))))

# If a new empty Queue is created, then it has a length of 0.
def test_len_is_zero_for_empty_queue():
    q = impl.Queue()
    length = q.len()
    assert length == 0

# If there are n number of enqueues immediately followed by n number of dequeues performed on an empty Queue (no Queue altering operations in between, non-Queue altering operations are permissible), then the length of the Queue will be equal to 0.
@given(strategy)
def test_len_is_zero_after_enqueue_all_then_dequeue_all_on_empty_queue(a):
    q = impl.Queue()
    for x in a:
        q.enqueue(x)
    for x in a:
        q.dequeue()
    length = q.len()
    assert length == 0

# If the Queue is empty (defined as have length of 0), then calls to dequeue will return None.
def test_dequeue_on_empty_list_returns_none_without_interceding_operations():
    q = impl.Queue()
    ret_val = q.dequeue()
    assert ret_val == None

# If the Queue is empty (defined as have length of 0), then calls to dequeue will return None.
@given(strategy)
def test_dequeue_on_empty_list_returns_none_with_interceding_operations(a):
    q = impl.Queue()
    for x in a:
        q.enqueue(x)
    for x in a:
        q.dequeue()
    ret_val = q.dequeue()
    assert ret_val == None

# If a value being added to the Queue with the enqueue method is None, Nan, Inf, or -Inf, then ValueError Exception should be raised.
@pytest.mark.parametrize("a", [None, float("NaN"), float("Inf"), -float("Inf")])
def test_enqueue_invalid_values_raise_ValueError(a):
    with pytest.raises(ValueError):
        q = impl.Queue()
        q.enqueue(a)

# If enqueue is called, then the length of the Queue increases by 1 (for each sucessful call).
@given(strategy)
def test_enqueue_single_call_increases_length_by_one(a):
    q = impl.Queue()
    q.enqueue(a) # Throw the entire list as an entry on the Queue for giggles.
    length = q.len()
    assert length == 1

# If enqueue is called, then the length of the Queue increases by 1 (for each sucessful call).
@given(strategy)
def test_enqueue_multiple_calls_each_increase_length_by_one(a):
    q = impl.Queue()
    correct_length = 0
    for x in a:
        q.enqueue(x)
        correct_length = correct_length + 1
    actual_length = q.len()
    assert correct_length == actual_length

# If dequeue is called "successfully" (defined as returning a non-None value), then the length of the Queue decreases by 1.
@given(strategy)
def test_dequeue_single_call_decreases_length_by_one_if_successful(a):
    q = impl.Queue()
    q.enqueue(a) # Throw the entire list as an entry on the Queue for giggles.
    old_length = q.len()
    q.dequeue()
    new_length = q.len()
    assert new_length == (old_length - 1)

# If dequeue is called "successfully" (defined as returning a non-None value), then the length of the Queue decreases by 1.
@given(strategy)
def test_dequeue_multiple_calls_each_decrease_length_by_one_if_successful(a):
    q = impl.Queue()
    # We enqueue everything twice so that this test will test length on a non-empty Queue.
    for x in a:
        q.enqueue(x)
    for x in a:
        q.enqueue(x)
    correct_length = q.len()
    for x in a:
        q.dequeue()
        correct_length = correct_length - 1
    new_length = q.len()
    assert new_length == correct_length

# If dequeue is called "not successfully" (defined as returning a None value), then the length of the Queue is not altered.
@given(strategy)
def test_dequeue_on_empty_stack_does_not_alter_length(a):
    q = impl.Queue()
    old_length = q.len()
    q.dequeue()
    new_length = q.len()
    assert old_length == new_length

# If there are n number of enqueues immediately followed by n number of dequeues (no Queue altering operations in between, non-Queue altering operations are permissible), then the dequeued values should be observed in the same order in which they were enqueued.
@given(strategy)
def test_enqueue_then_dequeue_many_values_must_return_in_same_order(a):
    q = impl.Queue()
    for x in a:
        q.enqueue(x)
    for x in a:
        item = q.dequeue()
        assert item == x

# If there are n number of enqueues immediately followed by n number of dequeues (no Queue altering operations in between, non-Queue altering operations are permissible), then the dequeued values should be observed in the same order in which they were enqueued.
@given(strategy)
def test_enqueue_then_dequeue_one_value_must_return_in_same_order(a):
    q = impl.Queue()
    q.enqueue(a)
    item = q.dequeue()
    assert item == a

# If dequeue is called "successfully" (defined as returning a non-None value), then the least recently enqueued value not already returned by dequeue will be returned.
@given(strategy)
def test_dequeue_returns_least_recently_enqueued_value(a):
    q = impl.Queue()
    queue_size = 0;
    for x in a:
        q.enqueue(x);
        queue_size = queue_size + 1
    if queue_size > 0:
        queue_size = queue_size - 1
        assert q.dequeue() == a[0]
    if queue_size > 0:
        for x in a:
            q.enqueue(x);
            queue_size = queue_size + 1
        assert a[1] == q.dequeue()

# If length is called multiple times in a row (with no interceding operations), then the same same value will be returned each time (the len() operation does not modify the Queue).
@given(strategy)
def test_len_does_not_alter_the_queue_when_called_multiple_times(a):
    q = impl.Queue()
    for x in a:
        q.enqueue(x)
    len1 = q.len()
    len2 = q.len()
    len3 = q.len()
    assert len1 == len2 == len3
