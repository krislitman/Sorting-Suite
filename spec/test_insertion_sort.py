import pytest
from ..classes.bubble_sort import InsertionSort


def test_insertion_sort_exists():
    insertion = InsertionSort()
    assert isinstance(insertion, InsertionSort)
