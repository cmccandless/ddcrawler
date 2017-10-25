class AnnotatedList(list):
    def __init__(self, label, *args):
        list.__init__(self, args)
        self.__name__ = label
