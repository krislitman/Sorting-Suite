import pytest
from ..classes.insertion_sort import InsertionSort


def test_insertion_sort_exists():
    insertion = InsertionSort()
    assert isinstance(insertion, InsertionSort)
