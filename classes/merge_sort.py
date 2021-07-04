from ..classes import converter
import pdb


class MergeSort:

    def sort(self, original):
        if str in original:
            converted = converter.convertList(original)
        else:
            converted = original

        l = len(converted)
        if l > 1:
            mid = l//2
            left = converted[:mid]
            right = converted[mid:]

            self.sort(left)
            self.sort(right)

            first = 0
            second = 0
            third = 0

            while first < len(left) and second < len(right):
                if left[first] < right[second]:
                    converted[third] = left[first]
                    first = first + 1
                else:
                    converted[third] = right[second]
                    second = second + 1
                third = third + 1

            while first < len(left):
                converted[third] = left[first]
                first = first + 1
                third = third + 1

            while second < len(right):
                converted[third] = right[second]
                second = second + 1
                third = third + 1
        return converted
