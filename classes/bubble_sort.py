class BubbleSort:
    list = []

    def sort(self, list):
        converted = self.convertList(list)
        import pdb
        pdb.set_trace()
        return list

    def convertList(self, list):
        newList = []
        for l in list:
            newList.append(ord(l))

        return newList
