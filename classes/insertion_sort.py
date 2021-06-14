from ..classes import converter


class InsertionSort:

    def sort(self, list):
        newList = []
        length = len(list) - 1
        converted = converter.convertList(list)
        for c in converted:
            if len(newList) == 0:
                newList.append(c)
            else:
                for n in newList:
                    if n > c:
                        newIndex = newList.index(n)
                        newList.insert(newIndex, c)
                        break
                    elif n < c and c > newList[-1]:
                        newList.append(c)
                        break
                    elif n < c and c > newList[newIndex + 1]:
                        newList.insert(newIndex + 2, c)
                        break
                    else:
                        pass

        expected = converter.convertBack(newList)
        return expected
