import pytest
from ..classes.bubble_sort import BubbleSort


def test_bubble_sort_exists():
    bubble = BubbleSort()
    assert isinstance(bubble, BubbleSort)


def test_bubble_sort_can_convert_values():
    bubble = BubbleSort()
    converted = bubble.convertList(["d", "b", "a", "c"])
    assert(converted == [100, 98, 97, 99])


def test_bubble_sort_can_convert_values_back():
    bubble = BubbleSort()
    converted = bubble.convertBack([100, 98, 97, 99])
    assert(converted == ["d", "b", "a", "c"])


def test_bubble_sort_can_sort():
    bubble = BubbleSort()
    expected = bubble.sort(["d", "b", "a", "c"])
    assert(expected == ["a", "b", "c", "d"])
