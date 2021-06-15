import pytest
from ..classes import converter


def test_merge_sort_exists():
    ms = MergeSort()
    assert isinstance(ms, MergeSort)
