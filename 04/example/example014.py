from abc import *

class AbstrictClass(metaclass=ABCMeta):
    @abstractmethod
    def abcMethod(self):
        pass