import pytest
from ..classes.bubble_sort import BubbleSort


def test_bubble_sort_exists():
    bubble = BubbleSort()
    assert isinstance(bubble, BubbleSort)
