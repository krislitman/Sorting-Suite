import pytest
import pdb
from ..classes import converter
from ..classes.merge_sort import MergeSort

# * Merge Sort Tests


def test_merge_sort_exists():
    ms = MergeSort()
    assert isinstance(ms, MergeSort)


def test_merge_sort_can_do_the_thing():
    ms = MergeSort()
    expected = ms.sort(["d", "b", "a", "c"])
    assert(expected == ["a", "b", "c", "d"])
