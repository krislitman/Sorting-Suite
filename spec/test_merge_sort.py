import pytest
from ..classes import converter
from ..classes.merge_sort import MergeSort

# * Merge Sort Tests


def test_merge_sort_exists():
    ms = MergeSort()
    assert isinstance(ms, MergeSort)
