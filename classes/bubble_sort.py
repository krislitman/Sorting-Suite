class BubbleSort:
    list = []

    def sort(self, list):
        converted = self.convertList(list)
        length = len(converted) - 1
        for c in converted:
            for l in range(length):
                if converted[l] > converted[l + 1]:
                    value = converted[l]
                    converted[l] = converted[l + 1]
                    converted[l + 1] = value

        expected = self.convertBack(converted)
        return expected

    def convertList(self, list):
        newList = []
        for l in list:
            newList.append(ord(l))

        return newList

    def convertBack(self, list):
        newList = []
        for l in list:
            newList.append(chr(l))

        return newList
