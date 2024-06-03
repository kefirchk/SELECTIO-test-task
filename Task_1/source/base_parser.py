import abc

class BaseParser(abc.ABC):
    @abc.abstractmethod
    def parse(self, outs):
        pass