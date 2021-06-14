import pytest
from ..classes.bubble_sort import BubbleSort


def test_bubble_sort_exists():
    bubble = BubbleSort()
    assert isinstance(bubble, BubbleSort)


def test_bubble_sort_can_sort():
    bubble = BubbleSort()
    expected = bubble.sort(["d", "b", "a", "c"])
    assert(expected == ["a", "b", "c", "d"])
