import pytest
from ..classes import converter
from ..classes.insertion_sort import InsertionSort


def test_insertion_sort_exists():
    insertion = InsertionSort()
    assert isinstance(insertion, InsertionSort)


def test_insertion_sort_sorts():
    insertion = InsertionSort()
    expected = insertion.sort(["d", "b", "a", "c"])
    assert(expected == ["a", "b", "c", "d"])
