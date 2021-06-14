from ..classes import converter


class BubbleSort:

    def sort(self, list):
        converted = converter.convertList(list)
        length = len(converted) - 1
        for c in converted:
            for l in range(length):
                if converted[l] > converted[l + 1]:
                    value = converted[l]
                    converted[l] = converted[l + 1]
                    converted[l + 1] = value

        expected = converter.convertBack(converted)
        return expected
