class AnnotatedList(list):
    def __init__(self, label, *args):
        super(AnnotatedList, self).__init__(args)
        self.__name__ = label
