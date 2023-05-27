class ParseTree:
    def __init__(self, n_type, value=None, children=None):
        self.type = n_type
        self.value = value
        self.children = children or []

    def __str__(self, level=0):
        if self.value is None:
            ret = "\t" * level + self.type + "\n"
        else:
            ret = "\t" * level + self.type + ": " + str(self.value) + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret